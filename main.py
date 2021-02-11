#imports
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import tkinter as tk
from tkinter.filedialog import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg







canvas = tk.Tk()
canvas.title = "QR code reader and generator"
canvas.geometry = "600x500"

textfield = tk.Entry(canvas, font = ("poppins", 30, "bold"))
textfield.pack()
def generate_qr_code():
    qrcode_text = textfield.get()
    qr = pyqrcode.create(qrcode_text)
    qr.png("qrcode.png", scale=8)
    img = mpimg.imread('qrcode.png')
    label3 = tk.Label(canvas, text="QR code generated (qrcode.png)")
    label3.pack()
    imgplot = plt.imshow(img)
    plt.show()


label1 = tk.Label(canvas, text ="QR Code generator", font = ("poppins", 30, "bold"))
label1.pack()
button1 = tk.Button(canvas, text = "Generate QR code", command = generate_qr_code)
button1.pack()


canvas.mainloop()




