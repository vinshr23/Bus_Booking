from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,columnspan=11,padx=w//2.7)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0,columnspan=11,pady=10)
Label(frame1,text="Add Bus Operator Details",bg='white',fg='green4',font=('Allice',15)).grid(row=2,column=0,columnspan=11,pady=10)

frame2=Frame(root)
frame2.grid(row=3,column=0)

Label(frame2,text="Operator Id:").grid(row=3,column=0)
idd=Entry(frame2)
idd.grid(row=3,column=1)

Label(frame2,text="Name:").grid(row=3,column=2)
name=Entry(frame2)
name.grid(row=3,column=3)

Label(frame2,text="Address:").grid(row=3,column=4)
add=Entry(frame2)
add.grid(row=3,column=5)

Label(frame2,text="Phone:").grid(row=3,column=6)
phno=Entry(frame2)
phno.grid(row=3,column=7)

Label(frame2,text="Email:").grid(row=3,column=8)
email=Entry(frame2)
email.grid(row=3,column=9)



def add_operator():
    if idd.get()=='':
        showerror('empty','please enter operator id')
    elif name.get()=='':
        showerror('empty','please enter operator name')
    elif add.get()=='':
        showerror('empty','please enter operator address')
    elif email.get()=='':
        showerror('empty','''please enter operator's email''')
    elif len(phno.get())!=10:
        showerror('invalid mobile','please enter 10 digit mobile number')
    else:
        import sqlite3
        con=sqlite3.Connection('bus_reservation_211b349')
        cur=con.cursor()
        cur.execute('insert into Operator_details(operator_name,OID,address,phone_number,Email)values(?,?,?,?,?)',(name.get(),idd.get(),add.get(),phno.get(),email.get()))
        con.commit()
        cur.execute('select * from Operator_details where OID=?',(idd.get(),))
        res=cur.fetchall()
        Label(frame2,text=res[0][0]+"     "+str(res[0][1])+"     " +res[0][2]+"     " +str(res[0][3])+"     " +res[0][4],font='calibri 15 bold').grid(row=6,column=0,columnspan=11)
        
Button(frame2,text="Add",bg='light green',fg='black',font=('Allice',10),width=8,command=add_operator).grid(row=3,column=10,padx=5)
Button(frame2,text="Edit",bg='light green',fg='black',font=('Allice',10),width=8).grid(row=3,column=11,padx=5)

def menu():
    root.destroy()
    import menu

home=PhotoImage(file='.\\home.png')
Button(frame2,image=home,command=menu).grid(row=5,column=11,pady=8)
root.mainloop()

