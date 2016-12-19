import time
import os
import sys
import numpy as np

import PL303
import E5071B

# Getting Terminal size
term_rows, term_columns = map(int, os.popen('stty size', 'r').read().split())

output_directory = 'vga_2016-12-19_40dBm_LNA'

if os.path.exists('/dev/tty.usbmodem456031'):
    psu_gain_serial = '/dev/tty.usbmodem456031'
elif os.path.exists('/dev/ttyACM0'):
    psu_gain_serial = '/dev/ttyACM0'
else:
    sys.exit('Can\'t find PSU')

vna_id_tuple = (2391, 1289)

calibration_s11 = 'cal/s11.sta'
calibration_s21 = 'cal/s21.sta'

psu_gain_serial_no = '456038'
vna_serial_no = 'MY42404018'

vtg_limit = 1 # Volts
vtg_gain_steps = range(4, 101) # e-10 Volts
cur_limit = 1e-3 # Ampere

freq_sweep_range = (3e5, 5e7) # Hz
output_power = -40 # dBm
sweep_points = 5e3 # Points
sweep_bandwidth = 1e3 # Hz

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
print('Output dir exists.')

# Connect to PSU
psu_gain = PL303.PL303(psu_gain_serial, psu_gain_serial_no)
print('Connected to Gain PSU')

# Connect to VNA
vna = E5071B.E5071B(vna_id_tuple, vna_serial_no)
print('Connected to VNA.')

try:
    if psu_gain.valid and vna.valid:

        print('Configuring PSU.')
        print('Setting voltage limit to {0:.2f}V.'.format(vtg_limit))
        psu_gain.vtg_limit = vtg_limit
        print('Setting current limit to {0:.3f}A.'.format(cur_limit))
        psu_gain.cur_limit = cur_limit
        print('Configuration of Gain PSU done.')
        print('-' * term_columns)

        print('Configuring VNA.')
        print('Setting VNA sweep range to ({0:.2E}, {1:.2E})Hz.'.format(*freq_sweep_range))
        vna.frequency_range = freq_sweep_range
        print('Sweep range set.')
        print('Setting output power to {0:.2f}dBm.'.format(output_power))
        vna.output_power = output_power
        print('Output power set.')
        print('Setting points to {0:.2f}Points.'.format(sweep_points))
        vna.sweep_points = sweep_points
        print('Sweep points set.')
        print('Setting bandwidth {0:.2f}Hz.'.format(sweep_bandwidth))
        vna.sweep_bandwidth = sweep_bandwidth
        print('Sweep points set.')
        print('Creating cal directory.')
        vna.create_directory('cal')
        time.sleep(1)
        print('Created cal directory.')
        print('Configuration of VNA done.')
        print('-' * term_columns)

        _in = input('Calibrate? y/n')
        if _in == 'y':
            print('Calibrating VNA.')
            # calibrate reflection
            print('Calibrating open.')
            _in = input('Please leave port 1 cable of the VNA unconnected. Then hit Enter.')
            vna.mode = 'S11'
            vna.calibration_method = ('SOLT1', 1)
            vna.calibrate('OPEN', 1)
            print('Calibrating open done.')

            print('Calibrating short.')
            _in = input('Please screw short on to the port 1 cable of the VNA. Then hit Enter.')
            vna.calibrate('SHORT', 1)
            print('Calibrating short done.')

            print('Calibrating load.')
            _in = input('Please screw a 50 Ohm load on to the port 1 cable of the VNA. Then hit Enter.')
            vna.calibrate('LOAD', 1)
            print('Calibrating load done.')
            print('Storing calibration.')
            vna.activate_calibration()
            vna.calibration_save_format = 'CDST'
            vna.store_calibration(calibration_s11)

            print('Calibration stored.')

            # Calibrating transmission
            print('Calibrating short for 2 port.')
            _in = input('Please short port 1 and port 2 cables of the VNA. Then hit Enter.')
            vna.mode = 'S21'
            vna.calibrate('THRU')
            vna.activate_calibration()
            vna.store_calibration(calibration_s21)
            print('Calibrating short done.')

        # _in = input('Connect device for reflection test to Port 1 and terminate it with 50 Ohms. Then hit Enter.')
        # vna.load_calibration(calibration_s11)
        # vna.output_power = output_power
        #
        # # Stepping through amplifications
        # psu_gain.output = True
        # for V in vtg_gain_steps:
        #     V /= 100
        #     print('Setting output voltage to {0:.2f}V.'.format(V), end='\r')
        #     psu_gain.voltage = V
        #     time.sleep(0.5)
        #     vna.display_format = 'MLIN'
        #     data = vna.single_measurement()
        #     np.savetxt('{0}/reading_reflection_{0:.2f}.csv'.format(output_directory, V), data, delimiter=',')
        #     # TODO: Read S11
        #     # TODO: Read input Z
        #     # TODO: Read SWR

        _in = input('Connect device for through test to Port 1 and 2. Then hit Enter.')
        # Load calibration s21
        vna.load_calibration(calibration_s21)
        vna.output_power = output_power

        # Stepping through amplifications
        for V in vtg_gain_steps:
            V /= 100
            print('Setting output voltage to {0:.2f}V.'.format(V), end='\r')
            psu_gain.voltage = V
            time.sleep(0.5)
            vna.display_format = 'MLIN'
            data = vna.single_measurement()
            np.savetxt('{0}/reading_transmission_{1:.2f}.csv'.format(output_directory, V), data, delimiter=',')
            # TODO: Read S21

        psu_gain.output = False
        print('Program done. Output off.')
        # Uncomment this to clear tripped errors
        # ser_psu_gain.write(b'TRIPRST\n')
    else:
        print('Invalid Device ID.')
        print('Exiting program.')
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt.')
    print('Exiting program.')
finally:
    psu_gain.output = False
    print('Program has shutdown.')
    # TODO: close VNA
