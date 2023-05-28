from tkinter import *
from PIL import Image, ImageTk
import time
import pygame
from pygame import mixer
import random

#Musica para la pantalla principal
mixer.init()
cancion = mixer.Sound("X2Download.app - Tokyo Drift (Fast & Furious) (64 kbps).mp3")
mixer.Sound.set_volume(cancion, 0.1)


#Ventana Principal
ventana = Tk()
ventana.title("Carrito")
ventana.geometry("987x629")
ventana.resizable(False, False)
cancion.play()

#Canvas
canvas1 = Canvas(ventana, width=989, height=629, bg="#D5D2FF")
canvas1.place(x=-1, y=0)

#Imagen fondo
imgfondo = Image.open("foto carro amarillo Oficial.jpg")
resizedfondo = imgfondo.resize((987, 629), Image.ANTIALIAS)
nvofondo = ImageTk.PhotoImage(resizedfondo)
fndbg = canvas1.create_image(0, 0, image=nvofondo, anchor=NW)

#Titulo
imgtitulo = Image.open("titulo RC.png")
resizedtitulo = imgtitulo.resize((495, 200), Image.ANTIALIAS)
nvotitulo = ImageTk.PhotoImage(resizedtitulo)
titulo = canvas1.create_image(290, 0, image=nvotitulo, anchor=NW)

btnjugar = Button(ventana, text="PLAY", width=10, height=2).place(relx=0.44, rely=0.85)
btnfuera = Button(ventana, text="SALIR", width=12, height=2, command=lambda: [ventana.destroy()]).place(relx=0.03, rely=0.05)

ventana.mainloop()


