import csv
import tkinter
import time
import datetime
from tkinter import *
from tkinter import messagebox
import uuid
l=[["unique ID","name","phone number","email","institutuin/company","time of entry"]]
k=open("stud1.csv","x")
with open("stud1.csv",'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(l)
def clicked():
    
   
    a=entry1.get()
    b=entry2.get()
    c=entry3.get()
    d=entry4.get()
    e=datetime.datetime.now()
    l.append([uuid.uuid1(),a,b,c,d,e])
    with open("stud1.csv",'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(l)
    k.close()
    
   
    
def search():
    s=entry5.get()
    for i in l:
        for j in i:
            if(j==s):
                messagebox.showinfo("congrats","match found")
            else:
                pass
    
window=tkinter.Tk()
window.title("Murugesa")
window.geometry("500x500")
lbl1=Label(window,text="registeration database",fg="red")
lbl1.grid(column=0,row=0)
lbl2=Label(window,text="name",fg="green")
lbl2.grid(column=2,row=2)
entry1=Entry(window)
entry1.grid(column=2,row=3)
lbl3=Label(window,text="phone number",fg="green")
lbl3.grid(column=2,row=4)
entry2=Entry(window)
entry2.grid(column=2,row=5)
lbl4=Label(window,text="email",fg="green")
lbl4.grid(column=2,row=6)
entry3=Entry(window)
entry3.grid(column=2,row=7)
lbl5=Label(window,text="institution/company",fg="green")
lbl5.grid(column=2,row=8)
entry4=Entry(window)
entry4.grid(column=2,row=9)
lbl6=Label(window,text="type the word to search",fg="green")
lbl6.grid(column=2,row=10)
entry5=Entry(window)
entry5.grid(column=2,row=11)
btn1=Button(window,text="search",command=search)
btn1.grid(column=2,row=12)
btn1=Button(window,text="submit",command=clicked)
btn1.grid(column=2,row=13)
window.mainloop()
