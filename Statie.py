import random
import numpy as np
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import adafruit_dht
import ADS1256
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
import time
from LCD import LCD
import RPi.GPIO as GPIO
from time import sleep
import os
import sys
import time
import board
import csv
import busio
import adafruit_adxl34x
import ADS1256
import datetime
from time import sleep
import os
import ssl
import smtplib
from email.message import EmailMessage
import Emailtrimis
dcvant = None
atentionare = None
tip_alerta = None


vreme = "Linistita"
#calibram senzorii
#calibrating the sensors
import calibrare

#pregatim variabilele 
#prepare the variables
aer=None
perioadazi = None
dirvant = "Vant slab"

#pini motor GPIO modul BCM
#preparing the motor pins
motor_channel = (17,20,22,27)

#setam sa nu se opreasca datorita unui warning  
#setting to continue if any warning will appear
GPIO.setwarnings(False)

#setam GPIO pe modul BCM
#activating GPIO with BCM
GPIO.setmode(GPIO.BCM)

#setam pinii driverului motorului pentru iesire
#setting gpio for output
GPIO.setup(motor_channel, GPIO.OUT)

#setam counterul pentru pasi facuti(mpp face 2048 pasi la 360 de grade)
#setting the counter for steps
step_count = 0

#pozitii aferente
#positions
pozitii = ["s","sv","v","nv","n","ne","e","se"]
#pozitii =  0   1    2    3   4   5    6    7  ]

#pasi diferenta dintre 2 puncte cardinale salvate in vector
#how many steps between 2 cardinals
steps = 256

#importam GRAFIC pentru schema grafica
#importing for graph
import GRAFIC

#importam modul din libraria busio-- ne foloseste la accelerometru--
#importing for accelerometer
i2c = busio.I2C(board.SCL,board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

#setam parametrii
#setting the paramethers
stare=None
aer=None

#implementam libraria LCD pentru afisaj
#implementing LCD
lcd = LCD()


#salvam pinii GPIO.BCM pentru cei 4 senzori DHT
#saving the pins of the DHT
sensor1 = adafruit_dht.DHT11(board.D23)#1
sensor2 = adafruit_dht.DHT11(board.D25)#2
sensor3 = adafruit_dht.DHT11(board.D21)#3
sensor4 = adafruit_dht.DHT11(board.D18)#4

#implementam un contor
#implementing a counter
contor = 1


perioada = None


acum = time.time()

#stergem fisierele din dht_date_temporare.csv pentru a porni afisajul grafic de la valorile prezente
#os.remove("dht_date_temporare.csv")




#pornim fisierele pentru a scrie tipul de valori pe coloane
#save in csv
with open("dht_date_temporare.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data", "Temperatura", "Umiditatea","Vreme","Perioada","Vant","Activitate seismica","Calitate Aer","Viteza Vant"])

#with open("dht_date.csv", "w", newline="") as f:
 #   writer = csv.writer(f)
  #  writer.writerow(["Data", "Temperatura", "Umiditatea","Vreme","Perioada","Vant","Activitate seismica","Calitate Aer","Viteza Vant"])





