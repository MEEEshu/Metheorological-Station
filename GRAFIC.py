
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd


#realizam o functie pentru animarea in timp real a valorilor intr-un grafic
#we define a function to animate in real time the values in a graph
def animate(i):
    data = pd.read_csv('dht_date_temporare.csv')
    x = data['Data']
    
    y = data['Temperatura']
    
    z = data['Umiditatea']
    plt.cla() 
    plt.plot(y, linestyle='solid', label='Temperatura')
    plt.plot(z, linestyle='--', label='Umiditate')
    #plt.plot(1,x)
    plt.ylim(10, 60)
    
    plt.legend()
    
    


