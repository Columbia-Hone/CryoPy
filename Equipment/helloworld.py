import visa
import equipment

rm = visa.ResourceManager()
racks = rm.list_resources()
print(racks)
toollist = [Equipment(rack, rm) for rack in racks if rack[0:3] in 'GPIB']
print(toollist.getID)
