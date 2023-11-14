from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))



Label(root,text="Fill Passenger Details To Book The Bus Ticket",bg='light blue',fg='red',font=('Allice',25)).grid(row=0,column=0,columnspan=10,padx=w//4.8,pady=65)
Label(root,text="Name:",font=('Allice',10)).grid(row=1,column=0)
name=Entry(root)
name.grid(row=1,column=1)
Label(root,text="Gender:",font=('Allice',10)).grid(row=1,column=2)


gender=StringVar()
gender.set('Male')
Option=['Male','Female']
menu=OptionMenu(root,gender,*Option)
menu.grid(row=1,column=3)

Label(root,text="No of seats:",font=('Allice',10)).grid(row=1,column=4)
seats=Entry(root)
seats.grid(row=1,column=5)

Label(root,text="Mobile no:",font=('Allice',10)).grid(row=1,column=6)
mobile_no=Entry(root)
mobile_no.grid(row=1,column=7)

Label(root,text="Age:",font=('Allice',10)).grid(row=1,column=8)
age=Entry(root)
age.grid(row=1,column=9)
def show():
    if name.get()=='':
        showerror('empty','Please enter name')
    elif seats.get()=='':
        showerror('empty','Please enter seats')
    elif mobile_no.get()=='':
        showerror('empty','Please enter mobile number')
    elif age.get()=='':
        showerror('empty','Please enter age')
    else:
        choice=askyesno('fare confirm','Total amopunt to be paid Rs.')
Button(root,text="Book Seat",bg='light green',command=show,fg='black',font=('Allice',10)).grid(row=1,column=10)
root.mainloop()
