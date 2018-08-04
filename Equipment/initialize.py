import visa
from equipment import *


#def initialize():
if __name__ ==  "__main__":
    rm = visa.ResourceManager()
    racks = rm.list_resources()
    #toollist = [Equipment(rack, rm) for rack in racks if rack[0:3] in 'GPIB']]
    listGPIB = []
    listEquip = []
    for rack in racks:
        
        if 'GPIB' in rack:
            listGPIB.append(rack)
            
            tool = rm.open_resource(rack)
            toolID = tool.query("*IDN?")
            print(toolID)
            #listEquip = listEquip.append(initEquip(tool, rack, toolID))

    


def initEquip(tool, address, toolID):
    if 'keithley' in toolID.lower():
        if '2400' in toolID.lower():
            return ke2400(address, toolID, tool)
        elif '2450' in toolID.lower():
            return ke2450(address, toolID, tool)
        else:
            return Equipment(address, toolID, tool)
    elif 'stanford' in toolID.lower():
        if 'sr830' in toolID.lower():
            return sr830(address, toolID, tool)
        else:
            return Equipment(address, toolID, tool)
    else:
        return Equipment(address, toolID, tool)
            
