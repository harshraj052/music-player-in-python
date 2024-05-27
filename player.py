import time
from tkinter import *  # importing all classes from tkinter
# Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python. As Tk and Tkinter are available on most of the Unix platforms as well as on the Windows system, developing GUI applications with Tkinter becomes the fastest and easiest.
from tkinter import filedialog 
# File dialogs help you open, save files or directories. This is the type of dialog you get when you click file,open. This dialog comes out of the module, there’s no need to write all the code manually.Tkinter does not have a native looking file dialog, instead it has the customer tk style.
from pygame import mixer #pygame is a library
# importing mixer class from pygame to get the buttons functioning to make our mp3 music like mp3 file to start playing, to pause it and to resume it again.
import os

root = Tk() #creating tkinter window
root.title("Evee Music Player")
# title method to give a title to the tkinter window
root.geometry("485x700+290+10")
# geometry method is used to set the dimensions of the tkinter window
root.configure(background = "#333333") # setting a color to the background
root.resizable(False,False) # false to not allow to resize both in x axis and y axis
# resizable method used to allow tkinter root window to change its size according to user's need as well as it will prohibit like it will not allow you to change size of window
mixer.init() #initialising mixer class



def AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
             if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

lower_frame=Frame(root, bg="#FFFFFF", width=485, height=180) # lower_frame is a variable here
# frame is a widget in tkinter.It is a rectangular region on the screen. A frame can also be used as a foundation class to implement complex widgets. It is used to organize a group of widgets
lower_frame.place(x=0, y=400)
# place method allows you to explicitly set the position and size of a window, either in absolute terms, or relative to another window. You can access the place manager through the place() method which is available for all standard widgets.

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

frameCnt=30
frames=[PhotoImage(file="aa1.gif", format='gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind+=1
    if ind == frameCnt:
        ind=0
    label.configure(image=frame)
    root.after(40, update, ind)

label=Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)





ButtonPlay= PhotoImage(file="play1.png")
Button(root, image=ButtonPlay, bg= "#FFFFFF", bd=0, height=60, width=60, command=PlayMusic).place(x=215, y=487)

ButtonStop=PhotoImage(file="stop1.png")
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60, command= mixer.music.stop).place(x=130, y=487)

ButtonPause= PhotoImage(file="pause1.png")
Button(root, image= ButtonPause, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.pause).place(x=300, y=487)

#Volume1= PhotoImage(file="volume.png")
#Button(root, image= Volume1, bg="#FFFFFF", bd=0, height=60, width=60, command= mixer.music.unpause).place(x=20, y=487)

Menu = PhotoImage(file = "menu.png")
Label(root, image = Menu).place(x=0, y=580, width=485, height=100)
# Tkinter Label is a widget that is used to implement display boxes where you can place text or images.


Frame_Music=Frame(root, bd=2, relief= RIDGE)
# The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
Frame_Music.place(x=0, y=585, width=485, height=100)


Button(root, text= "Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF", command= AddMusic).place(x=0, y=550)

Scroll= Scrollbar(Frame_Music)
Playlist= Listbox(Frame_Music, width=100, font=("Times New Roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)

Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()
 

