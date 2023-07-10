#import module from tkinter for UI
from tkinter import *
import tkinter as tk
from playsound import playsound
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py dataset_capture.py")
    
def function2():
    
    os.system("py training_dataSet.py")

def function3():

    os.system("py recognizer.py")

def function7():
    os.system("py automail.py")
    


   
def function6():

    root.destroy()

def attend():
    os.startfile("firebase\attendance_files"+str(datetime.now().date())+'.xls')
    
root.configure(background='black')

#stting title for the window
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")

#creating a text label
lbl2=Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="black",height=2)
lbl2.grid(row=1,columnspan=4,sticky=W+E+N+S,padx=5,pady=5)


#creating first button
bt1=tk.Button(root,text="Create Dataset",font=("times new roman",20),bg="green",fg='white',command=function1)
bt1.grid(row=3,columnspan=4,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
bt2=tk.Button(root,text="Train Dataset",font=("times new roman",20),bg="green",fg='white',command=function2)
bt2.grid(row=4,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
#creating third button
bt3=tk.Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="green",fg="white",command=function3)
bt3.grid(row=5,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
#creating attendance button
bt4=tk.Button(root,text="Attendance Sheet",font=('times new roman',20),bg="green",fg="white",command=attend)
bt4.grid(row=6,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)
#Button(root,text="Developers",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
bt6=tk.Button(root,text="Send Mail",font=('times new roman',20),bg="green",fg="white",command=function7)
bt6.grid(row=8,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)

bt5=tk.Button(root,text="Exit",font=('times new roman',20),bg="red",fg="white",command=function6)
bt5.grid(row=9,columnspan=4,sticky=N+E+W+S,padx=5,pady=5)



root.mainloop()
