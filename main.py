from tkinter import *
from tkinter import messagebox, filedialog
import random as r
import urllib.request
import os
import time
from PIL import Image,ImageTk
from cryptography.fernet import Fernet as fn
def show_frame(frame_faces):
    frame_faces.tkraise()
key = b'pythonprojectpatternrecognitionbyjntuacsede='
fr = fn(key)
win = Tk()
win.title("ARTS_VAN")
win.geometry("1100x600")
win.state("zoomed")
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)
frame1 = Frame(win)
frame2 = Frame(win)
frame3 = Frame(win)
frame4 = Frame(win)
frame5 = Frame(win)
v1 = StringVar(win)
v2 = StringVar(win)
v3 = StringVar(win)
v4 = StringVar(win)
f4var = 404
custom = 404
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0, column=0, sticky='nsew')
t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
m1, m2, m3, m4, m5, m6, m7, m8, m9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
lt = []
sd = []
tst = []
sql = []
lite = 0
lst = []
wcount = 0
kl = 0
ml = 0
sqc = 0
if os.path.exists('file.txt'):
    kl = 1
    with open('file.txt','r') as file:
        t = file.read()
        data = fr.decrypt(t.encode()).decode()
    lt = data.split()
if os.path.exists('data.txt'):
    ml = 1
