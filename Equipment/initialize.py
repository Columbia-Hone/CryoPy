import visa
from equipment import KE2400, Equipment, initEquip


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
            listEquip.append(initEquip(tool, rack, toolID))

    print(listEquip)


            
