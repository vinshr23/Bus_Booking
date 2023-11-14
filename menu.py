from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=3,pady=10,padx=(w//2.5))

Label(root,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=2,column=0,columnspan=3,pady=20)

def seat_booking():
    root.destroy()
    import seat_booking
Button(root,text='Seat Booking',bg='light green',fg='black',font=('Allice',15),command=seat_booking).grid(row=4,column=0,padx=20)
def booked_seat():
    root.destroy()
    import check_booked_seat
Button(root,text='Check Booked Seat',bg='light green',fg='black',font=('Allice',15),command=booked_seat).grid(row=4,column=1,padx=20)
def bus_detail():
    root.destroy()
    import add_bus_detail
Button(root,text='Add Bus Details',bg='light green',fg='black',font=('Allice',15),command=bus_detail).grid(row=4,column=2,padx=20)

Label(root,text="For Admin Only",fg='red').grid(row=5,column=2,pady=20)

#root.attributes('-fullscreen', True)
root.mainloop()
