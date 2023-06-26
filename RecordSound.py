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

        # init input stream
        try:
            self.input_stream = self.p.open(format=self.FORMAT,
                                            channels=self.CHANNELS,
                                            rate=self.RATE,
                                            input=True,
                                            stream_callback=self.input_callback,
                                            frames_per_buffer=self.CHUNK)
        except Exception:
            print("Micro fucked up")

        # init output stream
        try:
            self.output_stream = self.p.open(format=self.FORMAT,
                                             channels=self.CHANNELS,
                                             rate=self.RATE,
                                             output=True,
                                             stream_callback=self.output_callback,
                                             frames_per_buffer=self.CHUNK)
        except Exception:
            print("Speakers fucked up")

    # define audio input callback
    # This gets called with a block of incoming mic samples,
    def input_callback(self, in_data, frame_count, time_info, status):
        self.long_data.insert(0, in_data)
        return (None, pyaudio.paContinue)

    def output_callback(self, in_data, frame_count, time_info, status):
        try:
            data = self.long_data.pop()
            return (data, pyaudio.paContinue)
        except IndexError:
            return (None, pyaudio.paContinue)

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
            self.input_stream.stop_stream()
            self.output_stream.start_stream()

        elif data == 'start':
            print("started")
            self.output_stream.stop_stream()
            self.input_stream.start_stream()

        elif data == 'terminate':
            print("terminating")
            self.input_stream.stop_stream()
            self.output_stream.stop_stream()
            self.input_stream.close()
            self.output_stream.close()
            self.p.terminate()
