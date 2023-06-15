import cv2
from PIL import Image, ImageTk
import qrcode
import customtkinter as ctk
from tkinter import filedialog, messagebox
import tkinter as tk

root = ctk.CTk()
root.title("QR Code")
root.geometry("320x450")
root.resizable(False, False)

main_img = ctk.CTkImage(Image.open("main.png"), size=(300, 300))

label1 = ctk.CTkLabel(root, text="", image=main_img)
label1.place(x=10, y=10)

text = tk.StringVar()

entry = ctk.CTkEntry(root, textvariable=text, width=300, font=("Arial", 14), justify="center")
entry.place(x=10, y=325)

button_open = ctk.CTkButton(root, text="Open", width=145, corner_radius=0, fg_color="#ff3838", hover_color="#b52626", command=lambda: open())
button_open.place(x=165, y=405)

button_save = ctk.CTkButton(root, text="Save", width=145, corner_radius=0, fg_color="#ff3838", hover_color="#b52626", command=lambda: save())
button_save.place(x=10, y=405)

button_create = ctk.CTkButton(root, text="Create", width=145, corner_radius=0, fg_color="#ff3838", hover_color="#b52626", command=lambda: create_qr())
button_create.place(x=10, y=365)

button_decode = ctk.CTkButton(root, text="Decode", width=145, corner_radius=0, fg_color="#ff3838", hover_color="#b52626", command=lambda: decode())
button_decode.place(x=165, y=365)


def create_qr():
    global qr_resize
    data = entry.get()
    created_qr = qrcode.make(data)
    qr_resize = created_qr.resize((300,300))
    resim = ImageTk.PhotoImage(qr_resize)
    label1.configure(image=resim)


def save():
    path = filedialog.asksaveasfilename(defaultextension=".png")
    if path:
        qr_resize.save(path)
        messagebox.showinfo("Sucess", "QR Code is Saved")
    else:
        messagebox.showwarning("Error", "Enter Some Data First")


def open():
    global path1
    path1 = filedialog.askopenfilename()
    son = ctk.CTkImage(Image.open(path1), size=(300, 300))
    label1.configure(image=son)
    text.set("You Can Decode Now")


def decode():
    detector = cv2.QRCodeDetector()
    reval, point,s_qr = detector.detectAndDecode(cv2.imread(path1))
    text.set(reval)


root.mainloop()
