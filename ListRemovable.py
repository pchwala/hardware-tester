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

    def exec_and_output(self, command):
        return subprocess.check_output(command, shell=True).decode().strip()

    # function called when starting thread
    def run(self):
        # print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # receive arguments in a loop until None is received
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
                    """
                    command = "sudo fdisk -l"
                    all_info = self.exec_and_output(command)
                    disks = re.findall(r'Disk /[a-z/: ]*\d+', all_info)
                    for disk in disks:
                        temp = int(re.search(r'\d+', disk).group(0))
                        if temp < 100:
                            print(disk + 'G')
                            self.output_queue.put(disk)
                    """

                    command = "lsblk"
                    all_info = self.exec_and_output(command)
                    self.output_queue.put(all_info)
                    time.sleep(1)

                    if self.input_queue.empty() is False:
                        break
