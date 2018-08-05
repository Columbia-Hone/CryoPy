import visa

class KE2400(Keithley):
    def __init__(self, address, id, io):
        super().__init__(address, id, io)
    def setV(self, Vstart, Vend, increment, delay):
        pass
    def readV(self):
        pass
    def readI(self):
        pass
    #Need troubleshooting exceptions with output, compliance, etc.s