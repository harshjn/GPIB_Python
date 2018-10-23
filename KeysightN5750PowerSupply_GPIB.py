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
SaveMode=0;
#%% Initialise the Keysight N5750A Voltage meter
inst2 = rm.open_resource('GPIB0::5::INSTR')
print(inst2.query("*IDN?"))
inst2.write("*RST")
inst2.query("*TST?")

inst2.write("VOLT 12")

inst2.write("CURR:PROT:STAT 1.5")
inst2.write("CURR 0.4")

inst2.write("OUTP ON")


inst2.write("VOLT 0")

inst2.write("OUTP OFF")
