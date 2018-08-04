import visa
import numpy as np
import time
rm = visa.ResourceManager()
rmlist = rm.list_resources()
print(rmlist)
keithley = rm.open_resource('GPIB0::23::INSTR')
print(keithley.query("*IDN?"))
#keithley.write(":OUTP ON")
keithley.write("SENS:CURR:PROT .0001")#setting compliance
startvolts = 0
endvolts = 10
currentvolts = float(startvolts)
increment = .005
delay = .01
for x in np.arange(startvolts,endvolts+increment,increment):
    voltingsource = ":SOUR:VOLT %f" % (currentvolts)
    currentvolts = float(currentvolts + increment)
    time.sleep(delay)
    keithley.write(voltingsource)
    #keithleyvalues = keithley.read()
    #keithley.write(":READ?")
    #print(keithleyvalues)
## Looping back
currentvolts = float(currentvolts - increment)
for x in np.arange(startvolts,endvolts+increment,increment):
    voltingsource = ":SOUR:VOLT %f" % (currentvolts)
    currentvolts = float(currentvolts - increment)
    time.sleep(delay)
    keithley.write(voltingsource)
    #keithleyvalues = keithley.read()
    #keithley.write(":READ?")
    #print(keithleyvalues)
#keithelyvalues = keithleyvalues[1:1]
#voltage = float(keithleyvalues[0:13])
#current = float(keithleyvalues[14:27])
#print(voltage)
#print(current)