imglist = ['coffee.png', 'apple.png', 'diarymilk.png','shinchan.png','mananime.png','femanime.png','dhoni.png','hacker.png','jntua.png','bg1.jpeg','bg2.jpg']
lrus = ['https://blogger.googleusercontent.com/img/a/AVvXsEhRi9OuHkRPBbFSpIPfgR4Ug5EuWJ-c5CBHv3cPXON6UnPOcGYxPFl1Em-o_3ydZtX5dqirq9Ia_Fx4xKUWxUscQGrCn83qOUCidq6xK-eZpS45-dTakci93FyJgOBBAWqTxRcd9CIVsiJoJ8Y7Af4d2h6s4IUxyPp8heOkmrDUjayFRljyjFT0Ospr=s195',
        'https://blogger.googleusercontent.com/img/a/AVvXsEhrvWXhT1sFHqCRdovAzdOesyWB5l-OHyMTScdMj-T67_av5i9rjDSG5rbZTJc6in0hBLOX3KAssQ4mDgC3JOy-wfcbpHiIIxxYe_K1u06Cy_OktnzgxNaLhy19-F-8nZ7qsrKapWyrlzVHIKbSfr-lg_AQ1uZDbZdgZjwnwwsoXBNirPuKP1ZW6T68=s192',
        'https://blogger.googleusercontent.com/img/a/AVvXsEiVKL1drw4A0NshmFU4GogxpRb81zJNA2d90OobQWnSEO_EhLF9IHQ0eYKdBAI2kMEI04b0xt3hQta0bctg9b9RQelnJ7VCxdLit6QUUSk2oiorAG4YDbzVDqn2Mhgr3XwNjez_Lrphz1q2Gow7KsZscHnTvwv5XO-CS7iaW8lwUBY3WXXIY-Rgva8i=s185',
        'https://blogger.googleusercontent.com/img/a/AVvXsEh3I7_ROq8_YUVwK9b9dIzr0nrVng5NuolZZx13iDmywtuGWHVNrf5TbjJNi9rUBpVkpbDd0TfENB6x2ukX2D3JyZQZP_LKMnkFcK95bqZEoc96xHAe6qlwYeNyiVmL6NLHmdkSw8AbRArogbwWh-xEAEsBEPgK-buxA97ZRdUbVNdkDWjNG3K5qhDe=s184',
        'https://blogger.googleusercontent.com/img/a/AVvXsEis2DpA-t034VyK9qfGhzw1KM-bNOSSa20n8i5vIARAR9ge9K9okY1Bti2sKD0dKHnyioJUUX0QOpSliYD6fqC6qk1r9FtzSIGAjal8YtUqxcKGpXJ5QcgZwqUUJY5Q0oM15QLkmCap6nb_y3KDbEEIv12I1C3GVB9eSXd9lS8AJZaQYgKjUh0x2tMy=s196',
        'https://blogger.googleusercontent.com/img/a/AVvXsEhH5AWuBGUm4UQ1BI1UtzT84swysRJoT9gnWufKVAlGtYO-ETCkM5MeiLpv5owSkyQJSyMqUAMf4hY3EzMea5umQLKUoBFZhdb538gVxOquqaMxWcPKsp0kODUk0GIOKNqe7p9jYeW6LC5KTss3dIX2NcCvOc-9FY24Su2H08q1D0NHOpDsLMsRGDb4=s180',
        'https://blogger.googleusercontent.com/img/a/AVvXsEgOwiBYONeYzv1fUmzmwXiP2Uc4dtdaNh5gRBCH5ij81RapWk5bMUkMBVFictYq4GtihdMPEQalVl7Q3FcFwUrFdYd-4wgz3R_yMO_vtSF7lxokmqIIWpnj-BJgTaASMSKA4-xIaPEWQiMA9ZyxXJ62DAbL3W1PsVsOUdG5QFU0YB6lNZWB_SnnHyfY=s196',
        'https://blogger.googleusercontent.com/img/a/AVvXsEjhEW_d2OH2tQis2nbJEkfyO_NJ-1GxXjY76cHRRxoRHnE4OuxZPobEmZbm_QjwkYYAHJpi1JgVzmW-6Sy0gxbvH8FWISzT_KXMrPU08DxsnPWKiSb7FW6UuQ5q-xqQpxRYhlc8RRu3fB5dho-H4n4tXl_yt_r96X-gRsLete73S4aBbLo_cmPGOgwU=s188',
        'https://blogger.googleusercontent.com/img/a/AVvXsEilljyG5ePElMZZNva_WSXc8UMRyNJPqI6sq3yPAkB7Bs0lxWTM4KpznDPPB1mKv9UGH3LWecbs6TvHHJbNQBHUCPOOD28719kRHifN1ZLTttFoRiXj7HNvydvZ-DH1bD6Bn5gUN94LOCSl0p12C4Qgj52c8Hw8PGUsP6bOz-WJ5TJyPn0Rdk4xHCW5=s187',
        'https://blogger.googleusercontent.com/img/a/AVvXsEgIer1woSV0CpwYz47r5gzuKQkGLtw3cLfqAbExuotBuhnqw-Hc5dmqVCeTgCtfC0xdBNtj1vsuBKeyH9qJxHQIFRU8GSXYM86e_mnIQCdY3WDJObQV-JYAf7_7MgXENZMdsRwvEpl9M0f20qA65RRkvAFdlRdy6RUj72JqX7Md1e9Rqbdyrl0-02SX=s1920',
        'https://blogger.googleusercontent.com/img/a/AVvXsEgPgfH_05RrDpG-rYt-qHpbf4mezw-ibAC_4P7CY0A2gNVcNTuGMB3fC-IQ1jByn0UwOtdZT05Z0mVKaJeVl3jeuqVAUBz1k59yYSzEepni426TVRgyj3pzwxeDH6doW27GDgQjib_iiMjtLNtH1ePYmxJdfktnePFUv87jIrMxf4E_lIYcSQTSB9em=s1920']
l1 = Label(frame1, text='Set the Sequence order of Images :', font=('Arial', 15, 'bold'), fg='Brown')
l2 = Label(frame1, text='Enter your Password Sequence :', font=('Arial', 15, 'bold'), fg='Brown')
lb1 = Label(frame3, text='Answer the Security Questions for Security Reasons :', font=('Arial', 15, 'bold'), fg='Brown')
lb2 = Label(frame3, text='What is your Pet name :', font=('Arial', 15, 'bold'), fg='Brown')
lb3 = Label(frame3, text='What is your Elementary School name :', font=('Arial', 15, 'bold'), fg='Brown')
lb4 = Label(frame3, text='Who was your favourite hero :', font=('Arial', 15, 'bold'), fg='Brown')
lb5 = Label(frame3, text='Each Question has only 3 attempts!!', font=('Arial', 12, 'bold'), fg='Brown')
en1 = Entry(frame3, textvariable = v1, width = 24, font=('arial', 20))
en2 = Entry(frame3, textvariable = v2, width = 24, font=('arial', 20))
en3 = Entry(frame3, textvariable = v3, width = 24, font=('arial', 20))
pr = 0
def exitp():
    os.remove('file.txt')
    if os.path.exists('data.txt'):
        os.remove('data.txt')
    if os.path.exists('nothing.txt'):
        os.remove('nothing.txt')
    if os.path.exists('imaglist.txt'):
        os.remove('imaglist.txt')
    win.destroy()
    quit()
