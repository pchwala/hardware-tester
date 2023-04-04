import re
import threading
import subprocess
import time


class WirelessCheck(threading.Thread):
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

    def run(self):
        """
        Function called when starting thread

        :return: None
        """
        # Print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # Receive arguments in a loop until None is received
        while True:
            val = self.input_queue.get()
            print("Wireless checking")
            if val is None:
                return

            if val == 'stop':
                print("stopped")

            if val == 'start':
                print("started")
                while True:
                    command = "ping 8.8.8.8"

                    all_info = self.exec_and_output(command)

                    if self.input_queue.empty() is False:
                        break