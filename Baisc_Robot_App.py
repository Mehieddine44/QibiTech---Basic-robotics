import threading
import time
from Robot import Robot

class RobotWithIR(Robot):
    def process_infrared_data(self, data):
        with self.camera_lock:
            # Simulate infrared data processing
            print(f"{self.name} processing infrared data:", data)

def camera_sensor_emulator(robot):
    while True:
        # Simulate camera data acquisition
        camera_data = f"{robot.name} - Camera data snapshot"
        robot.process_camera_data(camera_data)
        time.sleep(1)

def infrared_sensor_emulator(robot):
    while True:
        # Simulate infrared data acquisition
        infrared_data = f"{robot.name} - Infrared data snapshot"
        robot.process_infrared_data(infrared_data)
        time.sleep(1.5)

if __name__ == "__main__":
    # Create a robot with IR sensor
    robot_with_ir = RobotWithIR("Robot1")

    # Create threads for sensor emulators
    camera_thread = threading.Thread(target=camera_sensor_emulator, args=(robot_with_ir,))
    infrared_thread = threading.Thread(target=infrared_sensor_emulator, args=(robot_with_ir,))

    # Start the sensor threads
    camera_thread.start()
    infrared_thread.start()

    # Main robot control loop
    while True:
        with robot_with_ir.camera_lock:
            camera_data = robot_with_ir.camera_data
        print(f"{robot_with_ir.name} making decisions based on camera data:", camera_data)

        # Perform robot control actions here

        time.sleep(1)