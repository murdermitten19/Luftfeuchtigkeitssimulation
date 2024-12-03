class Sensor:
    def __init__(self, ID):
        self.ID = ID
    
class Thermometer(Sensor):
    def __init__(self, ID, temperature):
        super().__init__(ID)
        self.temperature = temperature
        
class Hygrometer(Sensor):
    def __init__(self, ID, humidity):
        super().__init__(ID)
        self.humidity = humidity



    