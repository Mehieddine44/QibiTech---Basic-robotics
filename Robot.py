import threading
import time

class Robot:
    def __init__(self, name):
        self.name = name
        self.camera_data = None
        self.camera_lock = threading.Lock()

        self.sensors = {}
        self.sensor_locks = {}
        
        # Create locks for each sensor
        for sensor_name in ["IR Sensor", "Lidar Sensor", "Ultrasonic Sensor"]:
            self.sensors[sensor_name] = None
            self.sensor_locks[sensor_name] = threading.Lock()

    def attach_sensor(self, sensor_name, sensor):
        if sensor_name in self.sensors:
            self.sensors[sensor_name] = sensor
        else:
            raise ValueError(f"{sensor_name} is not a valid sensor for {self.name}.")  
         
    def process_sensor_data(self, sensor_name, data):
        if sensor_name in self.sensors:
            locks_to_acquire = sorted([self.sensor_locks[sensor_name], self.sensor_locks["IR Sensor"], 
                                                                        self.sensor_locks["Lidar Sensor"], 
                                                                        self.sensor_locks["Ultrasonic Sensor"]])
            # Account for deadlocks
            with locks_to_acquire[0]:
                with locks_to_acquire[1]:
                    with locks_to_acquire[2]:
                        with locks_to_acquire[3]:
                            sensor = self.sensors[sensor_name]
                            if sensor:
                                sensor.process_data(data)
                            else:
                                print(f"{self.name} does not have {sensor_name} attached.")
        else:
            raise ValueError(f"{sensor_name} is not a valid sensor for {self.name}.") 
               
    def process_camera_data(self, data):
        with self.camera_lock:
            # Simulate camera data processing
            print(f"{self.name} processing camera data:", data)
            self.camera_data = data

    def process_infrared_data(self, data):
        raise NotImplementedError("Infrared sensor function must be implemented in child class")

    def process_ultrasonic_data(self, data):
        raise NotImplementedError("Ultrasonic sensor function must be implemented in child class")

    def process_lidar_data(self, data):
        raise NotImplementedError("LIDAR sensor function must be implemented in child class")

    def process_force_torque_data(self, data):
        raise NotImplementedError("Force/Torque sensor function must be implemented in child class")
