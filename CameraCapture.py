import threading
import re

import customtkinter
import cv2 as cv

from PIL import Image


class CameraCapture(threading.Thread):
    """
    Thread for capturing video from camera using openCV

    'input_queue' for controlling thread behavior
    output from camera is converted to 'Image' gets put into 'output_queue'
    """
    def __init__(self, input_queue, output_queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.daemon = True
        self.receive_data = args

        self.camera_number = 0

        self.camera_width_scale = 1
        self.camera_height_scale = 1

        # Initialize camera capture
        self.capture = cv.VideoCapture(self.camera_number)
        if self.capture.isOpened() is False:
            print("Cannot open camera")
            self.output_queue.put('missing_camera')

    # Function called when starting thread
    def run(self):
        # Print name and received arguments
        print(threading.current_thread().name, self.receive_data)

        # Receive arguments in a loop until None is received
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
                # Initialize capture
                self.capture = cv.VideoCapture(self.camera_number)
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

                    # Get the latest frame and convert Image
                    # Also convert to RGB, so the color scheme is correct
                    returned, frame = self.capture.read()
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                    image_frame = Image.fromarray(frame)

                    # Convert to CTkImage so it can be displayed later and put into 'output_queue'
                    w, h = image_frame.size
                    w = int(w*self.camera_width_scale)
                    h = int(h*self.camera_height_scale)
                    image_ctk = customtkinter.CTkImage(None, dark_image=image_frame, size=(w, h))
                    self.output_queue.put(image_ctk)

                    if self.input_queue.empty() is False:
                        break

            if 'restart' in val:
                self.capture = None
                print("terminating")
                temp = re.sub(r"restart_", "", val, 1)
                self.camera_number = int(temp)
                print("changed camera to nr: " + str(self.camera_number))
                self.input_queue.put('start')

            if 'set_scale' in val:
                temp = re.findall(r'\d.\d', val)
                self.camera_width_scale = float(temp[0])
                self.camera_height_scale = float(temp[1])


