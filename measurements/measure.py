import time
import os


import PL303
import E5071B

# Getting Terminal size
term_rows, term_columns = os.popen('stty size', 'r').read().split()

psu_gain_serial = '/dev/tty.usbmodem456031'
vna_id_tuple = (2391, 1289)

calibration_s11 = 'cal/s11.sta'
calibration_s21 = 'cal/s21.sta'

psu_gain_device_id = '11'
vna_serial = 'MY42404018'

vtg_limit = 1 # Volts
vtg_gain_steps = range(4, 101) # e-10 Volts
cur_limit = 1e-3 # Ampere

freq_sweep_range = (3e5, 5e7) # Hz

# Connect to PSU
psu_gain = PL303(psu_gain_serial, psu_gain_device_id)
print('Connected to Gain PSU')

# Connect to VNA
vna = E5071B(vna_id_tuple)
print('Connected to VNA.')

try:
    if psu_gain.valid and vna_device[2] == vna_serial:

        print('Configuring PSU.')
        print('Setting voltage limit to {0.2f}V.'.format(vtg_limit))
        psu_gain.vtg_limit = vtg_limit
        print('Setting current limit to {0.3f}A.'.format(cur_limit))
        psu_gain.cur_limit = cur_limit
        print('Configuration of VNA done.')
        print('-' * term_columns)

        print('Configuring VNA.')
        # Set ranges of sweeps
        print('Setting VNA sweep range to ({0:.2E}, {1:.2E})Hz.'.format(freq_sweep_range))
        vna.frequency_range = freq_sweep_range
        print('Sweep range set.')

        print('Calibrating VNA.')
        # calibrate reflection
        print('Calibrating open.')
        _in = input('Please leave port 1 cable of the VNA unconnected. Then hit Enter.')
        vna.mode = 'S11'
        vna.calibrate('OPEN', 1)
        print('Calibrating open done.')

        print('Calibrating short.')
        _in = input('Please screw short on to the port 1 cable of the VNA. Then hit Enter.')
        vna.calibrate('SHORT', 1)
        print('Calibrating short done.')

        print('Calibrating load.')
        _in = input('Please screw a 50 Ohm load on to the port 1 cable of the VNA. Then hit Enter.')
        vna.calibrate('THRU', 1)
        vna.activate_calibration()
        vna.calibration_save_format = 'CDST'
        vna.store_calibration(calibration_s11)
        print('Calibrating load done.')

        # Calibrating transmission
        print('Calibrating short for 2 port.')
        _in = input('Please short port 1 and port 2 cables of the VNA. Then hit Enter.')
        vna.mode = 'S21'
        vna.calibrate('THRU')
        vna.activate_calibration()
        vna.store_calibration(calibration_s21)
        print('Calibrating short done.')

        vna.load_calibration(calibration_s11)

        # Stepping through amplifications
        psu_gain.output = True
        for V in vtg_gain_steps:
            V /= 100
            print('Setting output voltage to {0:.2f}V.'.format(V), end='\r')
            psu_gain.voltage = V
            vna.display_format = 'MLIN'
            data = vna.current_data
            np.savetxt('reading {0}.csv'.format(V), data, delimiter=',')
            # TODO: Read S11
            # TODO: Read input Z
            # TODO: Read SWR

        # Load calibration s21
        vna.load_calibration(_s21)

        # Stepping through amplifications
        for V in vtg_gain_steps:
            V /= 100
            print('Setting output voltage to {0:.2f}V.'.format(V), end='\r')
            psu_gain.voltage = V
            vna.display_format = 'MLIN'
            data = vna.current_data
            np.savetxt('reading {0}.csv'.format(V), data, delimiter=',')
            # TODO: Read S21

        print('Program done. Output off.')
        psu_gain.output = False
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
    # TODO: close VNA
