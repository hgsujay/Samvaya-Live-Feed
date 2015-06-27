from Tkinter import *
import ttk
from ttk import *
import os
from socket import *


################################
def upd():
    host = ""
    port = 13002
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    print "Waiting to receive messages..."
    while True:
        root.update()
        (data, addr) = UDPSock.recvfrom(buf)
        print "Received message: " + data
        if data[0]=='c':        #if first 2 charecters of data is c1, then update c1_var
            if data[1]=='1':
                msg=data[2:]
                c1_var.set(msg)
#if first 2 charecters of data is c2, then update c2_var
        if data[0]=='c':
            if data[1]=='2':
                msg=data[2:]
                c2_var.set(msg)

        if data[0]=='c':
            if data[1]=='3':
                msg=data[2:]
                c3_var.set(msg)

        if data[0]=='c':
            if data[1]=='4':
                msg=data[2:]
                c4_var.set(msg)

        if data[0]=='c':
            if data[1]=='5':
                msg=data[2:]
                c5_var.set(msg)

        if data[0]=='c':
            if data[1]=='6':
                msg=data[2:]
                c6_var.set(msg)


        if data[0]=='k':
            if data[1]=='1':
                msg=data[2:]
                k1_var.set(msg)

        if data[0]=='k':
            if data[1]=='2':
                msg=data[2:]
                k2_var.set(msg)

        if data[0]=='k':
            if data[1]=='3':
                msg=data[2:]
                k3_var.set(msg)

        if data[0]=='k':
            if data[1]=='4':
                msg=data[2:]
                k4_var.set(msg)

        if data[0]=='k':
            if data[1]=='5':
                msg=data[2:]
                k5_var.set(msg)
        if data[0]=='k':
            if data[1]=='6':
                msg=data[2:]
                k6_var.set(msg)
        if data[0]=='k':
            if data[1]=='7':
                msg=data[2:]
                k7_var.set(msg)
        if data[0]=='k':
            if data[1]=='8':
                msg=data[2:]
                k8_var.set(msg)
        if data[0]=='k':
            if data[1]=='9':
                msg=data[2:]
                k9_var.set(msg)
        if data[0]=='k':
            if data[1]=='a':
                msg=data[2:]
                k10_var.set(msg)

        if data[0]=='k':
            if data[1]=='b':
                msg=data[2:]
                k11_var.set(msg)

        if data[0]=='k':
            if data[1]=='c':
                msg=data[2:]
                k12_var.set(msg)



        if data[0]=='t':
            if data[1]=='1':
                msg=data[2:]
                t1_var.set(msg)

        if data[0]=='t':
            if data[1]=='2':
                msg=data[2:]
                t2_var.set(msg)

        if data[0]=='t':
            if data[1]=='3':
                msg=data[2:]
                t3_var.set(msg)


        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)

def start():
    global strt
    global c1
    global c1_var
    global root
    strt.config(state=DISABLED)
#    root.update_idletasks()

    upd()


"""                   
def stop():
    global stp
    stp.config(state=DISABLED)
    strt.config(state=NORMAL)
    root.update_idletasks()
"""
##########


root=Tk()
root.title('SRNG SAMPANNAPPA HOSTEL')

h=235
w=1300
lw=24
fnt_size=26

sam=Label(root)
sam.pack()
sam.config(text="Samvaya-15    Live update")
sam.config(width=lw*3, background='blue', foreground='white',anchor=CENTER)

sam.config(font=('Agency FB',23, 'bold'))
sam.pack()

#labels for holding data of Table tennis

chess_main=ttk.Label(root)
chess_main.config(font=('Algerian',fnt_size*(4/5), 'bold'), text="CHESS")
chess_main.pack()



r1=LabelFrame(root)
r1.config(height=h,width=w, text="Chess",relief=RIDGE)
r1.pack()
c1_var=StringVar()



cr0=ttk.Frame(r1)
cr0.pack()
c0=Label(cr0)
c0.config(text="Next up")
c0.config(width=lw, background='black', foreground='white',anchor=CENTER)
c0.config(font=('Courier',fnt_size/2, 'bold'))
c0.pack(side=LEFT)

c01=Label(cr0)
c01.config(text="Ongoing")
c01.config(width=lw, background='black', foreground='white',anchor=CENTER)
c01.config(font=('Courier',fnt_size/2, 'bold'))
c01.pack(side=LEFT)