try:
    for i in imglist:
        if os.path.exists(i):
            pass
        else:
            urllib.request.urlretrieve(lrus[pr],i)
        pr = pr + 1
except(urllib.error.URLError):
    messagebox.showerror('NO INTERNET','Please Connect to the Internet to Download the Files!')
    exitp()
bg1 = ImageTk.PhotoImage(file="bg1.jpeg")
Label(frame1, image=bg1).place(x=0, y=0, relwidth=1, relheight=1)
bg2 = ImageTk.PhotoImage(file="bg2.jpg")
Label(frame2, image=bg2).place(x=0, y=0, relwidth=1, relheight=1)
frame2_label = Label(frame2, text='...** WELCOME **...', font=('Algerian', 50, 'bold'), fg='Blue', bg='pink')
frame2_label.place(x=450, y=120)
frame2_button = Button(frame2, text="LOGOUT", fg='black', bg='wheat', font=("Baskerville Old Face", 24, "bold"),command=lambda: show_frame(frame1))
frame2_button.place(x=650, y=500)

f5ilt = []

i1,i2,i3,i4,i5,i6,i7,i8,i9='','','','','','','','',''
b1,b2,b3,b4,b5,b6,b7,b8,b9=0,0,0,0,0,0,0,0,0
ls = []

def coffee():
    global t1, m1, lite
    if lite == 0:
        if t1 == 0:
            t1 = 1
            b1.config(borderwidth=5, bg='grey')
            lt.append('coffee-1')
        elif t1 == 1:
            t1 = 0
            b1.config(borderwidth=0, bg='white')
            lt.remove('coffee-1')
    elif lite == 1:
        if m1 == 0:
            m1 = 1
            b1.config(borderwidth=5, bg='grey')
            tst.append('coffee-1')
        elif m1 == 1:
            m1 = 0
            b1.config(borderwidth=0, bg='white')
            tst.remove('coffee-1')
def apple():
    global t2, m2, lite
    if lite == 0:
        if t2 == 0:
            t2 = 1
            b2.config(borderwidth=5, bg='grey')
            lt.append('apple-2')
        elif t2 == 1:
            t2 = 0
            b2.config(borderwidth=0, bg='white')
            lt.remove('apple-2')
    elif lite == 1:
        if m2 == 0:
            m2 = 1
            b2.config(borderwidth=5, bg='grey')
            tst.append('apple-2')
        elif m2 == 1:
            m2 = 0
            b2.config(borderwidth=0, bg='white')
            tst.remove('apple-2')
def diarymilk():
    global t3, m3, lite
    if lite == 0:
        if t3 == 0:
            t3 = 1
            b3.config(borderwidth=5, bg='grey')
            lt.append('diarymilk-3')
        elif t3 == 1:
            t3 = 0
            b3.config(borderwidth=0, bg='white')
            lt.remove('diarymilk-3')
    elif lite == 1:
        if m3 == 0:
            m3 = 1
            b3.config(borderwidth=5, bg='grey')
            tst.append('diarymilk-3')
        elif m3 == 1:
            m3 = 0
            b3.config(borderwidth=0, bg='white')
            tst.remove('diarymilk-3')
def shinchan():
    global t4, m4, lite
    if lite == 0:
        if t4 == 0:
            t4 = 1
            b4.config(borderwidth=5, bg='grey')
            lt.append('shinchan-4')
        elif t4 == 1:
            t4 = 0
            b4.config(borderwidth=0, bg='white')
            lt.remove('shinchan-4')
    elif lite == 1:
        if m4 == 0:
            m4 = 1
            b4.config(borderwidth=5, bg='grey')
            tst.append('shinchan-4')
        elif m4 == 1:
            m4 = 0
            b4.config(borderwidth=0, bg='white')
            tst.remove('shinchan-4')
