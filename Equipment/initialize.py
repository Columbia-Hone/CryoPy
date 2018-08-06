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

    print(listID[0])
    
    print((listEquip[0].io.query("SLVL ?")))
   
    print(listEquip[1].readV()+1)
  
    #print(str(listEquip[1].io.query(":SOUR:VOLT:MODE?")))
    listEquip[1].setV(1)
    listEquip[0].rampV(0, 0.000, 0.001 ,0.5)
    #print(listEquip[1].io.read("READ?"))