cr1=ttk.Frame(r1)
cr1.pack()

c1=Label(cr1)
#a1_var.set("sujay\nvijay")
c1.config(textvariable =c1_var)
c1.config(width=lw, background='orange', anchor=W, relief=SUNKEN)
c1.config(font=('Courier',fnt_size, 'bold'))
c1.pack(side=LEFT)


c2_var=StringVar()
c2=Label(cr1)
c2.config(textvariable =c2_var)
c2.config(width=lw, background='green',anchor=E,relief=SUNKEN)
c2.config(font=('Courier',fnt_size, 'bold'))
c2.pack(side=LEFT)

cr2=ttk.Frame(r1)
cr2.pack()

c3_var=StringVar()
c3=Label(cr2)
c3.config(textvariable =c3_var)
c3.config(width=lw, background='orange', anchor=W,relief=RIDGE)
c3.config(font=('Courier',fnt_size, 'bold'))
c3.pack(side=LEFT)


c4=Label(cr2)
c4_var=StringVar()
c4.config(textvariable =c4_var)
c4.config(width=lw, background='green', anchor=E,relief=RIDGE)
c4.config(font=('Courier',fnt_size, 'bold'))
c4.pack(side=LEFT)

cr3=ttk.Frame(r1)
cr3.pack()
c5=Label(cr3)
c5_var=StringVar()
c5.config(textvariable =c5_var)
c5.config(width=lw, background='orange',foreground='black', anchor=W)
c5.config(font=('Courier',fnt_size, 'bold'))
c5.pack(side=LEFT)
#c5.grid(row=2,column=0)



c6_var=StringVar()
c6=Label(cr3)
c6.config(textvariable =c6_var)
c6.config(width=lw, background='green', anchor=E,relief=RIDGE)
c6.config(font=('Courier',fnt_size, 'bold'))
c6.pack(side=LEFT)
######################################################################

#labels for holding data of carrom
###################
carrom_main=ttk.Label(root)
carrom_main.config(font=('Algerian',fnt_size*(2/3), 'bold'),text="CARROM")
carrom_main.pack()


carrom=LabelFrame(root)

carrom.config(height=h,width=w, text="Carrom",relief=RIDGE)
carrom.pack()

kr0=ttk.Frame(carrom)
kr0.pack()
k0=Label(kr0)
k0.config(text="Next up")
k0.config(width=lw, background='black', foreground='white',anchor=CENTER)
k0.config(font=('Courier',fnt_size/2, 'bold'))
k0.pack(side=LEFT)


k01=Label(kr0)
k01.config(text="Ongoing")
k01.config(width=lw, background='black', foreground='white',anchor=CENTER)
k01.config(font=('Courier',fnt_size/2, 'bold'))
k01.pack(side=LEFT)



kr1=ttk.Frame(carrom)
kr1.pack()

k1_var=StringVar()
k1=Label(kr1)
k1.config(textvariable =k1_var)
k1.config(width=lw, background='orange', anchor=W,relief=SUNKEN)
k1.config(font=('Courier',fnt_size, 'bold'))
k1.pack(side=LEFT)


k2_var=StringVar()
k2=Label(kr1)
k2.config(textvariable =k2_var)
k2.config(width=lw, background='green',anchor=E,relief=SUNKEN)
k2.config(font=('Courier',fnt_size, 'bold'))
k2.pack(side=LEFT)

kr2=ttk.Frame(carrom)
kr2.pack()
k3_var=StringVar()
k3=Label(kr2)
k3.config(textvariable =k3_var)
k3.config(width=lw, background='orange', anchor=W,relief=RIDGE)
k3.config(font=('Courier',fnt_size, 'bold'))
k3.pack(side=LEFT)


k4=Label(kr2)
k4_var=StringVar()
k4.config(textvariable =k4_var)
k4.config(width=lw, background='green', anchor=E,relief=RIDGE)
k4.config(font=('Courier',fnt_size, 'bold'))
k4.pack(side=LEFT)

kr3=ttk.Frame(carrom)
kr3.pack()
k5=Label(kr3)
k5_var=StringVar()
k5.config(textvariable =k5_var)
k5.config(width=lw, background='orange',foreground='black', anchor=W,relief=SUNKEN)
k5.config(font=('Courier',fnt_size, 'bold'))
k5.pack(side=LEFT)

