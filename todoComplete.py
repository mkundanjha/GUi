from tkinter import *
from datetime import date
window=Tk()
window.configure(background='#879fdb')

today=date.today()
j=0
flag=1


window.geometry("340x540")
window.resizable(1,1)
window.title("To-do List")
name=StringVar()
cost_var=StringVar()
check_box_list = []
label_list=[]
def generate():
    k=name.get()
    global j
    if j<14:
        if k!='':
                j=j+1
                f = Frame(window,bg='#a7bfe5')
                Checkbutton(f,bg='#a7bfe5', var=StringVar(), text=" "+k).pack(side='left',fill=X)
                def sum():
                        f.destroy()
                        clearLabel()
                        global j
                        j=j-1
                Button(f, text='✕',fg='white', command=sum,bg='#dd2f2c').pack(side='right')
                check_box_list.append(f)  # add Frame
                f.pack(fill=X)
                name.set('')
    else:
            name.set('')
            global flag
            if flag:
                f=Frame(window,bg='#a7bfe5')
                l=Label(f,text="Sorry! Only 14 task allowed for now.").pack(fill=X)
                label_list.append(f)
                f.pack(fill=X)
                flag=0
def clearLabel():
        for w in label_list:
                w.forget()
        global flag
        flag=1

def clear():
        clearLabel()
        for i in check_box_list:
                if i.winfo_exists():    # Checks if the widget exists or not
                        i.destroy()  
                        name.set('')
      
       
        global j
        j=0

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
