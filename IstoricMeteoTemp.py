from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

data = pd.read_csv('dht_date_temporare.csv')

x = data['Data'].tolist()
y = data['Temperatura'].tolist()
z = data['Umiditatea'].tolist()
a = data['Viteza Vant'].tolist()

grafic = Tk()
grafic.title("Date Meteorologice")

def functieTemp():
  #realizam o functie pentru animarea in timp real a valorilor intr-un grafic
  plot1,ax1 = plt.subplots()
  ax1.plot(x,y, linestyle='solid',color = "green",label= "Temperatura")
  ax1.set_title("Temperatura medie")
  ax1.set_xlabel("Perioada")
  ax1.legend()
  ax1.set_ylabel("Valori t*C")
  ax1.set_ylim([0,50])
  plt.tight_layout()
  plt.show()

def functieUmiditate():
  plot2,ax2 = plt.subplots()  
  ax2.plot(x,z, linestyle='dotted',color = "red", label='Umiditate')
  ax2.set_title("Umiditate medie")
  ax2.set_xlabel("Perioada")
  ax2.set_ylabel("Valori umiditate %")
  ax2.set_ylim([10,70])
  #ax2.set_xlim([0,3])
  ax2.legend()
  plt.tight_layout()
  plt.show()

def functieToate():
  plot3,ax3 = plt.subplots() 
  ax3.plot(x,y,color = 'red',label = "Temperatura")
  ax3.plot(x,z,'yellow',label = "Umiditate")
  ax3.plot(x,a,"blue",label = "Viteza Vant")
  ax3.set_title("Raport Temperatura+Umiditate")
  ax3.set_xlabel("Perioada")
  ax3.set_ylabel("Valori")
  ax3.set_ylim([0,70])
  #ax3.set_xlim([0,3])
  ax3.legend()
  plt.tight_layout()
  plt.show()

def functieVitezaVant():
  plot4,ax4 = plt.subplots()
  ax4.plot(x,y,color = 'blue',label = "Viteza vant")
  #ax4.plot(x,z,'yellow',label = "Umiditate")
  ax4.set_title("Viteza Vant")
  ax4.set_xlabel("Perioada")
  ax4.set_ylabel("Valori (km/h)")
  ax4.set_ylim([0,100])
  plt.tight_layout()
  plt.show()

# buton pentru functia aflarii tensiunii - canal 0
buton0 = Button(grafic, text="Temperatură - istoric temporar", command=functieTemp, padx=25, pady=5).grid(row=0, column=0)
# buton pentru functia aflarii tensiunii - canal 1
buton1 = Button(grafic, text="Umiditate - istoric temporar", command=functieUmiditate, padx=25, pady=5).grid(row=1, column=0)
# buton pentru functia aflarii tensiunii - canal 2
buton2 = Button(grafic, text="Istoric total temporar", command=functieToate, padx=25, pady=5).grid(row=0, column=1)
# buton pentru functia aflarii tensiunii - canal 3
buton3 = Button(grafic, text="Viteză vânt- istoric temporar", command=functieVitezaVant, padx=25, pady=5).grid(row=1, column=1)

grafic.mainloop()

