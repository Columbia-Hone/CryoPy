import visa
from equipment import Equipment

rm = visa.ResourceManager()
racks = rm.list_resources()
#toollist = [Equipment(rack, rm) for rack in racks if rack[0:3] in 'GPIB']
GPIBlist = [rack for rack in racks if  rack[0:3] in 'GPIB']
print(GPIBlist)