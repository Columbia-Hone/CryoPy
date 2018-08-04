import visa
import ke2400

class Equipment:
    
    def __init__(self, address, id, io):
        self.io = io
        self.address = address
        self.id = id

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
    def __init__(self, address, id, io):
        super().__init__(address, id, io)
    def setV(self, Vstart, Vend, increment, delay):
        pass
    def readV(self):
        pass
    def readI(self):
        pass
    #Need troubleshooting exceptions with output, compliance, etc.s