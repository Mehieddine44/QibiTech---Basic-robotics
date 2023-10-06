# QibiTech---Basic-robotics
This repository contains a set of scripts simulating a skelaton for some basic applications in robotics.
I simulated some elements such as robots, sensors, and resources as OOP entities. I also included 
some code to acount for some issues related to thread safety such as data races, deadlocks, and resource contention.

(PS: ChatGPT was relied upon in some parts of scripting)

## Robot.py 
This script defines the parent Class of robots. It simulates a robot with a set of defaults sensors such as camera, IR, Lidar, and Ultra Sonic.
It allows for introducing new sensors with the method `attach_sensor()`. I implemented the function for processing camera data `process_camera_data()`
assuming that all robots in this class would have this function and left a bunch of other sensor processing functions as abstract methods. 
This class also has the `process_sensor_data()` which is supposed to represent a method for processing sensor data in general allowing more 
flexibility, it also provides code that acquires sensor locks in a predetermined order to avoid potential deadlocks.

## Baisc_Robot_App.py
This is supposed to represent a basic application of a robot with an IR. I implement the class `RobotWithIR()` which is a child class of 
the Robot class. The main robot control loop is acquiring a lock `(robot_with_ir.camera_lock)` before accessing and printing the camera data. This is done to prevent potential data races.

## SensorRegistry.py 
Provides a registry for sensors allowing the possibility for taking advantage of the flexibility and simplicity offered by registries in case the 
application grows too complex.

## Multi_Sensor_App.py
Depicts the basic use of the registery of sensors.

## Resources.py and Sharing_Resources_App.py
Offer a bunch of different classes represnting different resources and their use in a basic application which accounts for safe resource sharing.
the code uses threads, proper synchronization mechanisms, consistent data access patterns, and isolated resource management functions to enable safe sharing of resources in a concurrent environment.
