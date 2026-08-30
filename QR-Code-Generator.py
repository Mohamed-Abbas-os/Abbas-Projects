from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
import datetime 
import qrcode
import requests
import os
try:
    __version__="1.0.0"
    Version_url='https://raw.githubusercontent.com/Mohamed-Abbas-os/App-update/main/version.txt'
    Update_url='https://github.com/Mohamed-Abbas-os/App-update/releases/download/v1.1.0/QR-Code-Generator.exe'
    def check_update():
        try:
            response=requests.get(Version_url)
            latest_version=response.text.strip()
            if latest_version>__version__:
                answer=messagebox.askyesno('Update Available',f'New version {latest_version} available.Want to Download?')
                if answer:
                    download_update()
            else:
                messagebox.showinfo('No update Available','Your version have the latest version')
        except Exception :
            messagebox.showerror('Error',f'Failed to update /connection problem/network error \n try again after some time')
    def download_update():
        try:
            response=requests.get(Update_url)
            with open('QR-Code-Generator.exe','wb') as f:
                f.write(response.content)
                messagebox.showinfo('update downloaded ')
        except Exception:
            messagebox.showerror('Error','could not download update')
    def save_img():
        data1=text1.get('1.0','end-1c')
        data2=name.get().strip()
        text1.delete('1.0',END)
        name.delete(0,END)
        if data1 and data2 is not None:
            if data1 and data2:
                content=qrcode.make(data1)
                content.save(f'{data2}.png')
                messagebox.showinfo('Success',f"QR-Code saved as {data2}.png")
            else:
                messagebox.showwarning('Error','Error,failed to create image')
        else:
            messagebox.showwarning('No Values','Text or image name is Empty')
    def make():
       global text1,name
       text1=Text(root,width=20,height=3)
       text1.place(x=130,y=160)
       enter=Label(root,text='Enter text: ',bg='turquoise').place(x=70,y=180)
       name=Entry(root,width=26)
       name.place(x=130,y=225)
       img1=Label(root,text='Image Name: ',bg='turquoise').place(x=50,y=225)
       save=Button(root,text='Save',bg='red',fg='white',activebackground='green',command=save_img).place(x=170,y=280)
    def win2():
        w2=Toplevel(root)
        w2.geometry('200x200')
        w2.resizable(False,False)
        info1=Label(w2,text='App name: QR-Code-Generator').place(x=10,y=10)
        info2=Label(w2,text='Version: v1.0.0').place(x=10,y=30)
        info3=Label(w2,text='purpose: Generates qr code').place(x=10,y=50)
    def menu_win():
        w1=Toplevel(root)
        w1.geometry('200x150')
        w1.resizable(False,False)
        w1.title('More Options')
        info=Button(w1,text=' App Info',bg='red',fg='white',activebackground='green',command=win2).pack(pady=10)
        update=Button(w1,text='Update Version!',bg='red',fg='white',activebackground='green',command=check_update).pack(pady=5)
    root=Tk()
    root.title('QR-Code-Generator')
    root.geometry('400x400')
    root.resizable(False,False)
    root.config(background='Turquoise')
    title=ttk.Label(root,text='QR-Code Generator',font=('verdana',12,'bold',),background='turquoise',foreground='darkgreen').place(x=115,y=30)
    style=ttk.Style()
    style.theme_use('clam')
    style.configure('TButton',background='lightgreen',foreground='red',font=Font(weight='bold'))
    style.map('TButton',background=[('active','blue')],foreground=[('active','white')])
    button1=ttk.Button(root,text='Make QR code',style='TButton',command=make).place(x=135,y=100)
    version_label=Label(root,text='version(v1.0.0)',background='cyan').place(x=150,y=370)
    menu=Button(root,text=' : ',activebackground='red',background='blue',fg='black',command=menu_win).place(x=10,y=10)
    root.mainloop()
except Exception as e:
   messagebox.showerror('Error ','Error occured:')