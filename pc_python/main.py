import cv2
import requests
import threading

from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk


cap = None
running = False

ESP_IP = ""
speed = 50



# Connect RTSP Stream
def start_stream():

    global cap
    global running

    rtsp_url = rtsp_entry.get()

    if rtsp_url == "":
        messagebox.showerror("Error", "Enter RTSP URL")
        return

    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot open RTSP stream")
        return

    running = True

    threading.Thread(target=video_loop, daemon=True).start()


# Video Loop
def video_loop():

    global cap
    global running

    while running:

        ret, frame = cap.read()

        if not ret:
            continue

        # frame = cv2.resize(frame, (640, 480))

        h, w = frame.shape[:2]

        new_height = 600
        new_width = int((w / h) * new_height)

        frame = cv2.resize(frame, (new_width, new_height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = Image.fromarray(frame)

        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk

        video_label.configure(image=imgtk)


# Connect Robot
def connect_robot():

    global ESP_IP

    ESP_IP = ip_entry.get()

    if ESP_IP == "":
        messagebox.showerror("Error", "Enter ESP IP")
        return

    messagebox.showinfo("Connected", f"Robot IP set to {ESP_IP}")



# Send command to robot
def send_command(cmd):

    global ESP_IP

    if ESP_IP == "":
        messagebox.showerror("Error", "Connect robot first")
        return

    try:

        requests.get(f"http://{ESP_IP}/{cmd}")

    except Exception as e:

        print("Error:", e)


# Speed controls
def speed_up():

    send_command("+")


def speed_down():

    send_command("-")



def disconnect_all():

    global running
    global cap
    global ESP_IP

    running = False

    if cap is not None:
        cap.release()

    ESP_IP = ""

    video_label.configure(image='')

    messagebox.showinfo("Disconnected", "Camera and Robot disconnected")



# GUI Window
root = Tk()

root.title("RTSP Robot Controller")

root.geometry("900x700")


# RTSP Section
Label(root, text="RTSP URL").pack()

rtsp_entry = Entry(root, width=60)
rtsp_entry.pack()

Button(root, text="Start Stream", command=start_stream).pack(pady=5)


# Video Display
video_label = Label(root)
video_label.pack(pady=10)


# Robot IP Section
Label(root, text="ESP Robot IP").pack()

ip_entry = Entry(root, width=30)
ip_entry.pack()

Button(root, text="Connect Robot", command=connect_robot).pack(pady=5)


# Controls
control_frame = Frame(root)
control_frame.pack(pady=20)

Button(control_frame, text="FORWARD", width=15,
       command=lambda: send_command("F")).grid(row=0, column=1)

Button(control_frame, text="LEFT", width=15,
       command=lambda: send_command("L")).grid(row=1, column=0)

Button(control_frame, text="STOP", width=15,
       command=lambda: send_command("S")).grid(row=1, column=1)

Button(control_frame, text="RIGHT", width=15,
       command=lambda: send_command("R")).grid(row=1, column=2)

Button(control_frame, text="BACKWARD", width=15,
       command=lambda: send_command("B")).grid(row=2, column=1)


# Speed Buttons
speed_frame = Frame(root)
speed_frame.pack(pady=10)

Button(speed_frame, text="Speed +", width=15,
       command=speed_up).grid(row=0, column=0)

Button(speed_frame, text="Speed -", width=15,
       command=speed_down).grid(row=0, column=1)

Button(root,
       text="Disconnect Feed",
       width=20,
       bg="red",
       fg="white",
       command=disconnect_all).pack(pady=10)



# Main loop
root.mainloop()