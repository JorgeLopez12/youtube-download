from pytube import YouTube
from tkinter import *
from tkinter import messagebox

def accion():
    try:
        if videos:
            enlace = videos.get()
            video = YouTube(enlace) #agrega el enlace a video
            descarga = video.streams.get_highest_resolution() #descarga el video en alta resolucion
            descarga.download()
    except Exception as e:
        messagebox.showerror('Error', f'Something go wrong T-T :\n\n {e}')

def popup():
    messagebox.showinfo('Visit my linkedin', 'https://www.linkedin.com/in/jorge-alberto-lópez-sánchez-b71b85194/')

root = Tk()
root.config(bd=15)
root.title("Douwnload youtube vidios ^u^")

imagen = PhotoImage(file='Youtube_logo.png')
foto = Label(root, image=imagen, bd=0.1)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Click for more information', menu=helpmenu)
helpmenu.add_command(label='autor information', command=popup)
menubar.add_command(label='Go out ^u^', command=root.destroy)

instruccion = Label(root, text='Program to download youtube videos :3 \n')
instruccion.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text='Download', command=accion)
boton.grid(row=2, column=1)

root.mainloop()