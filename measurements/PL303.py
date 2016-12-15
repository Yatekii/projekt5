import serial


from device import Device


class PL303(Device):
    def __init__(self, serial, device_addr=None):
        self._serial = serial.Serial('/dev/tty.usbmodem456031')

        ser_psu_gain.write(b'ADDRESS?\n')
        line = ser_psu_gain.readline()

        self.valid = True
        if device_addr:
            self.valid = line[:-2] == device_addr

    @property
    def vtg_limit(self):
        self._serial.write(b'V1?\n')
        return int(self._serial.readline()[:-2].split(' ')[2])

    @vtg_limit.setter
    def vtg_limit(self, value):
        if 0 < value < 30:
            self._serial.write(b'OVP1 %.2f\n' % value)
        else:
            raise ValueError('Given value {0} is not in required range (0, 30)V.'.format(value))

    @property
    def cur_limit(self):
        self._serial.write(b'I1?\n')
        return int(self._serial.readline()[:-2].split(' ')[2])

    @cur_limit.setter
    def cur_limit(self, value):
        if 0 < value < 3:
            self._serial.write(b'I1 %3.f\n' % value)
        else:
            raise ValueError('Given value {0} is not in required range (0, 3)A.'.format(value))

    @property
    def output(self):
        self._serial.write(b'OP1?\n')
        return int(self._serial.readline()[:-2])

    @output.setter
    def output(self, value):
            ser_psu_gain.write(b'OP1 {0}\n'.format(1 if value else 0))

    @property
    def voltage(self):
        self._serial.write(b'OP1?\n')
        return int(self._serial.readline()[:-2])

    @voltage.setter
    def voltage(self, value):
            if 0 < value < 30:
                self._serial.write(b'V1 %.2f\n' % value)
            else:
                raise ValueError('Given value {0} is not in required range (0, 30)V.'.format(value))
