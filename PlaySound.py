import threading
import pyaudio
import wave


# PlaySound class works in separate thread
# Passing arguments through queue, args using queue.put('data')
# passing: 0 - stop playing sound
#          1 - start playing sound
#          2 - clean up and terminate thread
class PlaySound(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.receive_data = args

        self.FILENAME = './speaker_test.wav'
        self.CHUNK = 1024
        # open sound file
        self.wf = wave.open(self.FILENAME, 'rb')
        self.p = pyaudio.PyAudio()

        # init stream class
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                  channels=self.wf.getnchannels(),
                                  rate=self.wf.getframerate(),
                                  output=True,
                                  stream_callback=self.callback)

    # reading data from *.wav sequencially in chunks
    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        return data, pyaudio.paContinue

    # function called when starting thread
    def run(self):
        # print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # receive arguments in a loop until None is received
        while True:
            val = self.queue.get()
            if val is None:
                return
            self.play_sound(val)

    # starting and stopping playing sound
    def play_sound(self, data):
        print("Playing sound:")

        if data == 'stop':
            print("stopped")
            self.stream.stop_stream()
            # reset, so next time the function is called, sound is played from the beginning
            self.wf = wave.open(self.FILENAME, 'rb')

        elif data == 'start':
            print("started")
            self.stream.start_stream()

        elif data == 'terminate':
            print("terminating")
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()
            self.p.terminate()
