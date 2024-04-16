ROMANIAN:
Salutare, Acesta este un proiect de-al meu personal.
Am folosit un Raspberry PI model B, un shield ADDA Waveshare si am folosit ADS1256, 4 senzori DHT11, un accelerometru ADXL345, un motor de 3V folosit in mod generator, 
un joystick HW-504 pentru a selecta meniul de pe
un LCD conectat prin i2C, un fotorezistor, un senzor de gaze MQ-2 si un motor pas cu pas cu driver pentru a deservi pe post de girueta.
Proiectul a fost unul complex, am lasat in commit si fisierele CSV pentru date experimentale
Conexiunile i2C au fost realizate la nivelul ADXL345, LCD-ului, SPI a fost folosit pentru conexiunea ADDA Waveshare si Raspberry Pi, am folosit pini digitali pentru DHT11, 
iar pentru ADS1256 am conectat analogic la 
intrari bipolare multiplexare joystick-ul, fotorezistor-ul, senzorul de gaze si generatorul de 3V
Acest proiect are sansa de a fi conectat de la distanta cu ajutorul RaspController, poate avertiza in timp real prin SMTP anumite evenimente de tip natural 
(furtuni, cutremure, vijelii s.a.m.d.), poate detecta starea vremii, 
viteza vantului, si poate fi accesata prin intermediul unei baze de date de tip csv care poate fi apelata grafic prin tkinter de catre matplotlib.
Sper sa iti placa :)
Va mai urma :))

ENGLISH:
Hello, This is a personal project of mine.

I used a Raspberry Pi Model B, a Waveshare ADDA shield, and an ADS1256 ADC. I also incorporated 4 DHT11 sensors, an ADXL345 accelerometer, a 3V motor used as a generator, 
an HW-504 joystick for menu selection on an LCD connected via I2C, a photoresistor, an MQ-2 gas sensor, and a stepper motor with driver to serve as a weathervane.
The project was complex, and I left CSV files for experimental data in the commits.
I used I2C connections for the ADXL345 and LCD, SPI was used for the Waveshare ADDA connection to the Raspberry Pi, digital pins were used for the DHT11 sensors, 
and for the ADS1256, I connected analog inputs for the joystick, photoresistor, gas sensor, and 3V generator.
This project has the potential to be remotely accessed with RaspController. It can alert in real-time via SMTP for certain natural events (storms, earthquakes, hurricanes, etc.), detect weather conditions, wind 
speed, and can be accessed through a CSV database that can be graphically displayed via Tkinter with Matplotlib.
I hope you like it :)
More to come :))
