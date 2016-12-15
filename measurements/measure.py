import serial
import time
import usbtmc

calibration_s11 = 'cal/s11.sta'
calibration_s21 = 'cal/s21.sta'

ser_psu_gain = serial.Serial('/dev/tty.usbmodem456031')
print('Connected to {0}.'.format(ser_psu_gain.name))
instr = usbtmc.Instrument(2391, 1289)
vna_device = instr.ask("*IDN?").split(',')
print('Connected to {0}.'.format(vna_device[1]))
try:
    ser_psu_gain.write(b'ADDRESS?\n')
    line = ser_psu_gain.readline()
    if int(line[:-2]) == 11 and vna_device[2] == 'MY42404018':
        print('Configuring PSU.')
        print('Setting voltage limit to 1 Volt.')
        ser_psu_gain.write(b'OVP1 1\n')
        print('Setting current limit to 0.001 Ampere.')
        ser_psu_gain.write(b'I1 1e-3\n')

        _in = input('Please leave in and out cables of the VNA open. Then hit Enter.')
        print('Calibrating open.')
        # TODO: Calibrate open
        # Define calibration format
        instr.write(':MMEM:STOR:STYP CDST')
        # Store calibration s11
        instr.write(':MMEM:STOR ""{0}""'.format(calibration_s11))
        print('Calibrating open done.')

        _in = input('Please short in and out cables of the VNA. Then hit Enter.')
        # TODO: Calibrate closed
        print('Calibrating short.')
        # Store calibration s21
        instr.write(':MMEM:STOR ""{0}""'.format(calibration_s21))
        print('Calibrating short done.')

        # Load calibration s11
        instr.write(':MMEM:LOAD ""{0}""'.format(calibration_s11))

        # Stepping through amplifications
        for V in range(4, 101):
            print('Setting output voltage to {0:.2f} Volts.'.format(V / 100), end='\r')
            ser_psu_gain.write(b'OP1 0\n')
            ser_psu_gain.write(b'V1 %de-2\n' % V)
            ser_psu_gain.write(b'OP1 1\n')
            # TODO: Read S11
            # TODO: Read input Z
            # TODO: Read SWR
            time.sleep(1)

        # Load calibration s21
        instr.write(':MMEM:LOAD ""{0}""'.format(calibration_s21))

        # Stepping through amplifications
        for V in range(4, 101):
            print('Setting output voltage to {0:.2f} Volts.'.format(V / 100), end='\r')
            ser_psu_gain.write(b'OP1 0\n')
            ser_psu_gain.write(b'V1 %de-2\n' % V)
            ser_psu_gain.write(b'OP1 1\n')
            # TODO: Read S21
            time.sleep(1)

        print('Program done. Output off.')
        ser_psu_gain.write(b'OP1 0\n')
        # Uncomment this to clear tripped errors
        # ser_psu_gain.write(b'TRIPRST\n')
    else:
        print('Unknown Device ID.')
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt.')
    print('Exiting program.')
finally:
    ser_psu_gain.write(b'OP1 0\n')
    ser_psu_gain.close()
    # TODO: close VNA
