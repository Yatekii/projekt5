import usbtmc
import numpy as np


from device import Device


class E5071B(Device):
    def __init__(self, device_id, serial_nr=None):
        self._instr = usbtmc.Instrument(*device_id)
        device = self._instr.ask("*IDN?").split(',')
        self._vna_manufacturer, self._model_nr, self._serial_nr, self._version = device

        self.valid = True
        if serial_nr:
            self._serial_nr = self._serial_nr == serial_nr

    @property
    def frequency_range(self):
        return (
            int(self._instr.ask(':SENS1:FREQ:STAR?')),
            int(self._instr.ask(':SENS1:FREQ:STOP?'))
        )

    @frequency_range.setter
    def frequency_range(self, value):
        r = (3e5, 8.5e9)
        if r[0] < value[0] < value[1] < r[1]:
            self._instr.write(':SENS1:FREQ:STAR {0:.2E}'.format(value[0]))
            self._instr.write(':SENS1:FREQ:STOP {0:.2E}'.format(value[1]))
        else:
            raise ValueError('Given range {0}Hz is not in required range {1}Hz.'.format(value, r))

    @property
    def mode(self):
        return self._instr.ask(':CALC1:PAR1:DEF?')

    @mode.setter
    def mode(self, value):
        modes = ['S11', 'S21', 'S12', 'S22']
        if value in modes:
            self._instr.write(':CALC1:PAR1:DEF {0}'.format(value))
        else:
            raise ValueError('Unknown Mode {0}.'.format(value))

    @property
    def calibration_save_format(self):
        return self._instr.ask(':MMEM:STOR:STYP?')

    @calibration_save_format.setter
    def calibration_save_format(self, value):
        if value in ['STAT', 'CST', 'DST', 'CDST']:
            self._instr.write(':MMEM:STOR:STYP {0}'.format(value))
        else:
            raise ValueError('{0} is not a valid format.'.format(value))

    @property
    def display_format(self):
        return self._instr.ask(':CALC1:FORM?')

    @select_display_format.setter
    def display_format(self, value):
        if value in ['MLIN', 'MLOG', 'SMIT']:
            self._instr.write(':CALC1:FORM {0}'.format(value))
        else:
            raise ValueError('{0} is not a valid format.'.format(value))

    @property
    def current_data(self):
        data = instr.ask(':CALC1:DATA:SDAT?').split(',')
        data = [np.complex64(data[i], data[i+1]) for i in range(len(data) / 2)]
        return data

    def calibrate(self, method, port = None):
        if method in ['OPEN', 'SHORT', 'THRU'] and vna.mode == 'S11':
            self._instr.write(':SENS1:CORR:COLL:METH:SOLT1 {0}'.format(value))
            self._instr.write(':SENS1:CORR:COLL:{0} {1}'.format(method, ','.join(port)))
        elif method == 'THRU' and vna.mode == 'S21':
            self._instr.write(':SENS1:CORR:COLL:METH:THRU 1,2')
            self._instr.write(':SENS1:CORR:COLL:THRU 1,2')
        else:
            raise ValueError('{0} is not a valid method.'.format(value))

    def activate_calibration(self):
        self._instr.write(':SENS1:CORR:COLL:SAVE')

    def store_calibration(self, filename):
        self._instr.write(':MMEM:STOR ""{0}""'.format(filename))

    def load_calibration(self, filename):
        self._instr.write(':MMEM:LOAD ""{0}""'.format(filename))
