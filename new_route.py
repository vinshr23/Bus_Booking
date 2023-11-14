
from tkinter import *
from tkinter.messagebox import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

frame1=Frame(root)
frame1.grid(row=0,column=0)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=0,column=0,padx=w//2.7)
Label(frame1,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0)
Label(frame1,text="Add Bus Route Details",bg='white',fg='green4',font=('Allice',15)).grid(row=2,column=0)

frame2=Frame(root)
frame2.grid(row=3,column=0)
Label(frame2,text="Route Id:",font=('Allice',10)).grid(row=3,column=0)
route_id=Entry(frame2)
route_id.grid(row=3,column=1)

Label(frame2,text="Station Name:",font=('Allice',10)).grid(row=3,column=2)
st_name=Entry(frame2)
st_name.grid(row=3,column=3)

Label(frame2,text="Station Id:",font=('Allice',10)).grid(row=3,column=4)
st_id=Entry(frame2)
st_id.grid(row=3,column=5)

def success():
    if route_id.get()=='':
        showerror('empty','Please enter route id')
    elif st_name.get()=='':
        showerror('empty','Please enter station name')
    elif st_id.get()=='':
        showerror('empty','Please select station id')
    else:
        import sqlite3
        con=sqlite3.Connection('bus_reservation_211b349')
        cur=con.cursor()
        cur.execute('insert into route_details(RID,station_name,SID)values(?,?,?)',(route_id.get(),st_name.get(),int(st_id.get())))
        con.commit()
        cur.execute('select * from route_details where RID=?',(route_id.get(),))
        res=cur.fetchall()
        showinfo('ADDED','Route added sucessfuly')
        Label(frame2,text="ROUTE DETAILS-  "+res[0][0]+"     "+(res[0][1])+"     " +str(res[0][2]),font='calibri 12 bold',fg='blue').grid(row=4,column=2,columnspan=5)
        
def delete():
    import sqlite3
    con=sqlite3.Connection('bus_reservation_211b349')
    cur=con.cursor()
    cur.execute('DELETE from route_details where RID=? and SID=?',(route_id.get(),int(st_id.get())))
    showinfo('DELETED','Route deleted sucessfuly')

Button(frame2,text="Add Route",command=success,bg='light green',fg='black').grid(row=3,column=6,padx=20)
Button(frame2,text="Delete Route",bg='light green',fg='black',command=delete).grid(row=3,column=7)
def menu():
    root.destroy()
    import menu
home=PhotoImage(file='.\\home.png')
Button(frame2,image=home,command=menu).grid(row=4,column=7,pady=20,padx=30)
root.mainloop()
