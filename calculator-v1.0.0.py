try:
    from tkinter import *
    from tkinter import messagebox
    root=Tk()
    root.title('Calculator')
    root.geometry('255x360')
    root.resizable(False,False)
    root.iconbitmap(r'calculator.ico.ico')
    root.config(background='darkgreen')
    def entry(num):
        current=enter1.get()
        enter1.delete(0,END)
        enter1.insert(0,str(current)+str(num))
    def add():  
        try:
            global d
            global op
            if enter.get()=='':
                a=enter1.get()
                num1=enter.insert(END,str(a))
                d=enter.get()
                enter.insert(END,'  +')
            else:
                s=enter.get()
                n=s[:-1]
                a=enter1.get()
                x=int(n)+int(a)
                enter.delete(0,END)
                num1=enter.insert(END,str(x))
                d=enter.get()
                enter.insert(END,'  +')
            op=enter.get()
            enter1.delete(0,END)
        except Exception:
            messagebox.showwarning('Error','Error occurred')
    def sub():
        try:
            global d
            global op
            if enter.get()=='':
                a=enter1.get()
                num1=enter.insert(END,str(a))
                d=enter.get()
                enter.insert(END,'  -')
            else:
                s=enter.get()
                n=s[:-1]
                a=enter1.get()
                x=int(n)-int(a)
                enter.delete(0,END)
                num1=enter.insert(END,str(x))
                d=enter.get()
                enter.insert(END,'  -')
            op=enter.get()
            enter1.delete(0,END)
        except Exception:
            messagebox.showwarning('Error','Error occurred')
    def multiple():
        try:
            global d
            global op
            if enter.get()=='':
                a=enter1.get()
                num1=enter.insert(END,str(a))
                d=enter.get()
                enter.insert(END,'  x')
            else:
                s=enter.get()
                n=s[:-1]
                a=enter1.get()
                x=int(n)*int(a)
                enter.delete(0,END)
                num1=enter.insert(END,str(x))
                d=enter.get()
                enter.insert(END,'  x')
            op=enter.get()
            enter1.delete(0,END)
        except Exception:
            messagebox.showwarning('Error','Error occurred')
    def divide():
        try:
            global d
            global op
            if enter.get()=='':
                a=enter1.get()
                num1=enter.insert(END,str(a))
                d=enter.get()
                enter.insert(END,'  /')
            else:
                s=enter.get()
                n=s[:-1]
                a=enter1.get()
                x=int(n)/int(a)
                enter.delete(0,END)
                num1=enter.insert(END,str(x))
                d=enter.get()
                enter.insert(END,'  /')
            op=enter.get()
            enter1.delete(0,END)
        except Exception:
            messagebox.showwarning('Error','Error occurred')
    def equal():
        b=enter1.get()
        enter.delete(0,END)
        enter1.delete(0,END)
        try:
            if op[-1]=='+':
                c=float(d)+float(b)
                enter1.insert(0,str(c))
            elif op[-1]=='-':
                c=float(d)-float(b)
                enter1.insert(0,str(c))
            elif op[-1]=='x':
                c=float(d)*float(b)
                enter1.insert(0,str(c))
            elif op[-1]=='/':
                c=float(d)/float(b)
                enter1.insert(0,str(c))
            else:
                return
        except ValueError:
            messagebox.showwarning('error','Please enter number')
            enter.delete(0,END)
            enter1.delete(0,END)
        except ZeroDivisionError:
            messagebox.showerror('Error',"Can't divide by zero ")
        except Exception:
            messagebox.showerror('Error','An Error occurred,Please restart program :err')
    def delete():
        enter.delete(0,END)
        enter1.delete(0,END)
    label=Label(root,text='',bg='darkgreen',width=30,height=3)
    label.grid(row=0,column=0,columnspan=3,pady=5)
    enter=Entry(root,width=30)
    enter1=Entry(root,width=30)
    enter.place(x=35,y=9)
    enter1.place(x=35,y=30)
    button1=Button(root,text='9',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(9))
    button2=Button(root,text='8',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(8))
    button3=Button(root,text='7',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(7))
    button4=Button(root,text='6',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(6))
    button5=Button(root,text='5',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(5))
    button6=Button(root,text='4',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(4))
    button7=Button(root,text='3',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(3))
    button8=Button(root,text='2',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(2))
    button9=Button(root,text='1',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(1))
    button10=Button(root,text='0',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=lambda:entry(0))
    button11=Button(root,text='AC',bg='red',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=delete)
    button12=Button(root,text='+',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=add)
    button13=Button(root,text='-',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=sub)
    button14=Button(root,text='x',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=multiple)
    button15=Button(root,text='/',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=10,height=2,command=divide)
    button16=Button(root,text=' = ',bg='lightblue',activebackground='#2c3e50',activeforeground='white',width=20,height=2,command=equal)
    button1.grid(row=2,column=0,padx=3,pady=2)
    button2.grid(row=2,column=1,padx=3,pady=5)
    button3.grid(row=2,column=2,padx=3,pady=5)
    button4.grid(row=3,column=0,padx=3,pady=5)
    button5.grid(row=3,column=1,padx=3,pady=5)
    button6.grid(row=3,column=2,padx=3,pady=5)
    button7.grid(row=4,column=0,padx=3,pady=5)
    button8.grid(row=4,column=1,padx=3,pady=5)
    button9.grid(row=4,column=2,padx=3,pady=5)
    button10.grid(row=5,column=0,padx=3,pady=5)
    button11.grid(row=6,column=2,padx=3,pady=5)
    button12.grid(row=5,column=1,padx=3,pady=5)
    button13.grid(row=5,column=2,padx=3,pady=5)
    button14.grid(row=6,column=0,padx=3,pady=5)
    button15.grid(row=6,column=1,padx=3,pady=5)
    button16.grid(row=7,column=0,columnspan=3)
    root.mainloop()
except Exception:
    messagebox.showerror('Error','An Error occurred,Please restart program')