k6=Label(kr3)
k6_var=StringVar()
k6.config(textvariable =k6_var)
k6.config(width=lw, background='green',foreground='black', anchor=E,relief=SUNKEN)
k6.config(font=('Courier',fnt_size, 'bold'))
k6.pack(side=LEFT)

kr4=ttk.Frame(carrom)
kr4.pack()
k7=Label(kr4)
k7_var=StringVar()
k7.config(textvariable =k7_var)
k7.config(width=lw, background='orange',foreground='black', anchor=W,relief=RIDGE)
k7.config(font=('Courier',fnt_size, 'bold'))
k7.pack(side=LEFT)

k8=Label(kr4)
k8_var=StringVar()
k8.config(textvariable =k8_var)
k8.config(width=lw, background='green',foreground='black', anchor=E,relief=RIDGE)
k8.config(font=('Courier',fnt_size, 'bold'))
k8.pack(side=LEFT)

kr5=ttk.Frame(carrom)
kr5.pack()
k9=Label(kr5)
k9_var=StringVar()
k9.config(textvariable =k9_var)
k9.config(width=lw, background='orange',foreground='black', anchor=W,relief=SUNKEN)
k9.config(font=('Courier',fnt_size, 'bold'))
k9.pack(side=LEFT)

k10=Label(kr5)
k10_var=StringVar()
k10.config(textvariable =k10_var)
k10.config(width=lw, background='green',foreground='black', anchor=E,relief=SUNKEN)
k10.config(font=('Courier',fnt_size, 'bold'))
k10.pack(side=LEFT)

kr6=ttk.Frame(carrom)
kr6.pack()
k11=Label(kr6)
k11_var=StringVar()
k11.config(textvariable =k11_var)
k11.config(width=lw, background='orange',foreground='black', anchor=W,relief=RIDGE)
k11.config(font=('Courier',fnt_size, 'bold'))
k11.pack(side=LEFT)

k12=Label(kr6)
k12_var=StringVar()
k12.config(textvariable =k12_var)
k12.config(width=lw, background='green',foreground='black', anchor=E,relief=RIDGE)
k12.config(font=('Courier',fnt_size, 'bold'))
k12.pack(side=LEFT)

######################################################################


#labels for holding data of Table tennis
######################################################################

tt_main=ttk.Label(root)
tt_main.config(font=('Algerian',fnt_size*(2/3), 'bold'),text="TABLE TENNIS")
tt_main.pack()


tt=LabelFrame(root)

tt.config(height=h,width=w, text="Table Tennis",relief=RIDGE)
tt.pack()


tr0=ttk.Frame(tt)
tr0.pack()
t0=Label(tr0)
t0.config(text="Next up")
t0.config(width=lw, background='black', foreground='white',anchor=CENTER)
t0.config(font=('Courier',fnt_size/2, 'bold'))
t0.pack(side=LEFT)


t01=Label(tr0)
t01.config(text="Ongoing")
t01.config(width=lw, background='black', foreground='white',anchor=CENTER)
t01.config(font=('Courier',fnt_size/2, 'bold'))
t01.pack(side=LEFT)



tr1=ttk.Frame(tt)
tr1.pack()
t1_var=StringVar()
t1=Label(tr1)
t1.config(textvariable =t1_var)
t1.config(width=lw, background='orange',foreground='black', anchor=W)
t1.config(font=('Courier',fnt_size, 'bold'))
t1.pack(side=LEFT)


t2_var=StringVar()
t2=Label(tr1)
t2.config(textvariable =t2_var)
t2.config(width=lw, background='green',foreground='black', anchor=E)
t2.config(font=('Courier',fnt_size, 'bold'))
t2.pack(side=LEFT)

tr2=ttk.Frame(tt)
tr2.pack()
t3_var=StringVar()
t3=Label(tr2)
t3.config(textvariable =t3_var)
t3.config(width=lw*2, background='blue',foreground='white', anchor=CENTER)
t3.config(font=('Courier',fnt_size, 'bold'))
t3.pack()


strt=ttk.Button(root, text="start", command=start)
strt.pack()


root.mainloop()
