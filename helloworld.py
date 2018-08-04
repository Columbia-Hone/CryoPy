import visa

rm = visa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('GPIB0::23::INSTR')
print(inst.query("*IDN?"))