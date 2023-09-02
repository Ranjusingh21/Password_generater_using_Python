from tkinter import *
import string
import random
window=Tk()


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    number=string.digits
    special_charecters=string.punctuation
    all=small_alphabets+capital_alphabets+number+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passField.insert(0,random.sample(small_alphabets,password_length))
        
    if choice.get()==2:
        passField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))
        
    if choice.get()==3:
        passField.insert(0,random.sample(all,password_length))

    
    
    #password=random.sample(all,password_length)
    #passField.insert(0,password)
def copy():
    random_password=passField.get()
    pyperclip.copy(random_password)


window.config(bg='pink')
choice=IntVar()
Font=('arial',13,'bold')
passlabel=Label(window,text="Password Generator",
                font=('times new roman', 20 ,'bold'),bg="pink",fg='green')
passlabel.grid()

weakRadio=Radiobutton(window,text='Weak',value=1,variable=choice,font=Font)
weakRadio.grid(pady=10)

MediumRadio=Radiobutton(window,text='Medium',value=2,variable=choice,font=Font)
MediumRadio.grid(pady=7)

StrongRadio=Radiobutton(window,text='Strong',value=3,variable=choice,font=Font)
StrongRadio.grid(pady=7)

Lengthlabel=Label(window,text="Password Length",font=Font,bg="pink",fg='green')
Lengthlabel.grid(pady=7)

length_Box=Spinbox(window,width=5,from_=5,to_=18,font=Font)
length_Box.grid(pady=7)
                                                        #funtion creation
generatorButton=Button(window,text='Generate',font=Font,command=generator)
generatorButton.grid(pady=7)

passField=Entry(window,width=25,bd=2,font=Font)
passField.grid()

CopyButton=Button(window,text='Copy',font=Font,command=copy)
CopyButton.grid(pady=7)


window.mainloop()
