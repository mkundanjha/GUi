from tkinter import *
from datetime import date
window=Tk()
window.configure(background='white')

today=date.today()



window.geometry("320x480")
window.resizable(0,0)
window.title("To-do List")
name=StringVar()
cost_var=StringVar()
check_box_list = []
def generate():
    k=name.get()
    if k!='':
        f = Frame(window,bg='#dee2de')
        Checkbutton(f,bg='#dee2de', var=StringVar(), text=k).pack(side='left',fill=X)
        Button(f, text='✕', command=f.destroy,bg='#dd2f2c').pack(side='right')
        check_box_list.append(f)  # add Frame
        f.pack(fill=X)
        name.set('')
  
def clear():
    for i in check_box_list:
        if i.winfo_exists():    # Checks if the widget exists or not
            i.destroy()  
            name.set('')

lbl=Label(window,text="Enter your Task").pack()
# To get the entry    
ent=Entry(window,width=10,bg='#b8b8bc',textvariable=name)
ent.pack(fill=X)

# Submit Button
btn1=Button(window,text="Submit", fg='white',bg='blue',command= generate)
btn1.pack(fill=X)

# Clear Button
btn2=Button(window,text="Clear All", fg='white',bg='#f44e42',command= clear)
btn2.pack(fill=X)
lbl3=Label(window,text=today,bg='#b5c0f4').pack(fill=X)
lbl3=Label(window,text="Today's Task:",bg='#414240',fg='white').pack(fill=X)


window.mainloop()
