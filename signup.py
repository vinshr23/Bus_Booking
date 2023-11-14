from tkinter import*
root=Tk()
root.title('create account')
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0,padx=w//2.7)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0)

frame2=Frame(root)
frame2.grid(row=3,column=0)
Label(frame2,text='SET USERNAME:',font=('Allice',10),fg='black').grid(row=3,column=0,pady=40)
un=Entry(frame2)
un.grid(row=3,column=1)
Label(frame2,text='SET PASSWORD:',font=('Allice',10),fg='black').grid(row=4,column=0)
pas=Entry(frame2)
pas.grid(row=4,column=1)
def acct():
    import sqlite3
    con=sqlite3.Connection("bus_reservation_211b349")
    cur=con.cursor()
    cur.execute('insert into user(username,password) values (?,?)',(un.get(),pas.get()))
    con.commit()
    con.close()
    root.destroy()
    import user
Button(frame2,text='CREATE ACCOUNT',font=('Allice',10),bg='white',fg='black',command=acct).grid(row=5,column=0,columnspan=2,pady=10)

root.mainloop()
