from tkinter import *
import sqlite3
from tkinter.messagebox import*
root=Tk()

h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,padx=w//2.5)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=2,column=0)
Label(frame1,text="Enter Journey Detail",bg='light green',fg='black',font=('Allice',10)).grid(row=3,column=0,pady=5)

frame2=Frame(root)
frame2.grid(row=4,column=0)

Label(frame2,text="To:",font=('Allice',10)).grid(row=4,column=0,stick=E)
to=Entry(frame2)
to.grid(row=4,column=1)

Label(frame2,text="From:",font=('Allice',10)).grid(row=4,column=2,stick=E)
From=Entry(frame2)
From.grid(row=4,column=3)

Label(frame2,text="Journey Date(YYYY-MM-DD):",font=('Allice',10)).grid(row=4,column=4,stick=E)
date=Entry(frame2)
date.grid(row=4,column=5)
bus_select=StringVar()
bus_select.set(None)
booked_bus_id=""
Name=""
Age=""
Gender=""
Seats=""
Mobile=""
Fare=0



def pass_detail():
    booked_bus_id=bus_select.get()

    if booked_bus_id=='None':
        showwarning("Warning",'Please select a bus')
    else:
        frame3=Frame(root)
        frame3.grid(row=27,column=0)
        Label(frame3,text="Fill Passenger Details To Book The Bus Ticket",bg='light blue',fg='red',font=('Allice',25)).grid(row=27,column=0,columnspan=10,pady=20,padx=10)
        Label(frame3,text="Name:",font=('Allice',10)).grid(row=28,column=0,stick=E)
        namee=Entry(frame3)
        namee.grid(row=28,column=1)
        Label(frame3,text="Gender:",font=('Allice',10)).grid(row=28,column=2,stick=E,padx=5)


        genderr=StringVar()
        genderr.set('Male')
        Option=['Male','Female','other']
        menu=OptionMenu(frame3,genderr,*Option)
        menu.grid(row=28,column=3)

        Label(frame3,text="No of seats:",font=('Allice',10)).grid(row=28,column=4,stick=E,padx=5)
        seatss=Entry(frame3)
        seatss.grid(row=28,column=5)

        Label(frame3,text="Mobile no:",font=('Allice',10)).grid(row=28,column=6,stick=E,padx=5)
        mobile_noo=Entry(frame3)
        mobile_noo.grid(row=28,column=7)

        Label(frame3,text="Age:",font=('Allice',10)).grid(row=28,column=8,stick=E,padx=5)
        agee=Entry(frame3)
        agee.grid(row=28,column=9)

        
        con=sqlite3.connect('bus_reservation_211b349')
        cur=con.cursor()

        cur.execute('''select fare from bus_details where BID=?''',[booked_bus_id])
        Fare=cur.fetchone()
        fare=int(Fare[0])
        con.commit()
        con.close()

        def confirm():
            if len(namee.get())==0:
                showerror('empty','please enter name')
            elif int(seatss.get())>40:
                showerror('seats unavailable','you cannot book number of seats more then available seats')
            elif len(mobile_noo.get())!=10:
                showerror('invalid number','please enter 10 digit mobile number')
           
            elif int(agee.get())>200:
                showerror('very old','older then 200 years not possible')
            else:
                n=int(seatss.get())
                tf=n*fare
                tf=str(tf)
                answer = askyesno("Booking Confirmation", "Are you sure you want to book the bus?\n Total Amount to be paid is Rs "+tf)
                if answer:
                    name=namee.get()
                    age=agee.get()
                    nos=seatss.get()
                    mob=mobile_noo.get()
                    gender=genderr.get()
                    T_date=date.get()
                    con=sqlite3.connect('bus_reservation_211b349')
                    cur=con.cursor()
                    cur.execute('''select count(*)+1 from booking_history''')
                    a=cur.fetchone()
                    count=a[0]
                    cur.execute('''insert into booking_history (pname,gender,age,mobile,bus,travelling_date,booking_date,no_of_seats,total_fare,booking_ref_number) values (?,?,?,?,?,?,DATE(),?,?,?)''',(name,gender,age,mob,booked_bus_id,T_date,nos,tf,count))

                    cur.execute('''update running_details set seat_available=seat_available-? where RBID=? and running_date=?''',(nos,booked_bus_id,T_date))

                    con.commit()
                    con.close()

                    root.destroy()
                    import ticket
                
        

    

    

    Button(frame3,text="Book Seat",bg='light green',command=confirm,fg='black',font=('Allice',10)).grid(row=28,column=10)


def show_bus():
    import sqlite3
    con=sqlite3.Connection("bus_reservation_211b349")
    cur=con.cursor()
    To=to.get()
    Fromm=From.get()
    jdate=date.get()
    cur.execute('''select op_name,bus_type,seat_available,seat_capacity,fare,BID from bus_details,running_details,route_details as f, route_details as t where f.station_name=? and t.station_name=? and running_date=? and RBID=BID and f.SID<t.SID and f.RID=route_id and t.RID=route_id''',(To,Fromm,jdate))
    res=cur.fetchall()
    
    Label(frame2,text="Select Bus",fg='green',font=('Allice',10)).grid(row=5,column=1)
    Label(frame2,text="Operator",fg='green',font=('Allice',10)).grid(row=5,column=2)
    Label(frame2,text="Bus Type",fg='green',font=('Allice',10)).grid(row=5,column=3)
    Label(frame2,text="Available/Capacity",fg='green',font=('Allice',10)).grid(row=5,column=4)
    Label(frame2,text="Fare",fg='green',font=('Allice',10)).grid(row=5,column=5)
    loc=7
    bus=1
    for i in res:
        r1=Radiobutton(frame2,text='Bus'+str(bus),font='calibri 12 bold',bg='light blue',variable=bus_select,value=i[5],indicator=0)
        r1.grid(row=loc,column=1)
        Label(frame2,text=i[0],fg='green',font=('Allice',10)).grid(row=loc,column=2)
        Label(frame2,text=i[1],fg='green',font=('Allice',10)).grid(row=loc,column=3)
        Label(frame2,text=str(i[2])+"/"+str(i[3]),fg='green',font=('Allice',10)).grid(row=loc,column=4)
        Label(frame2,text=i[4],fg='green',font=('Allice',10)).grid(row=loc,column=5)
        Button(frame2,text="Proceed to Book",bg='light green',fg='black',font=('Allice',10),command=pass_detail).grid(row=loc,column=6)
        loc=loc+1
        bus=bus+1
    con.commit()
    con.close()

Button(frame2,text="Show bus",font=('Allice',10),bg='light green',command=show_bus,fg='black').grid(row=4,column=6)

def home():
    root.destroy()
    import menu



root.mainloop()
