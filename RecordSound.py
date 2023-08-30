import threading
import subprocess
import time


def exec_and_output(self, command):
    return subprocess.check_output(command, shell=True).decode().strip()


class RecordSound(threading.Thread):
    """
    RecordAndPlayback class works in separate thread
    Passing arguments through queue, args using queue.put('data')
    passing: 0 - stop playback, still recording
             1 - start record and playback
             2 - clean up and terminate thread
    """

    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_data = args

        self.record_proc = None
        self.played = False

    # Function called when starting thread
    def run(self):
        # print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # Receive arguments in a loop until None is received
        while True:
            val = self.queue.get()
            if val is None:
                return
            self.transmit_sound(val)

    def transmit_sound(self, data):
        print("Recording sound:")

        if data == 'stop':
            try:
                self.record_proc.terminate()
                self.record_proc.wait()
                if self.played is False:
                    playback_proc = subprocess.Popen(['aplay', 'test-mic.wav'])
                    self.played = True
                else:
                    return
                playback_proc.wait()
            except:
                pass

        elif data == 'start':
            self.played = False
            self.record_proc = subprocess.Popen(['arecord', '-f', 'cd', '-d', '4', 'test-mic.wav'])
            print("xd")

        elif data == 'terminate':
            try:
                self.record_proc.terminate()
                self.record_proc.wait()
            except:
                pass
