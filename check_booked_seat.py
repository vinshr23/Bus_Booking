from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,columnspan=3,padx=w//2.5,pady=20)

Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0,columnspan=3)
Label(frame1,text="Check Your Booking",bg='light green',fg='black').grid(row=2,column=0,columnspan=3,pady=10)

frame2=Frame(root)
frame2.grid(row=3,column=0)
Label(frame2,text="Enter Your Mobile No:",font=('Allice',10)).grid(row=3,column=0,stick=E)
mob_no=Entry(frame2)
mob_no.grid(row=3,column=1)

def history():
    if len(mob_no.get())!=10:
        showerror('invalid mobile','please enter 10 digit mobile number')
    else:    
        import sqlite3
        con=sqlite3.Connection('bus_reservation_211b349')
        cur=con.cursor()
        mob=int(mob_no.get())
        cur.execute('select * from booking_history where mobile=?',(mob,))
        res=cur.fetchall()
        k=len(res)
        Label(root,text=res).grid(row=10,column=0)
        Label(root,text=str(k)).grid(row=11,column=0)
        if len(res)!=0:
            cur.execute('select station_name from booking_history,bus_details,route_details where bus=BID and route_id=RID and mobile=? order by SID ',(mob,))
            bording_point=cur.fetchall()
            cur.execute('select station_name from booking_history,bus_details,route_details where bus=BID and route_id=RID and mobile=? order by SID desc',(mob,))
            destination_point=cur.fetchall()
                
            name=res[0][0]
            gend=res[0][1]
            age=res[0][2]
            phone=res[0][3]
            date=res[0][5]
            seats=res[0][7]
            fare=res[0][8]
            refno=res[0][9]
            bp=bording_point[0][0]
            dp=destination_point[0][0]
                
            fr=Frame(root,relief='groove',bd=5)
            fr.grid(row=4,column=0)
            Label(fr,text='Passengers: '+name,font='calibri 14 bold').grid(row=4,column=0)
            Label(fr,text='Gender: '+gend,font='calibri 14 bold').grid(row=4,column=4)
            Label(fr,text='Phone: '+str(phone),font='calibri 14 bold').grid(row=5,column=4)
            Label(fr,text='Fare RS: '+str(fare),font='calibri 14 bold').grid(row=6,column=4)
            Label(fr,text='Boarding Point: '+bp,font='calibri 14 bold').grid(row=8,column=4)
            Label(fr,text='No of seats: '+str(seats),font='calibri 14 bold').grid(row=5,column=0)
            Label(fr,text='Age: '+str(age),font='calibri 14 bold').grid(row=6,column=0)
            Label(fr,text='Booking Ref: '+str(refno),font='calibri 14 bold').grid(row=7,column=0)
            Label(fr,text='Travel on: '+date,font='calibri 14 bold').grid(row=8,column=0)
            Label(fr,text='Destination point: '+dp,font='calibri 14 bold').grid(row=9,column=0)
                
            Label(fr,text='Total amount Rs '+str(fare)+'.00/- to be paid at the time of boarding the bus',font='calibri 12 italic').grid(row=10,column=0,columnspan=5)
        else:
            choice=askyesno('No record found','Do tou want to book the seat now')
            if choice==1:
                root.destroy()
                import seat_booking
                
    
Button(frame2,text="Check Booking",bg='peach puff',font=('Allice',10),command=history).grid(row=3,column=2,stick=W,padx=10)

root.mainloop()
