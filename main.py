from Tkinter import *
import json
import ssl
import time
import paho.mqtt.client as paho
import serial
from gpiozero import PWMLED

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.4)
s=[0]
ser.isOpen()



pencere = Tk()
pencere.geometry('1600x900+0+0')
pencere.title("Home Automation")
pencere.tk_setPalette("white")
pencere.overrideredirect(0)

photo = PhotoImage(file ="beyaz_ev.png")
resim =Label(pencere, image=photo,bd=0)
resim.place(relx=0.07,rely=0.17)

photo2 = PhotoImage(file = "lamp_turn_on.png")
resim2 = Label(pencere, image=photo2, bd=0)
resim2.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim2.place_forget()

resim3 = Label(pencere, image=photo2, bd=0)
resim3.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim3.place_forget()

resim4 = Label(pencere, image=photo2, bd=0)
resim4.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim4.place_forget()

resim5 = Label(pencere, image=photo2, bd=0)
resim5.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim5.place_forget()

resim6 = Label(pencere, image=photo2, bd=0)
resim6.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim6.place_forget()

photo3 = PhotoImage(file = "door_open.png")
resim7 = Label(pencere, image=photo3, bd=0)
resim7.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim7.place(relx=0.05,rely=0.62)

photo4 = PhotoImage(file = "windows_open.png")
resim7 = Label(pencere, image=photo4, bd=0)
resim7.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim7.place(relx=0.155,rely=0.14)

resim8 = Label(pencere, image=photo4, bd=0)
resim8.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim8.place(relx=0.4,rely=0.14)

resim7 = Label(pencere, image=photo4, bd=0)
resim7.config(text="", compound = "center", borderwidth=0.01, highlightthickness=0.01,  font="Helveticalight 44 normal",  fg="white", bd=0)
resim7.place(relx=0.4,rely=0.75)

yazi1 = Label(pencere, bd=0)
yazi1.config(text="", compound = "center",   font="Helveticalight 20 normal",  fg="black", bd=1)
yazi1.place(relx=0.6,rely=0.4)
 
yazi2 = Label(pencere, bd=0)
yazi2.config(text="", compound = "center",   font="Helveticalight 20 normal",  fg="black", bd=1)
yazi2.place(relx=0.6,rely=0.5)

yazi3 = Label(pencere, bd=0)
yazi3.config(text="", compound = "center",   font="Helveticalight 20 normal",  fg="black", bd=1)
yazi3.place(relx=0.6,rely=0.6)


yazi4 = Label(pencere, bd=0)
yazi4.config(text="", compound = "center",   font="Helveticalight 20 normal",  fg="black", bd=1)
yazi4.place(relx=0.63,rely=0.15)


yazi5 = Label(pencere, bd=0)
yazi5.config(text="Home Automation System Display", compound = "center",   font="Helveticalight 30 bold",  fg="black", bd=1)
yazi5.place(relx=0.2,rely=0.05)

yazi6 = Label(pencere, bd=0)
yazi6.config(text="", compound = "center",   font="Helveticalight 10 normal",  fg="black", bd=1)
yazi6.place(relx=0.645,rely=0.235)



def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) + "\n")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#", 1)


def on_message(client, userdata, msg):
    fromdata = ser.readline()
    print("topic: " + msg.topic + "\n")
    if msg.topic == "bitirmepub" :
        data = json.loads(msg.payload)
        data2 =msg.payload
        firstname = data["firstname"]
        lastname = data["lastname"]
        beaconId = data["beaconId"]
        distance = data["distance"]
        seekbarval = data["seekbarval"]
        seekbartype = data["seekbartype"]
        motordirection = data["motordirection"]
        currenttime = data["currenttime"]
        switchval = data["switchval"]
        switchtype = data["switchtype"]
        yazi4.config(text="Welcome to your Home\n" + firstname + " " + lastname )
        currenttime = data["currenttime"]
        yazi6.config(text="(Last controlled: "+ currenttime + " )")

        if str(switchval) == "True":
            if switchtype == "switch1":
                resim2.place(relx=0.22,rely=0.57)
            if switchtype == "switch2":
                resim3.place(relx=0.115,rely=0.42)
            if switchtype == "switch3":
                resim4.place(relx=0.18,rely=0.22)
            if switchtype == "switch4":
                resim5.place(relx=0.425,rely=0.22)
            if switchtype == "switch5":
                resim6.place(relx=0.43,rely=0.55)


        if str(switchval) == "False":
            if switchtype == "switch1":
                resim2.place_forget()
            if switchtype == "switch2":
                resim3.place_forget()
            if switchtype == "switch3":
                resim4.place_forget()
            if switchtype == "switch4":
                resim5.place_forget()
            if switchtype == "switch5":
                resim6.place_forget()
        ser.write(data2)
        dowork()


def dowork():
        fromdata = ser.readline()
        print("gelendata  = " + fromdata)
        data3 = json.loads(fromdata)
            mqttc.publish("fromrasp", fromdata, qos=0)
        if data3["LDRValue1"] != "" :
            LDRValue1 = data3["LDRValue1"]
        if data3["LDRValue2"] != "" :
            LDRValue2 = data3["LDRValue2"]
        if data3["sicaklik"] != "" :
            sicaklik = data3["sicaklik"]
        yazi1.config(text="LDR_1 : " + LDRValue1 )
        yazi2.config(text="LDR_2 : " + LDRValue2 )
        yazi3.config(text="Sicaklik : " + sicaklik )

    


mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "awshost"
awsport = 8883
clientId = "OTELLO"
thingName = "Bitirme"
caPath = "root-CA.crt"
certPath = "Bitirme.cert.pem"
keyPath = "Bitirme.private.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2,
              ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_start()
pencere.mainloop()
