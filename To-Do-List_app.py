from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title('To-Do-list App')
root.geometry('400x400')
root.resizable(False,False)
bg_image=Image.open('bgimage.png')
bg_photo=ImageTk.PhotoImage(bg_image)
bg_layout=Label(root,image=bg_photo)
bg_layout.place(x=0,y=0,relwidth=1,relheight=1)
def add_task():
    w1=Toplevel(root)
    w1.title('Add task')
    w1.geometry('200x200')
    enter=Entry(w1)
    enter.pack()
    def saved():
        data=enter.get()
        isfilled=bool(enter.get().strip())
        if isfilled:
             with open('task_file.txt','a') as file:
                file.write('Your task'+'\n')
                file.write(str(data)+'\n')
             enter.delete(0,END)
             label1=Label(w1,text='Saved succesfully')
             label1.pack(padx=10,pady=5)
        else:
            label3=Label(w1,text='Please enter something!')
            label3.pack(padx=10,pady=5)
    but=Button(w1,text='Save',fg='blue',activebackground='green',command=saved)
    but.pack(padx=10,pady=10)
def view_task():
    w2=Toplevel(root)
    w2.title('View task')
    w2.geometry('200x200')
    with open('task_file.txt','r') as file1:
        a=file1.read()
    label2=Label(w2,text=a)
    label2.pack()
def delete_task():
    with open('task_file.txt','r') as file2:
        lines=file2.readlines()
        lines=lines[:-2]
    with open('task_file.txt','w') as file3:
        file3.writelines(lines)
    label_del1=Label(root,text=' your last task was deleted!',bg='lightgreen',fg='black')
    label_del1.place(x=120,y=280)
    label.after(1500,lambda:label_del1.place_forget())
def about_us():
    w3=Toplevel(root)
    w3.title('ABOUT US')
    w3.geometry('300x300')
    label6=Label(w3,text='Thank you for using this app ! ,This App is made by Mohamed Abbas.This App is made for purpose of learning PYTHON programming',font=('Arial,3'),wraplength=300)
    label6.pack()
label=Label(root,text='To-Do-list App',font=('Arial',15),fg='blue',bg='black')
label.pack(padx=15,pady=10)
add=Button(root,text='Add Task',command=add_task,activebackground='green',bg='#ADD8E6')
add.pack(padx=10,pady=15)
view=Button(root,text='View Task',command=view_task,activebackground='green',bg='#ADD8E6')
view.pack(padx=10,pady=15)
delete=Button(root,text='Delete Task',command=delete_task,activebackground='green',bg='#ADD8E6')
delete.pack(padx=10,pady=15)
about=Button(root,text='i',font=('Arial',8),bg='red',fg='white',activebackground='green',command=about_us)
about.place(x=10,y=10)
root.mainloop()