def mananime():
    global t5, m5, lite
    if lite == 0:
        if t5 == 0:
            t5 = 1
            b5.config(borderwidth=5, bg='grey')
            lt.append('mananime-5')
        elif t5 == 1:
            t5 = 0
            b5.config(borderwidth=0, bg='white')
            lt.remove('mananime-5')
    elif lite == 1:
        if m5 == 0:
            m5 = 1
            b5.config(borderwidth=5, bg='grey')
            tst.append('mananime-5')
        elif m5 == 1:
            m5 = 0
            b5.config(borderwidth=0, bg='white')
            tst.remove('mananime-5')
def femanime():
    global t6, m6, lite
    if lite == 0:
        if t6 == 0:
            t6 = 1
            b6.config(borderwidth=5, bg='grey')
            lt.append('femanime-6')
        elif t6 == 1:
            t6 = 0
            b6.config(borderwidth=0, bg='white')
            lt.remove('femanime-6')
    elif lite == 1:
        if m6 == 0:
            m6 = 1
            b6.config(borderwidth=5, bg='grey')
            tst.append('femanime-6')
        elif m6 == 1:
            m6 = 0
            b6.config(borderwidth=0, bg='white')
            tst.remove('femanime-6')
def dhoni():
    global t7, m7, lite
    if lite == 0:
        if t7 == 0:
            t7 = 1
            b7.config(borderwidth=5, bg='grey')
            lt.append('dhoni-7')
        elif t7 == 1:
            t7 = 0
            b7.config(borderwidth=0, bg='white')
            lt.remove('dhoni-7')
    elif lite == 1:
        if m7 == 0:
            m7 = 1
            b7.config(borderwidth=5, bg='grey')
            tst.append('dhoni-7')
        elif m7 == 1:
            m7 = 0
            b7.config(borderwidth=0, bg='white')
            tst.remove('dhoni-7')
def hacker():
    global t8, m8, lite
    if lite == 0:
        if t8 == 0:
            t8 = 1
            b8.config(borderwidth=5, bg='grey')
            lt.append('hacker-8')
        elif t8 == 1:
            t8 = 0
            b8.config(borderwidth=0, bg='white')
            lt.remove('hacker-8')
    elif lite == 1:
        if m8 == 0:
            m8 = 1
            b8.config(borderwidth=5, bg='grey')
            tst.append('hacker-8')
        elif m8 == 1:
            m8 = 0
            b8.config(borderwidth=0, bg='white')
            tst.remove('hacker-8')
def jntua():
    global t9, m9, lite
    if lite == 0:
        if t9 == 0:
            t9 = 1
            b9.config(borderwidth=5, bg='grey')
            lt.append('jntua-9')
        elif t9 == 1:
            t9 = 0
            b9.config(borderwidth=0, bg='white')
            lt.remove('jntua-9')
    elif lite == 1:
        if m9 == 0:
            m9 = 1
            b9.config(borderwidth=5, bg='grey')
            tst.append('jntua-9')
        elif m9 == 1:
            m9 = 0
            b9.config(borderwidth=0, bg='white')
            tst.remove('jntua-9')

