from tkinter import *
from tkinter import messagebox
import pyttsx3
try:
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    if voices:
        engine.setProperty('voice',voices[0].id)
    else:
        raise RuntimeError('no tts voices found on this system.')
except Exception as e:
    messagebox.showerror('TTS setup failed',f'Text-to-Speech engine could not start:\n{e}')
    exit()
def speak():
    audio=text1.get('1.0','end-1c')
    if not audio:
        messagebox.showwarning('Empty Input','Please Enter some text to speak')
        return
    try:
        engine.setProperty('rate',170)
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror('Speech Error',f'Something went wrong:\n{e}')
def about_us():
    w3=Toplevel(root)
    w3.title('ABOUT US')
    w3.geometry('300x300')
    w3.resizable(False,False)
    label6=Label(w3,text='Thank you for using this app ! ,This App is made by Mohamed Abbas.This App is made for purpose of learning PYTHON programming',font=('Arial,3'),wraplength=300)
    label6.pack()
root=Tk()
root.title('TEXT TO SPEECH')
root.iconbitmap(r'favicon.ico')
root.geometry('350x350')
root.config(background='lightblue')
root.resizable(False,False)
about=Button(root,text='i',font=('Arial',8),bg='red',fg='white',activebackground='green',command=about_us)
about.place(x=10,y=10)
label=Label(root,text='TEXT  TO  SPEECH  ENGINE',fg='white',bg='green')
label.pack(pady=10)
text1=Text(root,width=25,height=3)
text1.place(x=100,y=80)
label1=Label(root,text='Enter text:',bg='lightblue').place(x=40,y=93)
submit=Button(root,text='speak',bg='blue',fg='white',activebackground='green',command=speak)
submit.place(x=150,y=160)
root.mainloop()