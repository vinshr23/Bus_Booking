from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=4,pady=5,padx=w//2.5)
def newop():
    root.destroy()
    import new_operator
def newbus():
    root.destroy()
    import new_bus
def newrt():
    root.destroy()
    import new_route
def newrun():
    root.destroy()
    import new_run

Label(root,text="Online Bus Booking system",bg='light blue',fg='red',font=('Allice',25)).grid(row=1,column=0,columnspan=4)
Label(root,text="Add New Details To Bus",bg='white',fg='green4').grid(row=2,column=0,columnspan=4,pady=10)
Button(root,text="New Operator",bg='green',font=('Allice',10),command=newop).grid(row=3,column=0)
Button(root,text="New Bus",bg='orange red',font=('Allice',10),command=newbus).grid(row=3,column=1)
Button(root,text="New Route",bg='steel blue',font=('Allice',10),command=newrt).grid(row=3,column=2)
Button(root,text="New Run",bg='pink4',font=('Allice',10),command=newrun).grid(row=3,column=3)
root.mainloop()
