#importing libraries
from turtle import bgcolor
from playsound import playsound
from math import fabs
from tkinter import Menu, messagebox
from idm import IDMan
downloader = IDMan()
import os
from re import A
import tkinter
import customtkinter
import pyperclip
#Designing
customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.geometry("700x400")
app.title("Old Siege Launcher")
app.resizable(False,False)
app.iconbitmap("lib\Logo.ico")
#Center Screen
w = 700
h = 400
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/3) - (w/3)
y = (hs/3) - (h/2.7)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))
#cc
import pygame
pygame.mixer.init()
pygame.mixer.music.load("lib\Music.mp3")
pygame.mixer.music.play(-1)
whitetext = customtkinter.CTkLabel(text="                   Old Siege Iran                         ",fg_color="Grey27",text_font=("Helvetica 15 bold",30),text_color="PaleGreen2",width=700,height=20,)
whitetext.place(x=100,y=0)
def toggleMusic():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        
        

    else:
          pygame.mixer.music.unpause()

check_box_1 = customtkinter.CTkCheckBox(master=app,text="موزیک",text_font=("Tahoma",12),text_color="Gold",width=40,command=toggleMusic)
check_box_1.place(x=570,y=270)
check_box_1.select()
pygame.mixer.music.unpause()
#CCCCCCCCCCCCC 170 320

ctext = customtkinter.CTkLabel(master=app, text="کپی شد",text_font="Tahoma")
ctext.place(x=2,y=320)

lcolor = customtkinter.CTkLabel(master=app, text="            ",bg_color="Grey65",height=9000,width=200)
lcolor.place(x=1,y=1)

#defs
def button_function():
    os.startfile("lib\Old-Siege-Iran.exe")
def Closeapp():
    os.system("taskkill /im Old-Siege-Iran.exe /t /f")
#Velvet shell links
vurl1 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part01.rar"
vurl2 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part02.rar"
vurl3 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part03.rar"
vurl4 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part04.rar"
vurl5 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part05.rar"
vurl6 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part06.rar"
vurl7 = "https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part07.rar"

#White noise links
url1 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part01.rar"
url2 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part02.rar"
url3 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part03.rar"
url4 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part04.rar"
url5 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part05.rar"
url6 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part06.rar"
url7 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part07.rar"
url8 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part08.rar"
url9 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part09.rar"
url10 = "https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part10.rar"
#--------------------

#########1
def p1c():
    ctext.place(x=190,y=13)
    pyperclip.copy(url1)
    downloader.download(url1, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)

