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

    @staticmethod
    def exec_and_output(command):
        return subprocess.check_output(command, shell=True).decode().strip()

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

            if val == 'start':
                print("started")
                while True:
                    # Ping 8.8.8.8 4 times
                    command = "ping 8.8.8.8 -c 4"

                    try:
                        # if ping doesn't return error then wifi works OK, this process completed its job
                        all_info = self.exec_and_output(command)
                        self.output_queue.put("wlan_ok")
                        self.input_queue.put("terminate")

                        # if it returns error the try again after 5 seconds
                    except subprocess.CalledProcessError:
                        time.sleep(5)

                    if self.input_queue.empty() is False:
                        break

            elif val == 'terminate':
                print("terminating")