def imgdecl():
    global i1,i2,i3,i4,i5,i6,i7,i8,i9,b1,b2,b3,b4,b5,b6,b7,b8,b9,ls,f5ilt,lst
    if os.path.exists('imaglist.txt'):
        with open('imaglist.txt','r') as fd:
            dt = fd.read()
            dt = (fr.decrypt(dt.encode())).decode()
            lst = dt.split('\n')
        im1 = Image.open(lst[0])
        im2 = Image.open(lst[1])
        im3 = Image.open(lst[2])
        im4 = Image.open(lst[3])
        im5 = Image.open(lst[4])
        im6 = Image.open(lst[5])
        im7 = Image.open(lst[6])
        im8 = Image.open(lst[7])
        im9 = Image.open(lst[8])
        q1 = im1.resize((180,180))
        q2 = im2.resize((180,180))
        q3 = im3.resize((180,180))
        q4 = im4.resize((180,180))
        q5 = im5.resize((180,180))
        q6 = im6.resize((180,180))
        q7 = im7.resize((180,180))
        q8 = im8.resize((180,180))
        q9 = im9.resize((180,180))
        '''for lm,ln in zip((im1,im2,im3,im4,im5,im6,im7,im8,im9),imglist):
            lm = lm.resize((150,150))'''
        i1 = ImageTk.PhotoImage(q1)
        i2 = ImageTk.PhotoImage(q2)
        i3 = ImageTk.PhotoImage(q3)
        i4 = ImageTk.PhotoImage(q4)
        i5 = ImageTk.PhotoImage(q5)
        i6 = ImageTk.PhotoImage(q6)
        i7 = ImageTk.PhotoImage(q7)
        i8 = ImageTk.PhotoImage(q8)
        i9 = ImageTk.PhotoImage(q9)
        '''i1 = PhotoImage(file='coffee.png')
        i2 = PhotoImage(file='apple.png')
        i3 = PhotoImage(file='diarymilk.png')
        i4 = PhotoImage(file='shinchan.png')
        i5 = PhotoImage(file='mananime.png')
        i6 = PhotoImage(file='femanime.png')
        i7 = PhotoImage(file='dhoni.png')
        i8 = PhotoImage(file='hacker.png')
        i9 = PhotoImage(file='jntua.png')'''
    elif os.path.exists('nothing.txt'):
        i1 = PhotoImage(file='coffee.png')
        i2 = PhotoImage(file='apple.png')
        i3 = PhotoImage(file='diarymilk.png')
        i4 = PhotoImage(file='shinchan.png')
        i5 = PhotoImage(file='mananime.png')
        i6 = PhotoImage(file='femanime.png')
        i7 = PhotoImage(file='dhoni.png')
        i8 = PhotoImage(file='hacker.png')
        i9 = PhotoImage(file='jntua.png')
    b1 = Button(frame1, image=i1, command=coffee, bg='white', borderwidth=0)
    b2 = Button(frame1, image=i2, command=apple, bg='white', borderwidth=0)
    b3 = Button(frame1, image=i3, command=diarymilk, bg='white', borderwidth=0)
    b4 = Button(frame1, image=i4, command=shinchan, bg='white', borderwidth=0)
    b5 = Button(frame1, image=i5, command=mananime, bg='white', borderwidth=0)
    b6 = Button(frame1, image=i6, command=femanime, bg='white', borderwidth=0)
    b7 = Button(frame1, image=i7, command=dhoni, bg='white', borderwidth=0)
    b8 = Button(frame1, image=i8, command=hacker, bg='white', borderwidth=0)
    b9 = Button(frame1, image=i9, command=jntua, bg='white', borderwidth=0)
    ls =[b1, b2, b3, b4, b5, b6, b7, b8, b9]
def place():
    global ls,sd
    a, b = 200, 100
    j = 0
    sd.clear()
    imgdecl()
    while len(sd) != 9:
        d = int(r.random() * 9)
        if d not in sd:
            sd.append(d)
            ls[d].place(x=a, y=b)
            a = a + 270
            j = j+1
            if j==3:
                j=0
                a=200
                b=b+220
def con():
    global m1, m2, m3, m4, m5, m6, m7, m8, m9, wcount,ls
    if lt == tst:
        wcount = 0
        show_frame(frame2)
    elif lt != tst:
        messagebox.showerror('UNSUCCESSFUL', message='WRONG PATTERN')
        wcount = wcount+1
    if(wcount==5):
        messagebox.showwarning('WARNING','Many Unsuccessful Attempts,\n Please WAIT for 10s to Proceed!!!')
        time.sleep(10)
    if(wcount==10):
        messagebox.showerror('THRESHOlD BREACH','Too many Unsuccessful Attempts,\nSELF DESTRUCTION MODE Activated!!!')
        exitp()
    m1, m2, m3, m4, m5, m6, m7, m8, m9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    tst.clear()
    for i in ls:
        i.place_forget()
    place()
    b1.config(borderwidth=0, bg='white')
    b2.config(borderwidth=0, bg='white')
    b3.config(borderwidth=0, bg='white')
    b4.config(borderwidth=0, bg='white')
    b5.config(borderwidth=0, bg='white')
    b6.config(borderwidth=0, bg='white')
    b7.config(borderwidth=0, bg='white')
    b8.config(borderwidth=0, bg='white')
    b9.config(borderwidth=0, bg='white')
