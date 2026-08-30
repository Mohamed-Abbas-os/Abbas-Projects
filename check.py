import tkinter as tk
def click(button_text):
    if button_text=='=':
        try:
            result=str(eval(entry.get()))
            entry.delete(0,tk.END)
            entry.insert(0,'Error')
        except:
            entry.delete(0,tk.END)
            entry.insert(0,'error')
    elif button_text=='C':
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,button_text)
root=tk.Tk()
root.title('Calculator')
entry=tk.Entry(root,width=16,font='Arial',justify='right')
entry.grid(row=0,column=0,columnspan=4,pady=10)
buttons=[(('7'),( '8') ,( '9') ,( '/')),
         (('4'), ('5') , ('6') ,( '*')),
         (('1'), ('2') , ('3') ,( '-')),
         (('0'), ('.') ,( '=') ,( '+')),
         (('C'),)
         ]
for row_index,row in enumerate(buttons):
    for col_index,text in enumerate(buttons):
        button=tk.Button(root,text=text,width=5,height=2,font=('Arial',18),command=lambda txt=text:click(txt))
        button.grid(row=row_index+1,column=col_index,padx=5,pady=5)
root.mainloop()