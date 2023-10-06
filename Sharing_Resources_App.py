import threading
import time
import queue
from Resources import Sensor, Actuator, CommunicationChannel

def sensor_data_generator(sensor):
    while True:
        data = f"{sensor.name} - Data at {time.time()}"
        sensor.write_data(data)
        time.sleep(1)

def actuator_controller(actuator):
    while True:
        status = f"Status updated at {time.time()}"
        actuator.set_status(status)
        time.sleep(2)

def communication_handler(channel):
    while True:
        message = f"Message received at {time.time()}"
        channel.send_message(message)
        time.sleep(3)

if __name__ == "__main__":
    # Create shared resources
    ir_sensor = Sensor("IR Sensor")
    lidar_sensor = Sensor("Lidar Sensor")
    motor_actuator = Actuator("Motor Actuator")
    communication_channel = CommunicationChannel()

    # Create threads for resource management
    sensor_thread1 = threading.Thread(target=sensor_data_generator, args=(ir_sensor,))
    sensor_thread2 = threading.Thread(target=sensor_data_generator, args=(lidar_sensor,))
    actuator_thread = threading.Thread(target=actuator_controller, args=(motor_actuator,))
    communication_thread = threading.Thread(target=communication_handler, args=(communication_channel,))

    # Start resource management threads
    sensor_thread1.start()
    sensor_thread2.start()
    actuator_thread.start()
    communication_thread.start()

    # Main robot control loop
    while True:
        ir_data = ir_sensor.read_data()
        lidar_data = lidar_sensor.read_data()
        actuator_status = motor_actuator.get_status()
        message = communication_channel.receive_message()

        # Perform robot control actions based on the shared resources
        print(f"IR Sensor Data: {ir_data}")
        print(f"Lidar Sensor Data: {lidar_data}")
        print(f"Motor Actuator Status: {actuator_status}")
        print(f"Communication Channel Message: {message}")

        time.sleep(1)