while True:
    try:
        #initiem adc-ul pentru a citi valori
	#reading adc values
        ADC = ADS1256.ADS1256()
        ADC.ADS1256_init()
        
        #salvam valorile adc-ului intr-un vector valadc
	#saving the values
        valadc= ADC.ADS1256_GetAll()
        
        #alegem pozitiile pentru masinuta
	#choose the positions
        pozitii = ["s","sv","v","nv","n","ne","e","se"]
        
        #setam pinii din driverul motorasului
	#setting the driver pins
        motor_channel = (17,20,22,27)
        
        #pentru a nu ne da erori setam warningurile pe fals
	#to avoid errors, we are setting the warnings on false
        GPIO.setwarnings(False)
        
        #setam modul de citire al pinilor, alegem BCM
	#setting the BCM
        GPIO.setmode(GPIO.BCM)
        
        #setam pinii din Driver ca drept fiind outputuri
	#setting the outputs
        GPIO.setup(motor_channel, GPIO.OUT)
        
        #salvam valorile de acum ale acceleratorului
	#saving the accelerometer values
        x,y,z = accelerometer.acceleration
        
        #salvam valorile adc-ului intr-un vector valadc
	#saving the values in a vector
        #valadc = ADC.ADS1256_GetAll()
        
        #salvam in foto valorile fotorezistorului
	#saving the photoresistor values
        foto=valadc[3]/1677700
        
        #salvam in aerqual valorile senzorului MQ-2
	#saving MQ-2 values
        aerqual=valadc[1]/1677700
        print("aerqual=",valadc[1]/1677700)
      

        
        #salvam ora curenta pentru baza de date
	#saving the current time
        oracurenta = datetime.datetime.now()
        formatora = oracurenta.strftime("%H:%M:%S")
        
        print("Ora este: ", formatora)
        
        #salvam in temp1 temperatura de pe primul senzor
	#first temperature value
        temp1 = sensor1.temperature#sv
        
	#first humidity value
        #salvam in hum1 umiditatea de pe primul senzor
        hum1 = sensor1.humidity#sv

        #second temperature value
        #salvam in temp2 temperatura de pe al doilea senzor
        temp2 = sensor2.temperature#se
        
	#second humidity value
        #salvam in temp1 temperatura de pe al doilea senzor
        hum2 = sensor2.humidity#se
        
	#third temperature value
        #salvam in temp1 temperatura de pe al treilea senzor
        temp3 = sensor3.temperature#nv
        
	#third humidity value
        #salvam in temp1 temperatura de pe al treilea senzor
        hum3 = sensor3.humidity#nv
        
	#forth temperature value
        #salvam in temp1 temperatura de pe al patrulea senzor
        temp4 = sensor4.temperature#ne
        
	#forth humidity value
        #salvam in temp1 temperatura de pe al patrulea senzor
        hum4 = sensor4.humidity#ne
        
        #salvam in xjoy si yjoy valorile din HW-504 pentru a schimba meniul din LCD
	#HW-504 values to switch the lcd menu
        xjoy = valadc[7]/1677700
        dc = int(valadc[5]/16777*5)
        print("Viteza vant:",dc)
        if dc < 6:
                dcvant = "sub 6 km/h"
        else:
                dcvant = f"{dc}km/h"
        #facem media temperaturilor si umiditatilor pentru o precizie mai buna
	#mean for temperature and humidity
        avg_temp = (temp1 + temp2 + temp3 + temp4) / 4
        avg_hum = (hum1 + hum2 + hum3 + hum4) / 4
        
        
        #stabilim perioada din zi pentru afisajul grafic si baza de date
	#establish the csv files
        if int(oracurenta.strftime("%H"))>7 and int(oracurenta.strftime("%H"))<22:
                perioadazi = "Zi"
        else:
                perioadazi = "Noapte"
        
        
        if avg_temp > 39:
                tip_alerta = "Canicula"
                atentionare = "Temperaturi foarte ridicate"
        #lcd.message("Status alerta", 1)
        #lcd.message(str(stare), 2)
        #setam pe fereastra principala de LCD temperatura si umiditatea
	#setting the lcd output for temperature, humidity and so on
        #lcd.message("Temp:"+str(avg_temp)+"*C", 1)
        #lcd.message("Umid med:"+str(avg_hum)+"%", 2)
        
        
        #setam starile pentru meniul LCD si baza de date
        if abs(x-calibrare.x1)<0.5 and abs(y-calibrare.y1)<0.5:
                stare = "Inactiv"
        elif abs(x-calibrare.x1) >0.5 or abs(y-calibrare.y1)<0.5 and abs(x-calibrare.x1)<1 and (y-calibrare.y1)<1:
                stare = "  Activ Usor"
                tip_alerta = "Seism"
                Emailtrimis.mail(tip_alerta,stare)
                
                
                
                
        elif abs(x-calibrare.x1)>1 or abs(y-calibrare.y1)>1 and abs(x-calibrare.x1)<2 and (y-calibrare.y1)<2:
                stare = " Activ Moderat"
                tip_alerta = "Seism"
                Emailtrimis.mail(tip_alerta,stare)
                
               
               
               
        elif abs(x-calibrare.x1)>2 or abs(y-calibrare.y1)>2:
                stare = " Activ Sever"
                tip_alerta = "Seism"
                Emailtrimis.mail(tip_alerta,stare)
               
                
        
        #setam calitatea aerului pentru meniul LCD si baza de date
        if aerqual <1.45:
                aer="Normal"
        elif aerqual >1.45 and aerqual <1.7:
                aer = "Poluare Moderata"
                tip_alerta = "Poluare a aerului"
                Emailtrimis.mail(tip_alerta,aer)
               
        elif aerqual >1.7:
                aer="Poluat Sever"
                tip_alerta = "Poluare a aerului"
                Emailtrimis.mail(tip_alerta,aer)
               
        
        
        
        #setam starea vremii pentru baza de date si meniul LCD
        if int(oracurenta.strftime("%H"))>7 and int(oracurenta.strftime("%H"))<22 and foto <1.7:
                vreme = "Senin"
        elif int(oracurenta.strftime("%H"))>7 and int(oracurenta.strftime("%H"))<22 and foto > 1.7:
                vreme = "Innorat"
        elif int(oracurenta.strftime("%H"))<7 and int(oracurenta.strftime("%H"))>22 and abs(x-calibrare.x1) >0.5 and abs(y-calibrare.y1)>0.5:
                vreme = "instabila"
        elif int(oracurenta.strftime("%H"))<7 and int(oracurenta.strftime("%H"))>22 and foto > 2.5:
                vreme = "Linistita"
        elif int(oracurenta.strftime("%H"))<7 and int(oracurenta.strftime("%H"))>22:
                vreme = "Noapte"
        elif int(oracurenta.strftime("%H"))>7 and int(oracurenta.strftime("%H"))<22:
                vreme = "Zi"
        
        
        
        if int(avg_hum)>75.9 :
                vreme = "Ploua"
        
        if avg_hum > 75.9 and abs(x-calibrare.x1) >0.2 and abs(y-calibrare.y1)>0.2 and dc>50:
                vreme = "Furtuna"
                tip_alerta = "Furtuna si Vijelii" 
                Emailtrimis.mail(tip_alerta,vreme)
            #    buzz(1.5)
        
        #setam girueta electronica pentru a ne arata directia din care bate vantul
        #ne luam dupa umiditate
        if hum2 < avg_hum:
                #vantul bate din SE
                calibrare.motoras(1)#se
                dirvant = "SE------>NV"
                
        elif hum2<avg_hum and hum4<avg_hum:
                #vantul bate din E
                calibrare.motoras(2)#e
                dirvant = "E------->V"
                
        elif hum4<avg_hum:
                #vantul bate din NE
                calibrare.motoras(3)#ne
                dirvant = "NE------>SV"
                
        elif hum4<avg_hum and hum3<avg_hum:
                #vantul bate din N
                calibrare.motoras(4)#n
                dirvant = "N------->S"
                
        elif hum3<avg_hum:
                #vantul bate din NV
                calibrare.motoras(5)#nv
                dirvant = "NV------>SE"
                
        elif hum3<avg_hum and hum1<avg_hum:
                #vantul bate din NV
                calibrare.motoras(6)#v
                dirvant = "V------->E"
                
        elif hum1<avg_hum:
                #vantul bate din SV
                calibrare.motoras(7)#sv
                dirvant = "SV------>NE"
                
        elif hum2<avg_hum and hum1>avg_hum:
                #vantul bate din S
                calibrare.motoras(0)#s
                dirvant = "S------>N"
        
        
        #setam meniul LCD din joystick
        if xjoy >1.5:
                #setam un contor pentru afisor
                contor = contor + 1
                
                
        elif xjoy <0.5:
                contor = contor - 1
                
       
        #cream meniul din joystick
        if contor == 0:
                lcd.clear()
                lcd.message("Directie Vant", 1)
                lcd.message(dirvant, 2)
        elif contor == -1:
                contor = 6
                lcd.clear()
                lcd.message("  Umiditate:", 1)
                lcd.message(str(avg_hum)+"%", 2)
        elif contor == 7:
                contor = 0
                lcd.clear()
                lcd.message("Directie Vant", 1)
                lcd.message(dirvant, 2)
        elif contor == 1:
                lcd.clear()
                lcd.message("Activitate seism", 1)
                lcd.message(str(stare), 2)
        elif contor == 2:
                lcd.clear()
                lcd.message("Calitate Aer", 1)
                lcd.message(str(aer), 2)
        elif contor == 3:
                lcd.clear()
                lcd.message("Stare Vreme", 1)
                lcd.message(str(perioadazi)+str(vreme), 2)
        elif contor == 4:
                lcd.clear()
                lcd.message("Viteza vant:", 1)
                lcd.message(dcvant, 2)
        elif contor == 5:
                lcd.clear()
                lcd.message("Temperatura:", 1)
                lcd.message(str(avg_temp)+"*C", 2)
        elif contor == 6:
                lcd.clear()
                lcd.message("  Umiditate:", 1)
                lcd.message(str(avg_hum)+"%", 2)
        
                
                
        
        
        
        
        #afisam toate valorile
        titlu = str(perioadazi)+" "+str(vreme)	
        # Print average temperature and humidity
        print("Temperatura resimtita: {:.1f}°C".format(avg_temp))
        print("Umiditate resimtita: {:.1f}%".format(avg_hum))
        
        print("Perioada din zi: {}".format(perioadazi))
        print("Directie vant",dirvant)
        
        print("Activitate seism:",stare)
        print("Calitate aer",aer)
        
        print("Viteza vantului",contor)
        print("Stare vreme",vreme)
        print("Contor meniu:", contor)
        print("Viteza vantului ",dcvant)
        
        # Scriem datele in fisierele .csv
        with open("dht_date.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), float(avg_temp), float(avg_hum),str(vreme),str(perioadazi),str(dirvant),str(stare),str(aer),dc])
        with open("dht_date_temporare.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.strftime("%H:%M:%S"), float(avg_temp), float(avg_hum),str(vreme),str(perioadazi),str(dirvant),str(stare),str(aer),dc])    
        
       


        #exceptie senzor ADXL345 pentru unele erori in care ni se citesc valori nule
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
        #exceptie pentru senzorii dht, au momente cand nu se alimenteaza
    except Exception as error:
        sensor1.exit()
        sensor2.exit()
        sensor3.exit()
        sensor4.exit()
        raise error
        continue
        #exceptie pentru motorasul pas cu pas
    except KeyboardInterrupt:
        lcd.message("    STATIA SE   ",1)
        lcd.message("     INCHIDE   ",2)
        print('se opreste motorul')
        sys.exit(0)
        
        #exceptie ADC, unoeri nu se citesc valorile
    except :
        GPIO.cleanup()
        print ("\r\nSe opreste programul")
        exit()

    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("Pregateste-te sa schimbi meniul")
    time.sleep(2)
    print("Schimba meniul!")
    time.sleep(2)
    
    lcd.clear()

#recommended press CTRL + C to exit the program after it shows IDread Correct
#de recomandat ctrl c cand iesim din program dupa ce ne arata IDread correct

