# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import visa
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

rm = visa.ResourceManager()
rm.list_resources()


#%%  Initialise the Keysight Voltage Source
#Send 12 Volts to the solenoid  Using Keysight E3649A
inst = rm.open_resource('GPIB0::5::INSTR')
print(inst.query("*IDN?"))
print(inst.query("SYST:VERS?"))
#print(inst.query("*ESR?"))
print(inst.write("*RST"))

inst.write("Output on")

#%%
NumReadings=5;
wait_time=10.0
TimeMat=np.zeros([NumReadings,4])
TimeSecMat1=np.zeros([NumReadings,1])
TimeDateMat1=np.chararray(NumReadings,13)
TimeHourMat1=np.chararray(NumReadings,13)
TimeSecMat2=np.zeros([NumReadings,1])
TimeDateMat2=np.chararray(NumReadings,13)
TimeHourMat2=np.chararray(NumReadings,13)
for i in range(NumReadings):
    
    
    inst.write("Voltage 12")
    TimeDateMat1[j]=str(datetime.now().strftime('%Y-%m-%d:%H'))
    TimeHourMat1[j]=str(datetime.now().strftime('%H:%M'))
    
    TimeSecMat1=float(datetime.now().strftime('%S.%f'))
   
    time.sleep(wait_time)
    
    inst.write("Voltage 0")
    TimeDateMat2[j]=str(datetime.now().strftime('%Y-%m-%d:%H'))
    TimeHourMat2[j]=str(datetime.now().strftime('%H:%M'))
    TimeSecMat2=float(datetime.now().strftime('%S.%f'))
   time.sleep(wait_time)
    
    
   

#%%
if SaveMode==1:
    filename=str(datetime.datetime.now().time()) +'.txt'
    np.savetxt(filename,TimeMat1)
    np.savetxt(filename2, TimeMat2)
