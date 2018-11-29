import subprocess as sp
import time
from tkinter import *


window = Tk()

path="/home/emmanuel/Escritorio/talos-master/Ffmpeg_CapVid_Frames.py"
window.title("STB Tester interface")

def launch():
    exec(open(path).read())

window.geometry('400x250')

lbl = Label(window, text="Obtener datos del equipo STB:")

lbl.grid(column=3, row=3)

btn = Button(window, text="Obtener Datos", command=launch)
btn.grid()
btn.grid(column=10, row=4)

photo = PhotoImage(file="izzi_logo.png")
window = Label(image=photo)
window.photo = photo
window.grid(column=30, row=0)

window.mainloop()
