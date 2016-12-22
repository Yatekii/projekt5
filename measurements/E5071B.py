import usbtmc
import numpy as np


from device import Device


class E5071B(Device):

    device_name = 'E5071B'

    def __init__(self, device_id, serial_no=None):
        super().__init__()
        self._instr = usbtmc.Instrument(*device_id)
        self._instr.timeout = 60 * 1000
        device = self._instr.ask("*IDN?").split(',')
        self._vna_manufacturer, self._model_nr, self._serial_no, self._version = device

        self.valid = True
        if serial_no:
            print(self._model_nr, self._serial_no)
            self.valid = self._model_nr == self.device_name and self._serial_no == serial_no

    def close(self):
        self._instr.close()

    @property
    def frequency_range(self):
        return (
            int(self._instr.ask(':SENS1:FREQ:STAR?')),
            int(self._instr.ask(':SENS1:FREQ:STOP?'))
        )

    @frequency_range.setter
    def frequency_range(self, value):
        r = (3e5, 8.5e9)
        if r[0] <= value[0] < value[1] <= r[1]:
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
    def sweep_points(self):
        return int(self._instr.ask(':SENS1:SWE:POIN?'))

    @sweep_points.setter
    def sweep_points(self, value):
        self._instr.write(':SENS1:SWE:POIN {0}'.format(value))

    @property
    def sweep_bandwidth(self):
        return int(self._instr.ask(':SENS1:BAND?'))

    @sweep_bandwidth.setter
    def sweep_bandwidth(self, value):
        self._instr.write(':SENS1:BAND {0}'.format(value))

    @property
    def display_format(self):
        return self._instr.ask(':CALC1:FORM?')

    @display_format.setter
    def display_format(self, value):
        if value in ['MLIN', 'MLOG', 'SMIT']:
            self._instr.write(':CALC1:FORM {0}'.format(value))
        else:
            raise ValueError('{0} is not a valid format.'.format(value))

    @property
    def current_data(self):
        data = self._instr.ask(':CALC1:DATA:SDAT?').split(',')
        realpart = list(map(float, data[::2]))
        imagpart = list(map(float, data[1::2]))
        data = np.vectorize(complex)(realpart, imagpart)
        return data

    @property
    def calibration_method(self):
        return self._instr.ask(':SENS1:CORR:COLL:METH:TYPE?')

    @calibration_method.setter
    def calibration_method(self, value):
        if value[0] in ['OPEN', 'SHOR', 'THRU', 'ERES', 'SOLT1', 'SOLT2']:
            self._instr.write(':SENS1:CORR:COLL:METH:{0} {1}'.format(*value))
            self._instr.ask('*OPC?')
        else:
            raise ValueError('{0} is not a valid method.'.format(value[0]))

    def calibrate(self, method, port=None):
        if method in ['OPEN', 'SHORT', 'LOAD'] and self.mode == 'S11':
            self._instr.write(':SENS1:CORR:COLL:{0} {1}'.format(method, port))
            self._instr.ask('*OPC?')
        elif method == 'THRU' and self.mode == 'S21':
            self._instr.write(':SENS1:CORR:COLL:METH:THRU 1,2')
            self._instr.write(':SENS1:CORR:COLL:THRU 1,2')
            self._instr.ask('*OPC?')
        else:
            raise ValueError('{0} is not a valid method.'.format(method))

    @property
    def continuous_measurement(self):
        return False if self._instr.write(':INIT1:CONT?') == 'OFF' else True

    @continuous_measurement.setter
    def continuous_measurement(self, value):
        self._instr.write(':INIT1:CONT {0}'.format('ON' if value else 'OFF'))

    @property
    def measurement_trigger(self):
        return self._instr.write(':TRIG:SOUR?')

    @measurement_trigger.setter
    def measurement_trigger(self, value):
        if value in ['INT', 'EXT', 'MAN', 'BUS']:
            self._instr.write(':TRIG:SOUR {0}'.format(value))
        else:
            raise ValueError('{0} is not a valid source.'.format(value))

    @property
    def output_power(self):
        pass
        # return self._instr.ask(':SOUR1:POW?')

    @output_power.setter
    def output_power(self, value):
        self._instr.write(':SOUR1:POW {0:.2f}'.format(value))

    def activate_calibration(self):
        self._instr.write(':SENS1:CORR:COLL:SAVE')

    def store_calibration(self, filename):
        self._instr.write(':MMEM:STOR \"{0}\"'.format(filename))

    def load_calibration(self, filename):
        self._instr.write(':MMEM:LOAD \"{0}\"'.format(filename))

    def create_directory(self, name):
        self._instr.write(':MMEM:MDIR \"{0}\"'.format(name))

    def single_measurement(self):
        # self._instr.write(':DISP:WIND1:ACT')
        # self._instr.write(':CALC1:PAR1:SEL')
        self.continuous_measurement = True
        self.measurement_trigger = 'BUS'
        self._instr.write(':TRIG:SING')
        self._instr.ask('*OPC?')
        return self.current_data
