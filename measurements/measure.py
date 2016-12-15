import serial
import time
ser = serial.Serial('/dev/tty.usbmodem456031')
print('Connected to {0}.'.format(ser.name))
ser.write(b'ADDRESS?\n')
line = ser.readline()
if int(line[:-2]) == 11:
    print('Setting voltage limit to 1 Volt.')
    ser.write(b'OVP1 1\n')
    print('Setting current limit to 0.001 Ampere.')
    ser.write(b'I1 1e-3\n')

    for V in range(4, 101):
        print('Setting output voltage to {0} Volts.'.format(V))
        ser.write(b'OP1 0\n')
        ser.write(b'V1 %de-2\n' % V)
        ser.write(b'OP1 1\n')
        time.sleep(1)

    # Uncomment this to clear tripped errors
    # ser.write(b'TRIPRST\n')
    ser.write(b'IFLOCK?\n')
    line = ser.readline()
    print(line)
    ser.close()
