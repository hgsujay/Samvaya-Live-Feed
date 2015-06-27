"""
This is a part of window application that was written to update a live feed for a indoor games organized in an event.\
 This script is written to update the feed about chess.
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
    ip=ip_en.get()   #get ip from the ip entry field  
    print ip
    addr
    port=int(port_en.get())     #get port num from the port num entry field
    addr=(ip,port)      #bind it into a tuple


#send message to target
def send_msg(msg):
    config_target()     #configure target everytime a msg is sent
    global addr
    UDPSock.sendto(msg, addr)   #send message through a udp socket   
    print "msg sent " + msg


#functions when buttons are clicked, prefix a code before the msg and pass it to send_msg() func
def c1_bu():
    global p_en_1
    data='c1'+up_en_1.get()
    send_msg(data)

def c2_bu():
    global up_en_2
    data='c2'+on_en_1.get()
    send_msg(data)

def c3_bu():
    global up_en_3
    data='c3'+up_en_2.get()
    send_msg(data)

def c4_bu():
    global up_en_4
    data='c4'+on_en_2.get()
    send_msg(data)

def c5_bu():
    global up_en_5
    data='c5'+up_en_3.get()
    send_msg(data)

def c6_bu():
    global up_en_6
    data='c6'+on_en_3.get()
    send_msg(data)




host=str()  #string variable to store ip address
port=int()  #int variable to store port num
addr=tuple()    #a tuple to store host and port
UDPSock = socket(AF_INET, SOCK_DGRAM)


root=Tk()
root.title('Chess')

con=LabelFrame(root,text='Configuration')   #a child to root, to hold ip and host entries
con.pack()
ip_en=ttk.Entry(con)    #child of con labelframe, an entry field for ip_address
ip_en.insert(0,'192.168.1.1')
ip_en.pack()
port_en=ttk.Entry(con)      #child of con labelframe, an entry field for port num
port_en.insert(0,'13002')
port_en.pack()
config=ttk.Button(con, text="Configure")    #a button to set the addr variable using the host n port entries
config.pack()

#a label frame to hold all the buttons and entries about upcoming matches
upc=LabelFrame(root)
upc.config(text='Next up')
upc.pack(side=LEFT)

#one more label to hold all the entries for updating upcomming matches
upc1=Label(upc)
upc1.pack()
#label1 to hold a label, entry and button in a single row
la1=Label(upc1,text='c1')
la1.pack(side=LEFT)
up_en_1=ttk.Entry(upc1, width=25)
up_en_1.pack(side=LEFT)
up_en1_bu=ttk.Button(upc1,text='send',command=c1_bu)
up_en1_bu.pack(side=LEFT)

#label 2 to hold a label, entry and button in a single row
upc2=Label(upc)
upc2.pack()
la2=Label(upc2,text='c3')
la2.pack(side=LEFT)
up_en_2=ttk.Entry(upc2, width=25)
up_en_2.pack(side=LEFT)
up_en2_bu=ttk.Button(upc2,text='send',command=c3_bu)
up_en2_bu.pack(side=LEFT)

#label 3 to hold a label, entry and button in a single row
upc3=Label(upc)
upc3.pack()
la3=Label(upc3,text='c5')
la3.pack(side=LEFT)
up_en_3=ttk.Entry(upc3, width=25)
up_en_3.pack(side=LEFT)
up_en3_bu=ttk.Button(upc3,text='send',command=c5_bu)
up_en3_bu.pack(side=LEFT)


#parent labels to hold labels(c2,c4,c6), entry and button
ong=LabelFrame(root)
ong.config(text='ongoing')
ong.pack(side=LEFT)

ong1=Label(ong)
ong1.pack()
on_la_1=Label(ong1,text='c2')
on_la_1.pack(side=LEFT)
on_en_1=ttk.Entry(ong1, width=25)
on_en_1.pack(side=LEFT)
on_en1_bu=ttk.Button(ong1,text="send",command=c2_bu)
on_en1_bu.pack(side=LEFT)


ong2=Label(ong)
ong2.pack()
on_la_2=Label(ong2,text='c4')
on_la_2.pack(side=LEFT)
on_en_2=ttk.Entry(ong2, width=25)
on_en_2.pack(side=LEFT)
on_en2_bu=ttk.Button(ong2,text='send',command=c4_bu)
on_en2_bu.pack(side=LEFT)

ong3=Label(ong)
ong3.pack()
on_la_3=Label(ong3,text='c6')
on_la_3.pack(side=LEFT)
on_en_3=ttk.Entry(ong3, width=25)
on_en_3.pack(side=LEFT)
on_en3_bu=ttk.Button(ong3,text='send',command=c6_bu)
on_en3_bu.pack(side=LEFT)

mainloop()


