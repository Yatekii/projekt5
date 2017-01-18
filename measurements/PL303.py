import serial


from device import Device


class PL303(Device):

    device_name = 'PL303-P'

    def __init__(self, ser, serial_no=None):
        super().__init__()
        self._serial = serial.Serial(ser)
        self._serial.write(b'*IDN?\n')
        device = self._serial.readline().replace(b' ', b'').decode('ascii').split(',')
        self._vna_manufacturer, self._model_nr, self._serial_no, self._version = device

        self.valid = True
        if serial_no:
            print(self._model_nr, self._serial_no)
            self.valid = self._model_nr == self.device_name and self._serial_no == serial_no

    def close(self):
        self._serial.close()

    @property
    def vtg_limit(self):
        self._serial.write(b'OVP1?\n')
        return int(self._serial.readline()[:-2].split(' ')[2])

    @vtg_limit.setter
    def vtg_limit(self, value):
        if 0 < value < 30:
            self._serial.write(
                'OVP1 {:.2f}\n'.format(value).encode('ascii')
            )
            self._serial.write(b'*OPC?\n')
            self._serial.readline()
        else:
            raise ValueError('Given value {0} is not in required range (0, 30)V.'.format(value))

    @property
    def cur_limit(self):
        self._serial.write(b'I1?\n')
        return int(self._serial.readline()[:-2].split(' ')[2])

    @cur_limit.setter
    def cur_limit(self, value):
        if 0 < value < 3:
            self._serial.write(
                'I1 {:.3f}\n'.format(value).encode('ascii')
            )
            self._serial.write(b'*OPC?\n')
            self._serial.readline()
        else:
            raise ValueError('Given value {0} is not in required range (0, 3)A.'.format(value))

    @property
    def output(self):
        self._serial.write(b'OP1?\n')
        return int(self._serial.readline()[:-2])

    @output.setter
    def output(self, value):
        self._serial.write(
            'OPv1 {:d}\n'.format(1 if value else 0).encode('ascii')
        )
        self._serial.write(b'*OPC?\n')
        self._serial.readline()

    @property
    def voltage(self):
        self._serial.write(b'OP1?\n')
        return int(self._serial.readline()[:-2])

    @voltage.setter
    def voltage(self, value):
        if 0 < value < 30:
            self._serial.write(
                'V1 {:.2f}\n'.format(value).encode('ascii')
            )
            self._serial.write(b'*OPC?\n')
            self._serial.readline()
        else:
            raise ValueError('Given value {0} is not in required range (0, 30)V.'.format(value))
