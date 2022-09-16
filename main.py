import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk


my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window
my_w.columnconfigure(0, weight=1)
my_w.columnconfigure(1, weight=3)
my_w.title('Watermark Adder')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w, text='Add Watermark to your photo with a click', width=100, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload File',
    command = lambda:upload_file())
b1.grid(row=2, column=1)



def upload_file():
    global img
    global type
    global b2, b4
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((400,200)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(my_w,image=img) # using Button
    b2.grid(row=3, column=1)
    b4 = tk.Button(my_w, text='Add Image',
       command = lambda:add_img_watermark())
    b4.grid(row=5, column=1)






def add_img_watermark():
    global logo
    global img
    global b2, b4
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    logo=Image.open(filename)
    logo_resized = logo.resize((5, 10))
    image_copy = ImageTk.getimage(img).copy()
    position = ((340), (140))
    image_copy.paste(logo, position)
    ready=ImageTk.PhotoImage(image_copy)
    rgb_im = image_copy.convert('RGB')
    rgb_im.save('audacious.jpg')
    img = ImageTk.PhotoImage(file='audacious.jpg')
    b2.grid_forget()
    canv = Canvas(my_w, width=400, height=200, bg='white')
    canv.create_image(
        0,
        0,
        anchor=NW,
        image=img
        )
    canv.grid(row=4, column=1)
    b4.grid_forget()
    l1 = Label(text="saved!")
    l1.grid(row=5, column=1)


my_w.mainloop()