def ent():
    l2.place(x=70, y=20)
    global lite, kl
    lite = 1
    but2.place(x=1150, y=340)
    btf.place(x=1080,y=420)
    place()
    b1.config(borderwidth=0, bg='white')
    b2.config(borderwidth=0, bg='white')
    b3.config(borderwidth=0, bg='white')
    b4.config(borderwidth=0, bg='white')
    b5.config(borderwidth=0, bg='white')
    b6.config(borderwidth=0, bg='white')
    b7.config(borderwidth=0, bg='white')
    b8.config(borderwidth=0, bg='white')
    b9.config(borderwidth=0, bg='white')
    if kl==0:
        messagebox.showinfo('PATTERN SET','Your Pattern has been set Successfully')
def setA():
    global ml
    a = v1.get()
    b = v2.get()
    c = v3.get()
    txt = a.lower()+'\n'+b.lower()+'\n'+c.lower()
    with open('data.txt','w') as flp:
        flp.write(fr.encrypt(txt.encode()).decode())
    show_frame(frame1)
    ml = 1
    v1.set('')
    v2.set('')
    v3.set('')
    ent()
def chkC():
    c = v3.get()
    global sqc, kl
    if c.lower()!=sql[2]:
        messagebox.showerror('INCORRECT','Wrong Answer Entered!')
        v3.set('')
        sqc=sqc+1
        if sqc==3:
            messagebox.showerror('THRESHOLD BREACH','Too many Unsuccessful Attempts,\nSELF DESTRUCTION MODE Activated!!!')
            exitp()
    else:
        sqc = 0
        lb4.place_forget()
        en3.place_forget()
        but6.place_forget()
        show_frame(frame1)
        but2.place_forget()
        btf.place_forget()
        but.place(x=1150, y=370)
        lb5.place_forget()
        kl=0
        main()
def chkB():
    b = v2.get()
    global sqc
    if b.lower()!=sql[1]:
        messagebox.showerror('INCORRECT','Wrong Answer Entered!')
        v2.set('')
        sqc=sqc+1
        if sqc==3:
            messagebox.showerror('THRESHOlD BREACH','Too many Unsuccessful Attempts,\nSELF DESTRUCTION MODE Activated!!!')
            exitp()
    else:
        sqc = 0
        lb3.place_forget()
        en2.place_forget()
        but5.place_forget()
        lb4.place(x=30,y=180)
        en3.place(x=400,y=180)
        but6.place(x=350,y=500)
def chkA():
    global sqc
    a = v1.get()
    if a.lower()!=sql[0]:
        messagebox.showerror('INCORRECT','Wrong Answer Entered!')
        v1.set('')
        sqc=sqc+1
        if sqc==3:
            messagebox.showerror('THRESHOlD BREACH','Too many Unsuccessful Attempts,\nSELF DESTRUCTION MODE Activated!!!')
            exitp()
    else:
        sqc = 0
        lb2.place_forget()
        en1.place_forget()
        but4.place_forget()
        lb3.place(x=30,y=180)
        en2.place(x=450,y=180)
        but5.place(x=350,y=500)
but3 = Button(frame3,text = 'SUBMIT', command=setA, font=('arial',20), bg='grey', borderwidth=1)
but4 = Button(frame3,text = 'ANSWER', command=chkA, font=('arial',20), bg='white', borderwidth=1)
but5 = Button(frame3,text = 'ANSWER', command=chkB, font=('arial',20), bg='white', borderwidth=1)
but6 = Button(frame3,text = 'ANSWER', command=chkC, font=('arial',20), bg='white', borderwidth=1)
def std():
    global kl,ls
    l1.place_forget()
    but.place_forget()
    for i in ls:
        i.place_forget()
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    b7.place_forget()
    b8.place_forget()
    b9.place_forget()
    global kl, ml
    if kl==0 or ml==0:
        with open('file.txt','w') as fil:
            data = ''
            for a in lt:
                data = data+a+' '
            fil.write(fr.encrypt(data.encode()).decode())
        kl = 1
        if ml==0:
            show_frame(frame3)
            lb1.place(x=50,y=100)
            lb2.place(x=30,y=180)
            lb3.place(x=30,y=280)
            lb4.place(x=30,y=380)
            en1.place(x=300,y=180)
            en2.place(x=450,y=280)
            en3.place(x=400,y=380)
            but3.place(x=350,y=500)
        else:
            ent()
    else:
        ent()
