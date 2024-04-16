#DIRECTOR CALIBRARE
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
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import time
import os
import board
import adafruit_dht
import csv
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
#initializam biblioteca LCD pentru afisaj
#initialise LCD
lcd = LCD()
#initializam i2c din biblioteca busio pt accelerometru
#initialise i2c for accelerometer
i2c = busio.I2C(board.SCL,board.SDA)
#define accelerometer
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#salvam Primele valori pe care le vom compara cu cele care vor veni in program 
#we are saving the first values to compare with the other values from program when it runs
x1,y1,z1 = accelerometer.acceleration
print(round(x1,2),round(y1,2),round(z1,2))

# cream o functie pentru o oprire de program in conditii de siguranta, fara a perturba functionalitatea
# sistemului
# we create a function to stop in a safestate, without disturbing the functionality of the system

def safe_exit(signum,frame):
        exit(1)
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

#afisam textul de calibrare
#lcd output message for calibration
lcd.text("Statie Meteo",1)
lcd.text("Loading...",2)    
        


#pini motor GPIO modul BCM
#set the step motor pins
motor_channel = (17,20,22,27)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#stabilim pinii driverului motorasului ca output
#set the pins of the driver
GPIO.setup(motor_channel, GPIO.OUT)
#configuram un counter pentru pasi
#configure the step counter
step_count = 0
#facem un vector pentru pozitia mpp
#establish a vector for step motor position
pozitii = ["s","se","e","ne","n","nv","v","sv"]
#pozitii / positions =  0   1    2    3   4   5    6    7  ]
#alegem cati pasi sunt intre 2 puncte cardinale predefinite de noi
#choose how many steps are between 2 cardinals
steps = 256


def motoras(nr):
    with open("Valori.txt","r") as f:
      numar=f.read()
    step_count = 0
    steps = 256
    pasidoriti = (int(nr)-int(numar))*steps
    print(pasidoriti)
    while step_count < abs(pasidoriti):
        try:
            if pasidoriti > 0:
              #setam sa se roteasca in sensul acelor de ceasornic
              #set the step motor to change its position in clockwise
              GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
              sleep(0.02)
              step_count += 1
            
            else:
              #aici setam sa se roteasca in sensul contra acelor de ceasornic
	      #set the step motor to change its position in counter-clockwise
              GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
              sleep(0.02)
              step_count += 1
              GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
              sleep(0.02)
              step_count += 1
        
    #apasam CTRL+C pentru a inchide
    #press CTRL+C to shut the sys off
        except KeyboardInterrupt:
        
        
           print('motor oprit')
           sys.exit(0)
        with open ("Valori.txt","w") as f:
             f.write(str(nr))
    
#deoarece este o librarie de warm up, vom seta ca girueta sa arate inspre SUD
#because it's a warm up library made, we will set the step motor to show like a weathervane
#SUD
#south
motoras(0)
