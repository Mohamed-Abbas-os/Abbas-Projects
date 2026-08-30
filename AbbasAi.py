from tkinter import Tk,Button,Canvas
from turtle import RawTurtle
import random
class app():
    def __init__(self):
        self.appname="videos Hub"
        self.root=Tk()
        self.root.geometry('600x550')
        self.root.resizable('False','False')
        self.root.title('Videos Hub')
        self.root.config(background='black')
        self.button1=Button(self.root,text='START',bg='red',activebackground='green',command=self.nextpage)
        self.button1.place(x=300,y=200)
        self.root.mainloop()
    def nextpage(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
myapp=app()