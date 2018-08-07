import visa
from equipment import KE2400, Equipment, initEquip
import time

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
    
    
    #print((listEquip[0].setSF(10)))
    listEquip[0].rampV(0, 0.00500, 0.001 ,0.5)

    t0 = time.time()
    for idx in range(0,100):
        (listEquip[0].autoRange())
    t1 = time.time()
    print(t1-t0)
    t0 = time.time()
    for idx in range(0,100):

        (listEquip[0].read())
    t1 = time.time()

    
    print(t1-t0)
    #print(str(listEquip[1].io.query(":SOUR:VOLT:MODE?")))
    #listEquip[1].setV(1)
    
    #print(listEquip[1].io.read("READ?"))