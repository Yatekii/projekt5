# Setup
import usbtmc
instr = usbtmc.Instrument(2391, 1289)
print(instr.ask("*IDN?"))
# Agilent Technologies,E5071B,MY42404018,A.09.10

# Set marker on/off
instr.write(":CALC1:MARK1 OFF")
# get formatted data
print(instr.ask(":CALC1:DATA:FDAT?"))
# get raw data
print(instr.ask(":CALC1:DATA:SDAT?"))
# set formatting
instr.write(":CALC1:FORM SMIT")

# setup measurement
instr.write(":CALC1:PAR1:DEF S21")
instr.write(":SENS1:FREQ:STAR 100E6")
instr.write(":SENS1:FREQ:STOP 100E6")

# enable storing calibration
instr.write(":MMEM:STOR:STYP CDST")
instr.write(":MMEM:STOR ""Test1/State01.sta""")
instr.write(":MMEM:LOAD ""Test1/State01.sta""")

# calibrate through
instr.write(":SENS1:CORR:COLL:METH:THRU 1,2")
instr.write(":SENS1:CORR:COLL:THRU 2,1")
instr.write(":SENS1:CORR:COLL:SAVE")

# calibrate reflection
instr.write(":SENS1:CORR:COLL:METH:SOLT1 1")
instr.write(":SENS1:CORR:COLL:OPEN")
instr.write(":SENS1:CORR:COLL:SHORT")
instr.write(":SENS1:CORR:COLL:LOAD")
instr.write(":SENS1:CORR:COLL:SAVE")
