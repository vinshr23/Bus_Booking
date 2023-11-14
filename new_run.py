from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,columnspan=7,padx=w//2.5)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0,columnspan=7)
Label(frame1,text="Add Bus Running Details",bg='white',fg='green4',font=('Allice',15)).grid(row=2,column=0,columnspan=7,pady=25)

frame2=Frame(root)
frame2.grid(row=3,column=0)
Label(frame2,text="Bus Id:",font=('Allice',10)).grid(row=3,column=0,stick=E)
bus_id=Entry(frame2)
bus_id.grid(row=3,column=1)

Label(frame2,text="Running Date:",font=('Allice',10)).grid(row=3,column=2,stick=E)
date=Entry(frame2)
date.grid(row=3,column=3)

Label(frame2,text="Seat Available:",font=('Allice',10)).grid(row=3,column=4,stick=E)
seat=Entry(frame2)
seat.grid(row=3,column=5)

def run():
    if bus_id.get()=='':
        showerror('empty','Please enter bus id')
    elif date.get()=='':
        showerror('empty','Please enter date')
    elif seat.get()=='':
        showerror('empty','Please select seats')
    else:
        import sqlite3
        con=sqlite3.Connection('bus_reservation_211b349')
        cur=con.cursor()
        cur.execute('insert into running_details(RBID,running_date,seat_available)values(?,?,?)',(bus_id.get(),date.get(),seat.get()))
        con.commit()
        
        showinfo('ADDED','Run added sucessfuly')
        #Label(frame2,text="ROUTE DETAILS-  "+res[0][0]+"     "+(res[0][1])+"     " +str(res[0][2]),font='calibri 12 bold',fg='blue').grid(row=4,column=2,columnspan=5)
        


Button(frame2,text="Add Run",bg='light green',fg='black',font=('Allice',10),command=run).grid(row=3,column=6,padx=20)
Button(frame2,text="Delete Run",bg='light green',fg='black',font=('Allice',10)).grid(row=3,column=7)

def menu():
    root.destroy()
    import menu
home=PhotoImage(file='.\\home.png')
Button(frame2,image=home,command=menu).grid(row=4,column=7,pady=20,padx=30)
root.mainloop()
