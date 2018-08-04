import visa
import Equipment

rm = visa.ResourceManager()
print(rm.list_resources(1))
inst = rm.open_resource('GPIB0::8::INSTR')
print(inst.query("*IDN?"))