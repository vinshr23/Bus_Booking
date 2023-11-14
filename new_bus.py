from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,padx=w//2.5)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0)
Label(frame1,text="Add Bus Details",bg='white',fg='green4',font=('Allice',15)).grid(row=2,column=0)

frame2=Frame(root)
frame2.grid(row=5,column=0)

Label(frame2,text="Bus Id:",font=('Allice',10)).grid(row=5,column=0)
bus_id=Entry(frame2)
bus_id.grid(row=5,column=1)

Label(frame2,text="Bus Type:",font=('Allice',10)).grid(row=5,column=2)
bus_type=StringVar()
Option=["AC 2x2","AC 3x2","NON AC 2x2", "NON AC 3x2","AC SLEEPER 2x1","NON AC SLEEPER 2x1"]
bus_type.set("select bus")
OptionMenu(frame2,bus_type,*Option).grid(row=5,column=3)

Label(frame2,text="Capacity:",font=('Allice',10)).grid(row=5,column=4)
capacity=Entry(frame2)
capacity.grid(row=5,column=5)

Label(frame2,text="Fair:",font=('Allice',10)).grid(row=5,column=6)
Fair=Entry(frame2)
Fair.grid(row=5,column=7)

Label(frame2,text="Operator Id:",font=('Allice',10)).grid(row=5,column=8)
op_id=Entry(frame2)
op_id.grid(row=5,column=9)

Label(frame2,text="Operator name:",font=('Allice',10)).grid(row=5,column=10)
name=Entry(frame2)
name.grid(row=5,column=11)


Label(frame2,text="Route Id:",font=('Allice',10)).grid(row=5,column=12)
rt_id=Entry(frame2)
rt_id.grid(row=5,column=13)

def success():
    if bus_id.get()=='':
        showinfo('empty','Please enter bus id')
    elif capacity.get()=='':
        showinfo('empty','Please enter capacity')
    elif name.get()=='':
        showinfo('empty','Please enter name')
    elif bus_type.get()=='select bus':
        showinfo('empty','Please select bus type')
    elif Fair.get()=='':
        showinfo('empty','Please enter fair')
    elif op_id.get()=='':
        showinfo('empty','Please enter operator id')
    elif rt_id.get()=='':
        showinfo('empty','Please enter route id')
    else:
        import sqlite3
        con=sqlite3.Connection('bus_reservation_211b349')
        cur=con.cursor()
        cur.execute('insert into bus_details(BID,Bus_type,Op_name,operator_id,route_id,seat_capacity,fare)values(?,?,?,?,?,?,?)',(bus_id.get(),bus_type.get(),name.get(),op_id.get(),rt_id.get(),capacity.get(),Fair.get()))
        con.commit()
        cur.execute('select * from bus_details where BID=?',(bus_id.get(),))
        res=cur.fetchall()
        Label(frame2,text="BUS ADDED-   "+res[0][0]+"     "+res[0][1]+"     " +res[0][2]+"     " +res[0][3]+"     " +res[0][4]+"     "+str(res[0][5])+"     "+str(res[0][6]),font='calibri 15 bold',fg='blue').grid(row=7,column=2,columnspan=11)

def menu():
    root.destroy()
    import menu
       
Button(frame2,text="Add Bus",bg='light green',command=success,fg='black',font=('Allice',10)).grid(row=10,column=6)
Button(frame2,text="Edit Bus",bg='light green',fg='black',font=('Allice',10)).grid(row=10,column=7)
home=PhotoImage(file='.\\home.png')
Button(frame2,image=home,command=menu).grid(row=10,column=8)
