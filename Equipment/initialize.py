import visa
from equipment import KE2400, Equipment, initEquip


#def initialize():
if __name__ ==  "__main__":
    rm = visa.ResourceManager()
    racks = rm.list_resources()
    #toollist = [Equipment(rack, rm) for rack in racks if rack[0:3] in 'GPIB']]
    listGPIB = []
    listEquip = [] 
    listID = []
    for rack in racks:
        
        if 'GPIB' in rack:
            listGPIB.append(rack)
            
            tool = rm.open_resource(rack)
            toolID = tool.query("*IDN?")
            listID.append(toolID)
            print(toolID)
            listEquip.append(initEquip(tool, rack, toolID))

    print(listID)
    print((listEquip[1].io.query_ascii_values(":READ?")[0]))
    print(listEquip[1].readV())
    print(listEquip[1].nowV)
    #print(str(listEquip[1].io.query(":SOUR:VOLT:MODE?")))
    listEquip[1].setV(12)
    listEquip[1].rampV(0.1, -0.1, 0.005 ,0.5)
    #print(listEquip[1].io.read("READ?"))