p1 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 1",text_font="Tahoma",command=p1c)
p1.place(x=40,y=12)
#######################
def p1c2():
    ctext.place(x=190,y=49)
    pyperclip.copy(url2)
    downloader.download(url2, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
po = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 2",text_font="Tahoma",command=p1c2)
po.place(x=40,y=48)
#################
def p1c3():
    ctext.place(x=190,y=85)
    pyperclip.copy(url3)
    downloader.download(url3, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p3 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 3",text_font="Tahoma",command=p1c3)
p3.place(x=40,y=84)
#################
def p1c3():
    ctext.place(x=190,y=121)
    pyperclip.copy(url4)
    downloader.download(url4, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p4 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 4",text_font="Tahoma",command=p1c3)
p4.place(x=40,y=120)
###############
def p1c3():
    ctext.place(x=190,y=157)
    pyperclip.copy(url5)
    downloader.download(url5, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p5 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 5",text_font="Tahoma",command=p1c3)
p5.place(x=40,y=156)
#################
def p1c3():
    ctext.place(x=190,y=193)
    pyperclip.copy(url6)
    downloader.download(url6, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p6 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 6",text_font="Tahoma",command=p1c3)
p6.place(x=40,y=192)
##################
def p1c3():
    ctext.place(x=190,y=229)
    pyperclip.copy(url7)
    downloader.download(url7, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p2 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 7",text_font="Tahoma",command=p1c3)
p2.place(x=40,y=228)
##################
def p1c3():
    ctext.place(x=190,y=265)
    pyperclip.copy(url8)
    downloader.download(url8, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p8 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 8",text_font="Tahoma",command=p1c3)
p8.place(x=40,y=264)
##################
def p1c3():
    ctext.place(x=190,y=301)
    pyperclip.copy(url9)
    downloader.download(url9, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p9 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 9",text_font="Tahoma",command=p1c3)
p9.place(x=40,y=300)
##################
def p1c3():
    ctext.place(x=190,y=337)
    pyperclip.copy(url10)
    downloader.download(url10, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
p10 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 10",text_font="Tahoma",command=p1c3)
p10.place(x=40,y=336)
#-------------------

#velvet buttons-----------------------------------------------------------------

def vp1c():
    ctext.place(x=190,y=13)
    pyperclip.copy(vurl1)
    downloader.download(vurl1, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)

vp1 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 1",text_font="Tahoma",command=vp1c)

#######################
def vp1c2():
    ctext.place(x=190,y=49)
    pyperclip.copy(vurl2)
    downloader.download(vurl2, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vpo = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 2",text_font="Tahoma",command=vp1c2)

#################
def vp1c3():
    ctext.place(x=190,y=85)
    pyperclip.copy(vurl3)
    downloader.download(vurl3, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vp3 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 3",text_font="Tahoma",command=vp1c3)

#################
def vp1c3():
    ctext.place(x=190,y=121)
    pyperclip.copy(vurl4)
    downloader.download(vurl4, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vp4 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 4",text_font="Tahoma",command=vp1c3)

###############
def vp1c3():
    ctext.place(x=190,y=157)
    pyperclip.copy(vurl5)
    downloader.download(vurl5, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vp5 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 5",text_font="Tahoma",command=vp1c3)

#################
def vp1c3():
    ctext.place(x=190,y=193)
    pyperclip.copy(vurl6)
    downloader.download(vurl6, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vp6 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 6",text_font="Tahoma",command=vp1c3)

##################
def vp1c3():
    ctext.place(x=190,y=229)
    pyperclip.copy(vurl7)
    downloader.download(vurl7, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)
vp2 = customtkinter.CTkButton(master=app,width=110,height=30,border_width=2,corner_radius=0,text="پارت 7",text_font="Tahoma",command=vp1c3)

vp3.place(x=40,y=600)
vpo.place(x=40,y=600)
vp1.place(x=40,y=600)    
vp2.place(x=40,y=600)
vp6.place(x=40,y=600)
vp5.place(x=40,y=600)
vp4.place(x=40,y=600) 
#------------------
a = 0
def seaseonc():
    global a
    if a == 0:
     whitetext.place(x=-9999,y=369)
     velvet.place(x=23,y=369)
     ctext.place(x=2,y=320)
     a = 2
     p1.place(x=-9999,y=999999)
     p2.place(x=-9999,y=999999)
     po.place(x=-9999,y=999999)
     p3.place(x=-9999,y=999999)
     p10.place(x=-9999,y=999999)  
     p4.place(x=-9999,y=999999) 
     p5.place(x=-9999,y=999999)        
     p8.place(x=-9999,y=999999)  
     p6.place(x=-9999,y=999999)
     p9.place(x=-9999,y=999999)
     vp3.place(x=40,y=84)
     vpo.place(x=40,y=48)
     vp1.place(x=40,y=12)    
     vp2.place(x=40,y=228)
     vp6.place(x=40,y=192)
     vp5.place(x=40,y=156)
     vp4.place(x=40,y=120)  
    else:
        ctext.place(x=2,y=320)
        velvet.place(x=-99999,y=369)
        whitetext.place(x=23,y=369)
        a = 0
        p10.place(x=40,y=336)
        p9.place(x=40,y=300)
        p2.place(x=40,y=228)
        p8.place(x=40,y=264)
        p1.place(x=40,y=12)
        po.place(x=40,y=48)
        p4.place(x=40,y=120)
        p5.place(x=40,y=156)
        p3.place(x=40,y=84)
        p6.place(x=40,y=192)
        vp3.place(x=40,y=600)
        vpo.place(x=40,y=600)
        vp1.place(x=40,y=600)    
        vp2.place(x=40,y=600)
        vp6.place(x=40,y=600)
        vp5.place(x=40,y=600)
        vp4.place(x=40,y=600) 
# Buttons
openapp = customtkinter.CTkButton(master=app, text="ورود به اپلیکیشن", command=button_function,text_font="Tahoma")
openapp.place(x=400,y=320)
closeapp = customtkinter.CTkButton(master=app, text="بستن اپلیکیشن", command=Closeapp,text_font="Tahoma")
closeapp.place(x=548,y=320)
changes = customtkinter.CTkButton(master=app, text="تغییر سیزن", command=seaseonc,text_font="Tahoma")
changes.place(x=400,y=269)

def on_closing ():
 if messagebox.askyesno("Quit", "آیا میخواهید خارج شوید ؟"):
     app.destroy()
     os.system("taskkill /im Old-Siege-Iran.exe /t /f")
app.protocol("WM_DELETE_WINDOW", on_closing)

whitetext = customtkinter.CTkLabel(text="White Noise",bg_color="Grey65",fg_color="Grey57",text_color="black")
whitetext.place(x=23,y=369)
velvet = customtkinter.CTkLabel(text="Velvet Shell",bg_color="Grey65",fg_color="Grey57",text_color="black")
velvet.place(x=-99999,y=369)
app.mainloop()