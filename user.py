from tkinter import*
root=Tk()
root.title('user login')

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0,padx=w//2.7)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0)

Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0)

frame2=Frame(root)
frame2.grid(row=3,column=0)
Label(frame2,text='USERNAME:',font=('Allice',10),fg='black').grid(row=3,column=0,pady=40)
username=Entry(frame2)
username.grid(row=3,column=1)
Label(frame2,text='PASSWORD:',font=('Allice',10),fg='black').grid(row=4,column=0)
password=Entry(frame2)
password.grid(row=4,column=1)

def login():
    import sqlite3
    con=sqlite3.Connection("bus_reservation_211b349")
    cur=con.cursor()
    cur.execute('select * from user where password=?',(password.get(),))
    res=cur.fetchall()
    if len(res)!=0:
        root.destroy()
        import menu
    else:
        Label(root,text='user not exist please sign up').grid(row=3,column=0,columnspan=2)
        
def signup():
    root.destroy()
    import signup
    Label(root,text='SET USERNAME:',font=('Allice',10),fg='black').grid(row=4,column=0)
    un=Entry(root)
    un.grid(row=4,column=1)
    Label(root,text='SET PASSWORD:',font=('Allice',10),fg='black').grid(row=5,column=0)
    pas=Entry(root)
    pas.grid(row=5,column=1)
    
Button(frame2,text='Login',font=('Allice',10),bg='white',fg='black',command=login).grid(row=5,column=0,pady=10)
Button(frame2,text='SignUp',font=('Allice',10),bg='white',fg='black',command=signup).grid(row=5,column=1,pady=10)
root.mainloop()
