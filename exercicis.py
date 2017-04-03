from random import randint
import datetime
def exercici1():
    print "Hello Moto"
def exercici2():
    print "Numero: ",randint(0,1000)
def exercici3():
    dataActual=datetime.datetime.now()
    horaFormatada = str(dataActual.hour)+":"+str(dataActual.minute)+":"+str(dataActual.second)
    archi=open('datos.txt','w')
    archi.write(horaFormatada)
    archi.close()
