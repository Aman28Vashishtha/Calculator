from tkinter import *                            
import numpy as np                               
import math as m
import time

import serial


ser=serial.Serial('COM6',9600,timeout=1)
command ="robot forward"


if 'robot forward' in command:
    print(ser)
    ser.write('F'.encode())
    time.sleep(3)
    print(ser.readline().decode('ascii'))
    # ser.close()
    #speak("moving robot forward")

elif 'robot backward' in command:
    print(ser)
    ser.write('B'.encode())
    time.sleep(3)
    print(ser.readline().decode('ascii'))
    # ser.close()
    #speak("moving robot forward")
            
elif 'robot stop' in command:
    print(ser)
    ser.write('S'.encode())
    time.sleep(3)
    print(ser.readline().decode('ascii'))
    # ser.close()
    #speak("moving robot forward")

elif 'robot left' in command:
    print(ser)
    ser.write('L'.encode())
    time.sleep(3)
    print(ser.readline().decode('ascii'))
    # ser.close()
    #speak("moving robot forward")

elif 'robot right' in command:
    print(ser)
    ser.write('R'.encode())
    time.sleep(3)
    print(ser.readline().decode('ascii'))
    # ser.close()
    #speak("moving robot forward")



#    creating GUI window
root = Tk()
root.configure(background='black' )

#   fixing the size of window
root.geometry("450x565")
##root.maxsize(540,490)
##root.minsize(540,490)

#   tital/name of window
root.title("ROBOT MODULE")

#    creating labels
label=Label(text="",height=3,width=70,bg='black',font = ('arial', 18))
label.grid(row=2,column=6)

label1=Label(text="",height=3,width=70,bg='black',font = ('arial', 18))
label1.grid(row=1,column=6)

#    creating string variable
expresion=StringVar()
#    using set method to show text message in label2
expresion.set('ROBOT MODULE')

display = Label(textvariable = expresion, font=('arial', 18), bg='grey', fg='white', width=32 ).place(y = 45)
        
equ=''


heigh_0 = 2
width_0 = 10




#row3
if (ser.readline().decode('ascii')=='F'):
    button=Button(text="FORWARD",command=lambda:butpress(2),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
    button.grid(row=5,column=2)
else:
    button=Button(text="FORWARD",command=lambda:butpress(2),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
    button.grid(row=5,column=2)

#row4
button=Button(text="LEFT",command=lambda:butpress(4),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
button.grid(row=6,column=1)

button=Button(text="STOP",command=lambda:butpress(5),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
button.grid(row=6,column=2)

button=Button(text="RIGHT",command=lambda:butpress(6),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
button.grid(row=6,column=4)


#row5

button=Button(text="BACKWARD",command=lambda:butpress(8),height = heigh_0,width = width_0,bg='black',fg='white',relief='flat',font = ('arial', 18))
button.grid(row=7,column=2)






#    start the GUI
root.mainloop()
