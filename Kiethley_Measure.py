# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import visa
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import time
rm = visa.ResourceManager()
rm.list_resources()
SaveMode=1;
#%% Initialise the Kiethley 2410 Voltage meter
inst2 = rm.open_resource('GPIB0::24::INSTR')
print(inst2.query("*IDN?"))
inst2.write("*RST")
inst2.query("*TST?")
#inst2.query("MEASure:CURRent?")
#inst2.query("MEASure:VOLTage?")
inst2.query("CONF?")
inst2.write("CONF:VOLT")

#%%
NumMeasurements=1000

Out1=np.zeros([NumMeasurements,1])
TimeSecMat=np.zeros([NumMeasurements,1])
TimeDateMat=np.chararray(NumMeasurements,13)
TimeHourMat=np.chararray(NumMeasurements,13)
for j in range(NumMeasurements):
    MEAS=inst2.query(":MEASure:VOLTage:DC?")
    ind=MEAS.find(',')
    Out1[j][0]=float(MEAS[0:ind])
#    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#for i in range(2000):
    TimeDateMat[j]=str(datetime.now().strftime('%Y-%m-%d:%H'))
    TimeHourMat[j]=str(datetime.now().strftime('%H:%M'))
    
    TimeSecMat=float(datetime.now().strftime('%S.%f'))
    
#%%
if SaveMode==1:
    filename=str(datetime.datetime.now().time()) +'.txt'
    np.savetxt(filename,Out1)
    np.savetxt(filename2, TimeMat1)