def fgp():
    show_frame(frame3)
    lb1.place_forget()
    lb2.place_forget()
    lb3.place_forget()
    lb4.place_forget()
    en1.place_forget()
    en2.place_forget()
    en3.place_forget()
    global sql
    if not os.path.exists('data.txt'):
        messagebox.showinfo('MISSING','Security reset data not entered or found missing!')
        exitp()
    with open('data.txt','r') as fg:
        qwd = fg.read()
        sql = fr.decrypt(qwd.encode()).decode().split('\n')
    lb1.place(x=50,y=100)
    lb2.place(x=50,y=180)
    lb5.place(x=50,y=50)
    en1.place(x=300,y=180)
    but4.place(x=350,y=500)
btf = Button(frame1, text='Forgot Password', font=('algerian', 24), command=fgp, bg='orange', fg = 'red')
but2 = Button(frame1, text='CONFIRM', font=('algerian', 24), command=con, bg='orange')
but = Button(frame1, text='SET', font=('algerian', 24), command=std, bg='orange')
f4l1 = Label(frame4, text='Please Select the Images to Proceed :', font=('calibri', 30, 'bold'), fg='black', bg='white')

def main():
    global lite, kl, lt
    Tk.lower(frame2)
    a, b = 150, 100
    lite = 0
    if kl==1:
        ent()
    elif kl == 0:
        but2.place_forget()
        btf.place_forget()
        l2.place_forget()
        l1.place(x=70, y=20)
        but.place(x=1150, y=370)
        place()
def reset():
    global t1, t2, t3, t4, t5, t6, t7, t8, t9, kl
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
    lt.clear()
    kl=0
    main()
frame2_button2 = Button(frame2, text="Change Pattern", fg='black', bg='wheat', font=("Baskerville Old Face", 24, "bold"),command=reset)
frame2_button2.place(x=620, y=330)

main()

def selecti():
    f,g = 100,100
    global f5ilt
    ilt = filedialog.askopenfilenames(filetypes=(('PNG','*.png'),('JPEG','*.jpeg'),('MTS','*.mts')))
    f5ilt = list(ilt)[:9]
    while(len(ilt)<9):
        messagebox.showinfo('Select More','You have selected only '+str(len(ilt))+' images,\n Select '+str(9-len(ilt))+' more')
        ilt = ilt+tuple(filedialog.askopenfilenames(filetypes=(('PNG','*.png'),('JPEG','*.jpeg'),('MTS','*.mts'))))
        f5ilt = list(ilt)[:9]
    with open('imaglist.txt','w') as fp:
        td = f5ilt[0]
        for i in f5ilt[1:]:
            td=td+'\n'+i
        fp.write(fr.encrypt(td.encode()).decode())
    place()
    show_frame(frame1)


def proceed():
    if f4var==1:
        with open('nothing.txt','w') as no:
            no.write('Do not Delete This File...')
        place()
        show_frame(frame1)
        return
    elif f4var==2:
        show_frame(frame5)
        selecti()
    else:
        messagebox.showerror('No Option Selected','Select any Option to Proceed')

def f4rb1():
    global f4var
    f4var = 1
def f4rb2():
    global f4var
    f4var = 2


f4b1 = Radiobutton(frame4, text='Use the Default Images Provided',font=('calibri',20),variable=v4,value=1,command=f4rb1)
f4b2 = Radiobutton(frame4, text='Manually select the images from My Images *(1:1 recommended)',font=('calibri',20),variable=v4,value=2,command=f4rb2)
f4b3 = Button(frame4, text='PROCEED', font=('algerian', 24, 'bold'), command=proceed, bg='orange')


f4l1.place(x=100,y=100)
f4b1.place(x=370,y=300)
f4b2.place(x=370,y=370)
f4b3.place(x=480,y=520)


if os.path.exists('nothing.txt') or os.path.exists('imaglist.txt'):
    show_frame(frame1)
else:
    show_frame(frame4)
win.mainloop()
