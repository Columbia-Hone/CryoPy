import visa

class Equipment:
    
    def __init__(self, address,resource_manager):
        self = resource_manager.open_resource(address)
        self.address = address
        self.id = self.query("*IDN?")
    
    def getID(self):
        return self.id

class Source(Equipment):
    pass

class Meter(Equipment):
    pass
