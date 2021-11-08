from tkinter import *
import cv2
from PIL import Image, ImageTk

window = Tk()
window.title("LiveCam2 by HMZ")
# remove the title bar, force quit to close the window
# window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.geometry("+600+300")
display = Label(window)
display.grid(row=0, column=0)
video = cv2.VideoCapture(0)

def show_frame():
    _, frame = video.read()
    frame = cv2.resize(frame, (280, 210))
    frame = cv2.flip(frame, 1)
    cv2img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2img)
    imgtk = ImageTk.PhotoImage(master=display, image=img)
    display.imgtk = imgtk
    display.configure(image=imgtk)
    window.after(10, show_frame)

show_frame()
window.mainloop()