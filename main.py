#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO
from time import sleep
while True:
    try:
        ADC = ADS1256.ADS1256()
        ADC.ADS1256_init()

    #while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        #print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
        print ("0 ADC = %lf"%(ADC_Value[0]/1677700))
        print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
       # print ("\33[9A")

        
    except :
        GPIO.cleanup()
        print ("\r\nProgram end     ")
        exit()
   # time.sleep(5)
