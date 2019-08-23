# -*- coding: utf-8 -*-
#%% Initialise the Keysight N5700 series DC power supply or the E364x DC power supply


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
inst2 = rm.open_resource('GPIB0::5::INSTR')  # Select the address of instrument displayed when you turn on the instrument.
print(inst2.query("*IDN?"))
inst2.write("*RST")
inst2.query("*TST?")

# inst2.write("INST:NSEL 1") # Select output in case of multiple outputs as in E3649A power supply

inst2.write("VOLT 12")

inst2.write("CURR:PROT:STAT 1.5")
inst2.write("CURR 0.4")

inst2.write("OUTP ON")

inst2.write("VOLT 0")

inst2.write("OUTP OFF")

