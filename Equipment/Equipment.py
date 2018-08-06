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
class SRlockin(Meter):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)

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
    def readV(self):
        self.nowV = self.io.query_ascii_values(":READ?")[0]
        return float(self.nowV)
    def readI(self):
        self.nowI = self.io.query_ascii_values(":READ?")[1]
        return float(self.nowI)
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
    #Need troubleshooting exceptions with output, compliance, etc.s

def initEquip(tool, address, toolID):
    if 'keithley' in toolID.lower():
        
        if '2400' in toolID.lower():
            return KE2400(address, toolID, tool)
# """         elif '2450' in toolID.lower():
#             return KE2450(address, toolID, tool) """
        else:
                return Equipment(address, toolID, tool)
    # """ elif 'stanford' in toolID.lower():
    #     if 'sr830' in toolID.lower():
    #         return SR830(address, toolID, tool)
    #     else:
    #         return Equipment(address, toolID, tool)
    # elif 'yokogawa' in toolID.lower():
    #     if 'gs200' in toolID.lower():
    #         return Yokogs200(address, toolID, tool)
    #     else:
    #         return Equipment(address, toolID, tool) """
    else:
        return Equipment(address, toolID, tool) 