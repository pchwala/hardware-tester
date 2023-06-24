import threading
import pyaudio


# RecordAndPlayback class works in separate thread
# Passing arguments through queue, args using queue.put('data')
# passing: 0 - stop playback, still recording
#          1 - start record and playback
#          2 - clean up and terminate thread
class RecordSound(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_data = args

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100

        self.p = pyaudio.PyAudio()

        self.long_data = []
        self.TIME = 20

        # init stream class
        try:
            self.stream = self.p.open(format=self.FORMAT,
                                      channels=self.CHANNELS,
                                      rate=self.RATE,
                                      output=True,
                                      input=True,
                                      stream_callback=self.callback,
                                      frames_per_buffer=self.CHUNK)
        except Exception:
            print("cos sie zjebalo xD")

    # define audio io callback
    # This gets called with a block of incoming mic samples,
    # and returns a block of outgoing speaker samples.
    def callback(self, in_data, frame_count, time_info, status):
        self.long_data.insert(0, in_data)
        if len(self.long_data) > self.TIME:
            temp_data = self.long_data[self.TIME]
            self.long_data.pop()
            return temp_data, pyaudio.paContinue
        else:
            return in_data, pyaudio.paContinue

    # function called when starting thread
    def run(self):
        # print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # receive arguments in a loop until None is received
        while True:
            val = self.queue.get()
            if val is None:
                return
            self.transmit_sound(val)

    def transmit_sound(self, data):
        print("Recording sound:")

        if data == 'stop':
            print("stopped")
            self.stream.stop_stream()

        elif data == 'start':
            print("started")
            self.stream.start_stream()

        elif data == 'terminate':
            print("terminating")
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
