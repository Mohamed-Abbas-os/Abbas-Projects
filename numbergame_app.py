from tkinter import *
import random
root=Tk()
root.title('NUMBER GUESSING GAME')
root.geometry('300x300')
root.config(background='lightgreen')
num=random.randint(1,100)
label=Label(root,text='NUMBER GUESSING GAME',fg='blue',bg='lightblue',width=25,height=2,font=('Arial,8'))
label.place(x=35,y=10)
def click():
    try:
        guess=int(enter.get())
        if guess==num:
            label3=Label(root,text=f"'{num}' you guessed correctly",fg='white',bg='green')
            label3.place(x=90,y=170)
            root.after(1000,lambda:label3.place_forget())
        elif guess>num:
            label4=Label(root,text='too high',fg='white',bg='red')
            label4.place(x=120,y=170)
            root.after(1000,lambda:label4.place_forget())
        elif guess<num:
            label5=Label(root,text='too low',fg='white',bg='red')
            label5.place(x=125,y=170)
            root.after(1000,lambda:label5.place_forget())
    except ValueError:
        label6=Label(root,text='Enter valid number',fg='white',bg='red')
        label6.place(x=90,y=170)
        root.after(1000,lambda:label6.place_forget())
    enter.delete(0,END)
label1=Label(root,text='Enter your guessed number (1 to 100)!',bg='lightblue')
label1.place(x=60,y=60)
label2=Label(root,text='Enter :',fg='white',bg='red')
label2.place(x=55,y=90)
enter=Entry(root)
enter.place(x=110,y=90)
Ebutt=Button(root,text='Enter',bg='green',activebackground='red',fg='white',command=click).place(x=130,y=120)
root.mainloop()