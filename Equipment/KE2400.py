import visa

class KE2400(Keithley):
    def __init__(self, address, id, io, compliance = 1e-6):
        super().__init__(address, id, io)
        self.compliance = compliance
        self.io.write('SENS:CURR:PROT ' + self.compliance)
        self.io.write(':SOURce1:CLEar:AUTO OFF')
    def setV(self, Vstart, Vend, increment, delay):
        pass
    def readV(self):
        pass
    def readI(self):
        pass
    #Need troubleshooting exceptions with output, compliance, etc.s