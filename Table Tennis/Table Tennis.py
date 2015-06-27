"""
This is a part of window application that was written to update a live feed for a indoor games organized in an event.
 This script is written to update the feed about Table Tennis.
"""
from Tkinter import *
import ttk
from ttk import *
import os
from socket import *



########
def config_target():
#    update_status("configuring target...")
    global ip_en
    global port_en
    global addr
    ip=ip_en.get()    
    print ip
    addr
    port=int(port_en.get())
    addr=(ip,port)
#    update_status("Target Configured...")


def send_msg(msg):	#func to send the data
    config_target()
    global addr
    UDPSock.sendto(msg, addr)
    print "msg sent " + msg


	#callbacks for the buttins
def t1_bu():
    global p_en_1
    data='t1'+up_en_1.get()
    send_msg(data)

def t2_bu():
    global up_en_2
    data='t2'+on_en_1.get()
    send_msg(data)

def t3_bu():
    global up_en_3
    data='t3'+com_en_1.get()
    send_msg(data)

host=str()
port=int()
addr=tuple()
UDPSock = socket(AF_INET, SOCK_DGRAM)


#Graphics part of the code
root=Tk()
root.title('Table Tennis')

con=LabelFrame(root,text='Configuration')
con.pack()
ip_en=ttk.Entry(con)
ip_en.insert(0,'192.168.1.1')
ip_en.pack()
port_en=ttk.Entry(con)
port_en.insert(0,'13002')
port_en.pack()
config=ttk.Button(con, text="Configure")
config.pack()


upc=LabelFrame(root)
upc.config(text='Next up')
upc.pack(side=LEFT)
upc1=Label(upc)
upc1.pack()
la1=Label(upc1,text='t1')
la1.pack(side=LEFT)
up_en_1=ttk.Entry(upc1, width=25)
up_en_1.pack(side=LEFT)
up_en1_bu=ttk.Button(upc1,text='send',command=t1_bu)
up_en1_bu.pack(side=LEFT)

com=LabelFrame(root)
com.config(text='commentary')
com.pack(side=LEFT)
com_la_2=Label(com,text='t3')
com_la_2.pack(side=LEFT)
com_en_1=ttk.Entry(com, width=40)
com_en_1.pack(side=LEFT)
com_en2_bu=ttk.Button(com,text='send',command=t3_bu)
com_en2_bu.pack(side=LEFT)


ong=LabelFrame(root)
ong.config(text='ongoing')
ong.pack(side=LEFT)
ong1=Label(ong)
ong1.pack()
on_la_1=Label(ong1,text='t2')
on_la_1.pack(side=LEFT)
on_en_1=ttk.Entry(ong1, width=25)
on_en_1.pack(side=LEFT)
on_en1_bu=ttk.Button(ong1,text='send',command=t2_bu)
on_en1_bu.pack(side=LEFT)


mainloop()


