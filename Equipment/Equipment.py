import visa


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