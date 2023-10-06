from Robot import Robot
from SensorRegistry import SensorRegistry, Sensor


if __name__ == "__main__":
    # Create a sensor registry
    sensor_registry = SensorRegistry()

    # Create sensors and add them to the registry
    sensor1 = Sensor("IR Sensor")
    sensor2 = Sensor("Lidar Sensor")
    sensor3 = Sensor("Ultrasonic Sensor")

    sensor_registry.add_sensor("Sensor1", sensor1)
    sensor_registry.add_sensor("Sensor2", sensor2)
    sensor_registry.add_sensor("Sensor3", sensor3)

    # Create robots and associate sensors with them
    robot1 = Robot("Robot1")
    robot1_sensors = [sensor_registry.get_sensor("Sensor1"), sensor_registry.get_sensor("Sensor2")]
    robot1.sensors = robot1_sensors

    robot2 = Robot("Robot2")
    robot2_sensors = [sensor_registry.get_sensor("Sensor3")]
    robot2.sensors = robot2_sensors

    # Print the sensors associated with each robot
    print(f"{robot1.name} sensors: {[sensor.name for sensor in robot1.sensors]}")
    print(f"{robot2.name} sensors: {[sensor.name for sensor in robot2.sensors]}")

    # Accessing a sensor's data
    sensor1_data = "IR Sensor Data"
    robot1.sensors[0].data = sensor1_data

    # Retrieving data from a sensor
    retrieved_data = robot1.sensors[0].data
    print(f"Retrieved data from {robot1.name}'s IR Sensor: {retrieved_data}")
