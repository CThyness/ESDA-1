# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 13:17:29 2020

@author: carlt
"""

import csv
import matplotlib.pyplot as plt
from math import *

R = 1000

def L_estimat(H, w):
    return R/(w*sqrt(H**(-2) - 1))

#header = []
data = []


filename = "Leq_4.csv"
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    #header = next(csvreader)

    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
    #print(data)
#print(header)

f = [(p[0]) for p in data]  #Husk: Dette tallet er i frekvens
#ch1 = [p[1] for p in data]  Denne kommer bare til å være V av V (100%)
ch2 = [p[2] for p in data]  #Amplitudeandel ch2 av ch1
#ch3 = [p[3] for p in data]  #Faseforskyvning

inductance = []

for i in range(0, len(ch2)):
    L = L_estimat(ch2[i]/100, f[i]*2*pi)
    inductance.append(L)

print(sum(inductance)/len(inductance))  #returner gjennomsnittsverdien til induktansestimatene
    