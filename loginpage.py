from tkinter import *
root=Tk()
root.geometry("600x300")

def getvals():
    print("Acceped")

Label(root, text="Python Regsitration Form", font="arial 15 bold").grid(row=0, column=3)

name=Label(root, text="name")
phone=Label(root, text="phone")
gender=Label(root, text="gemder")
pymentmode=Label(root, text="payment mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
pymentmode.grid(row=4,column=2)

namevalue= StringVar
phonevalue=StringVar
gendervalue=StringVar
pymentmodevalue=StringVar
checkvalue = IntVar
 
nameentery =Entry(root, textvariable=namevalue)
phoneentery =Entry(root, textvariable=phonevalue)
genderentery =Entry(root, textvariable=gendervalue)
pymentmodeentery =Entry(root, textvariable=pymentmodevalue)

nameentery.grid(row=1,column=3)
phoneentery.grid(row=2,column=3)
genderentery.grid(row=3,column=3)
pymentmodeentery.grid(row=4,column=3)

Checkbutton= Checkbutton(text="remember me?", variable=checkvalue)
Checkbutton.grid(row=5, column=3)

Button(text="Submit", command=getvals).grid(row=6, column=3)

root.mainloop()
