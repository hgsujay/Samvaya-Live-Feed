"""
This is a part of window application that was written to update a live feed system for a indoor games organized in a event. 
This script is written to update the feed about carrom.
"""
from Tkinter import *
import ttk
from ttk import *
import os
from socket import *



#function to configure host and port
def config_target():
    global ip_en
    global port_en
    global addr
    ip=ip_en.get()  #get ip from the ip entry field   
    print ip
    addr
    port=int(port_en.get()) #get port num from the port num entry field
    addr=(ip,port)  #bind it into a tuple


#send message to target
def send_msg(msg):
    config_target() #configure target everytime a msg is sent
    global addr
    UDPSock.sendto(msg, addr)   #send message through a udp socket
    print "msg sent " + msg


#functions when buttons are clicked, prefix a code before the msg and pass it to send_msg() func

def k1_bu():
    global up_en_1
    data='k1'+up_en_1.get()
    send_msg(data)

def k2_bu():
    global on_en_1
    data='k2'+on_en_1.get()
    send_msg(data)

def k3_bu():
    global up_en_2
    data='k3'+up_en_2.get()
    send_msg(data)

def k4_bu():
    global on_en_2
    data='k4'+on_en_2.get()
    send_msg(data)

def k5_bu():
    global up_en_3
    data='k5'+up_en_3.get()
    send_msg(data)

    
def k6_bu():
    global on_en_3
    data='k6'+on_en_3.get()
    send_msg(data)

def k7_bu():
    global up_en_4
    data='k7'+up_en_4.get()
    send_msg(data)

def k8_bu():
    global on_en_4
    data='k8'+on_en_4.get()
    send_msg(data)

def k9_bu():
    global up_en_5
    data='k9'+up_en_5.get()
    send_msg(data)

def k10_bu():
    global on_en_5
    data='ka'+on_en_5.get()
    send_msg(data)

def k11_bu():
    global up_en_6
    data='kb'+up_en_6.get()
    send_msg(data)
    

def k12_bu():
    global on_en_6
    data='kc'+on_en_6.get()
    send_msg(data)




host=str()  #string variable to store ip address
port=int()  #int variable to store port num
addr=tuple()    #a tuple to store host and port
UDPSock = socket(AF_INET, SOCK_DGRAM)


root=Tk()


con=LabelFrame(root,text='Configuration')   #a child to root, to hold ip and host entries
con.pack()
ip_en=ttk.Entry(con)    #child of con labelframe, an entry field for ip_address
ip_en.insert(0,'192.168.1.1')
ip_en.pack()
port_en=ttk.Entry(con)  #child of con labelframe, an entry field for port num
port_en.insert(0,'13002')
port_en.pack()
config=ttk.Button(con, text="Configure", command=config_target)    #a button to set the addr variable using the host n port entries
config.pack()


#a label frame to hold all the buttons and entries about upcoming matches
upc=LabelFrame(root)
upc.config(text='Next up')
upc.pack(side=LEFT)

#one more label to hold all the entries for updating upcomming matches
upc1=Label(upc)
upc1.pack()

#label1 to hold a label, entry and button in a single row
la1=Label(upc1,text='k1')
la1.pack(side=LEFT)
up_en_1=ttk.Entry(upc1, width=25)
up_en_1.pack(side=LEFT)
up_en1_bu=ttk.Button(upc1,text='send',command=k1_bu)
up_en1_bu.pack(side=LEFT)

#label 2 to hold a label, entry and button in a single row
upc2=Label(upc)
upc2.pack()
la2=Label(upc2,text='k3')
la2.pack(side=LEFT)
up_en_2=ttk.Entry(upc2, width=25)
up_en_2.pack(side=LEFT)
up_en2_bu=ttk.Button(upc2,text='send',command=k3_bu)
up_en2_bu.pack(side=LEFT)

