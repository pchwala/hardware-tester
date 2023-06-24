import threading

import customtkinter
import cv2 as cv
import numpy as np

from PIL import Image


class CameraCapture(threading.Thread):
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

        self.capture = cv.VideoCapture(0)
        if self.capture.isOpened() is False:
            print("Cannot open camera")
            self.output_queue.put('missing_camera')

        # function called when starting thread
    def run(self):
        # print name and received arguments
        print(threading.current_thread().name, self.receive_data)
        # receive arguments in a loop until None is received
        while True:
            val = self.input_queue.get()
            print("Camera checking")
            if val is None:
                return

            if val == 'stop':
                print("stopped")
                self.capture.release()

            if val == 'start':
                print("started")
                self.capture = cv.VideoCapture(0)
                if self.capture.isOpened() is False:
                    print("Cannot open camera")
                    self.output_queue.put('missing_camera')

                while True:
                    # Capture frame-by-frame
                    returned, frame = self.capture.read()
                    # if frame is read correctly returned is True
                    if returned is False:
                        print("Can't receive frame (stream end?).")
                        self.output_queue.put('failed_capture')
                        break

                    # Get the latest frame and convert into Image and put into output queue
                    returned, frame = self.capture.read()
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                    image_frame = Image.fromarray(frame)

                    image_ctk = customtkinter.CTkImage(None, dark_image=image_frame, size=(512, 512))
                    self.output_queue.put(image_ctk)

                    if self.input_queue.empty() is False:
                        break

            if val == 'terminate':
                print("terminating")
