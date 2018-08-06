import visa
import time
import numpy as np

class Equipment:
    
    def __init__(self, address, id, io):
        self.io = io
        self.address = address
        self.id = id
    
    def __str__(self):
        return str(self.id)
    def __float__(self):
        return 0.0
        

class Source(Equipment):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)

class Meter(Equipment):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)
class Keithley(Source, Meter):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)
class SR830(Source, Meter):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)
        self.rangelist = np.array([2e-9, 5e-9, 10e-9, 20e-9,\
        5e-8, 1e-7, 2e-7, 5e-7, 1e-6, 2e-6, 5e-6, 1e-5, 2e-5, 5e-5, 1e-4,
        2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2, 1e-1, 2e-1, 5e-1, 1.0])
    def read(self, chA=10, chB = 11, chC = 1, chD =4):
        # 1:X,2:Y, 3:R, 4:Theta, 5:AuxIn1, 6:AuxIn2, 7:AuxIn3, 8:AuxIn4
        # 9:Freq, 10:CH1, 11:CH2
        
        # X, Y are read at same time, R, Theta read at same time.
        # 10 us delay between the two pairs
        return self.io.query_ascii_values("SNAP? %i,%i,%i,%i" % (chA,chB,chC,chD))
    def setRange(self, range = 15):
        # Sets the sensitivity
        # 0:2nV/fA, 1:5nV/fA, 2:10nV/fA, 3:20nV/fA, 4:50nV/fA, 5:100nV/fA, 6:200nV/fA
        # 7:500nV/fA, 8:1uV/pA, 9:2uV/pA, 10:5uV/pA, 11:10uV/pA, 12:20uV/pA, 13:50uV/pA
        # 14:100uV/pA, 15:200uV/pA, 16:500uV/pA, 17:1mV/nA, 18:2mV/nA, 19:5mV/nA
        # 20:10mV/nA, 21:20mV/nA, 22:50mV/nA, 23:100mV/nA, 24:200mV/nA, 25:500mV/nA
        # 26: 1V/uA
        self.io.write("SENS " + str(range))
    def autoRange(self):
        curVal = self.read()[0]
        
        curRange = self.io.query_ascii_values("SENS ?")

    def setSF(self, sf):
        # sets sample frequency, which should be always at least 2x your  signal frequency
        self.io.write("SRAT " + str(sf))
    def setV(self, ampl):
        self.io.write("SLVL " + str(ampl))
    def readV(self):
        return self.io.query("SLVL ?")
    def rampV(self, startV, endV, increment=0.005, delay=.1, increment2 = .1, delay2 = .1):
        
        nowV = float(self.readV())
        if nowV  > startV :
            increment2*=-1
        if startV > endV:
            increment*=-1
        for val in np.arange(nowV,startV+increment2,increment2):
            self.setV(val)
            time.sleep(delay2)
        for val in np.arange(startV, endV+increment, increment):
            self.setV(val)
            time.sleep(delay)
        return float(self.readV())

class KE2400(Keithley):
    def __init__(self, address, id, io, compliance = 2e-6, vlimit = 'MAX'):
        super().__init__(address, id, io)
        self.compliance = compliance
        self.vlimit = vlimit
        print(self.compliance)
        self.io.write('SENS:CURR:PROT ' + str(self.compliance))
        self.io.write(':SOURce1:CLEar:AUTO OFF')
        self.io.write('SOUR:VOLT:RANG ' + self.vlimit)
        self.io.write(":SOUR:VOLT:MODE FIX")
    def setV(self, setV):
        self.io.write(":SOUR:VOLT " + str(setV))
    def readAll(self):
        return self.io.query_ascii_values(":READ?")
    def readV(self):

        return self.io.query_ascii_values(":READ?")[0]
    def readI(self):       
        return  self.io.query_ascii_values(":READ?")[1]
    def rampV(self, startV, endV, increment=0.005, delay=.1, increment2 = .1, delay2 = .1):
        
        nowV = float(self.readV())
        if nowV  > startV :
            increment2*=-1
        if startV > endV:
            increment*=-1
        for val in np.arange(nowV,startV+increment2,increment2):
            self.setV(val)
            time.sleep(delay2)
        for val in np.arange(startV, endV+increment, increment):
            self.setV(val)
            time.sleep(delay)
        return float(self.readV())
    #Need troubleshooting exceptions with output, compliance, etc.s

def initEquip(tool, address, toolID):
    if 'keithley' in toolID.lower():
        
        if '2400' in toolID.lower():
            return KE2400(address, toolID, tool)
# """         elif '2450' in toolID.lower():
#             return KE2450(address, toolID, tool) """
        else:
                return Equipment(address, toolID, tool)
    elif 'stanford' in toolID.lower():
        if 'sr830' in toolID.lower():
            return SR830(address, toolID, tool)
        else:
            return Equipment(address, toolID, tool)
    # elif 'yokogawa' in toolID.lower():
    #     if 'gs200' in toolID.lower():
    #         return Yokogs200(address, toolID, tool)
    #     else:
    #         return Equipment(address, toolID, tool) """
    else:
        return Equipment(address, toolID, tool) 