import threading
import time
import queue

class Sensor:
    def __init__(self, name):
        self.name = name
        self.data = None
        self.lock = threading.Lock()

    def read_data(self):
        with self.lock:
            return self.data

    def write_data(self, data):
        with self.lock:
            self.data = data

class Actuator:
    def __init__(self, name):
        self.name = name
        self.status = None
        self.lock = threading.Lock()

    def get_status(self):
        with self.lock:
            return self.status

    def set_status(self, status):
        with self.lock:
            self.status = status

class CommunicationChannel:
    def __init__(self):
        self.queue = queue.Queue()

    def send_message(self, message):
        self.queue.put(message)

    def receive_message(self):
        return self.queue.get()