import re
import threading
import subprocess
import time


class ListRemovable(threading.Thread):
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

        self.removables = []

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
            print("Ports checking")
            if val is None:
                return

            if val == 'stop':
                print("stopped")

            if val == 'start':
                print("started")
                while True:
                    command = "lsblk | grep disk"
                    all_info = self.exec_and_output(command)

                    disks = re.findall(r'\d+,', all_info)
                    output_info = "Devices:\n\n"
                    x = 0
                    for disk in disks:
                        disks[x] = "-  " + re.sub(r',', " GB Volume", disk) + "\n"
                        output_info += disks[x] + "\n"
                        x += 1

                    self.output_queue.put(output_info)
                    time.sleep(0.5)

                    if self.input_queue.empty() is False:
                        break