#label 3 to hold a label, entry and button in a single row
upc3=Label(upc)
upc3.pack()
la3=Label(upc3,text='k5')
la3.pack(side=LEFT)
up_en_3=ttk.Entry(upc3, width=25)
up_en_3.pack(side=LEFT)
up_en3_bu=ttk.Button(upc3,text='send',command=k5_bu)
up_en3_bu.pack(side=LEFT)

#label 4 to hold a label, entry and button in a single row
upc4=Label(upc)
upc4.pack()
la4=Label(upc4,text='k7')
la4.pack(side=LEFT)
up_en_4=ttk.Entry(upc4, width=25)
up_en_4.pack(side=LEFT)
up_en4_bu=ttk.Button(upc4,text='send',command=k7_bu)
up_en4_bu.pack(side=LEFT)

#label 5 to hold a label, entry and button in a single row
upc5=Label(upc)
upc5.pack()
la5=Label(upc5,text='k9')
la5.pack(side=LEFT)
up_en_5=ttk.Entry(upc5, width=25)
up_en_5.pack(side=LEFT)
up_en5_bu=ttk.Button(upc5,text='send',command=k9_bu)
up_en5_bu.pack(side=LEFT)

#label 6 to hold a label, entry and button in a single row
upc6=Label(upc)
upc6.pack()
la6=Label(upc6,text='k11')
la6.pack(side=LEFT)
up_en_6=ttk.Entry(upc6, width=25)
up_en_6.pack(side=LEFT)
up_en6_bu=ttk.Button(upc6,text='send',command=k11_bu)
up_en6_bu.pack(side=LEFT)



#a label frame to hold all the buttons and entries about ongoing matches
ong=LabelFrame(root)
ong.config(text='ongoing')
ong.pack(side=LEFT)

#parent labels to hold labels(k2,k4,k6,k8,k10,k12), entry and button
ong1=Label(ong)
ong1.pack()
on_la_1=Label(ong1,text='k2')
on_la_1.pack(side=LEFT)
on_en_1=ttk.Entry(ong1, width=25)
on_en_1.pack(side=LEFT)
on_en1_bu=ttk.Button(ong1,text='send',command=k2_bu)
on_en1_bu.pack(side=LEFT)


ong2=Label(ong)
ong2.pack()
on_la_2=Label(ong2,text='k4')
on_la_2.pack(side=LEFT)
on_en_2=ttk.Entry(ong2, width=25)
on_en_2.pack(side=LEFT)
on_en2_bu=ttk.Button(ong2,text='send',command=k4_bu)
on_en2_bu.pack(side=LEFT)

ong3=Label(ong)
ong3.pack()
on_la_3=Label(ong3,text='k6')
on_la_3.pack(side=LEFT)
on_en_3=ttk.Entry(ong3, width=25)
on_en_3.pack(side=LEFT)
on_en3_bu=ttk.Button(ong3,text='send',command=k6_bu)
on_en3_bu.pack(side=LEFT)

ong4=Label(ong)
ong4.pack()
on_la_4=Label(ong4,text='k8')
on_la_4.pack(side=LEFT)
on_en_4=ttk.Entry(ong4, width=25)
on_en_4.pack(side=LEFT)
on_en4_bu=ttk.Button(ong4,text='send',command=k8_bu)
on_en4_bu.pack(side=LEFT)

ong5=Label(ong)
ong5.pack()
on_la_5=Label(ong5,text='k10')
on_la_5.pack(side=LEFT)
on_en_5=ttk.Entry(ong5, width=25)
on_en_5.pack(side=LEFT)
on_en5_bu=ttk.Button(ong5,text='send',command=k10_bu)
on_en5_bu.pack(side=LEFT)


ong6=Label(ong)
ong6.pack()
on_la_6=Label(ong6,text='k12')
on_la_6.pack(side=LEFT)
on_en_6=ttk.Entry(ong6, width=25)
on_en_6.pack(side=LEFT)
on_en6_bu=ttk.Button(ong6,text='send',command=k12_bu)
on_en6_bu.pack(side=LEFT)

mainloop()


