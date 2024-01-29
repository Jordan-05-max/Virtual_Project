"""Face detection program"""
import cv2
import tkinter as tk
import facedetection_util
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1250x650+50+20")
        self.login_button_main_window = facedetection_util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)
        self.register_newUser_button_main_window = facedetection_util.get_button(self.main_window, 'register new user',
                                                                                 'gray', self.register_newUser,
                                                                                 fg='black')
        self.register_newUser_button_main_window.place(x=750, y=400)

        self.webcam_label = facedetection_util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'cap'not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_pil = frame

        img_ = cv2.cvtColor(self.most_recent_capture_pil, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)



    def start(self):
        self.main_window.mainloop()

    def login(self):
        pass

    def register_newUser(self):
        pass


if __name__ == "__main__":
    App = App()
    App.start()
