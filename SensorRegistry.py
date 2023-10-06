class SensorRegistry:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, name, sensor):
        if name not in self.sensors:
            self.sensors[name] = sensor
        else:
            raise ValueError(f"Sensor with name '{name}' already exists in the registry.")

    def get_sensor(self, name):
        if name in self.sensors:
            return self.sensors[name]
        else:
            raise KeyError(f"Sensor with name '{name}' not found in the registry.")

    def list_sensors(self):
        return list(self.sensors.keys())

class Sensor:
    def __init__(self, name):
        self.name = name
