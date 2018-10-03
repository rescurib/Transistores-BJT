#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:41:49 2018

@author: Rodolfo Escobar
         r.escurib@gmail.com
"""

import numpy as np

# Vss
# |
# R1
# |
# --- Vout = Vss*k_V
# |
# R2
# |
# GND

# 1/(1+k_r) = k_V
# 1 = k_V(1+k_r)
# 1/k_V - 1 = k_r

# Array de valores comerciales
Res10per = [100,120,150,180,220,227,330,390,470,560,680,820]

def k_r(k_V):
    """
    Esta función calcula la constante k_V de 
    la ecuación R2/(R2+k_V*R2) = k_V = Vout/Vin
    """
    kr = np.float(k_V) -1
    return kr

def div_i(Vcc,I,k_r):
    """
    Esta función calcula el valor de R2 dada
    una constante k_V y una restricción de
    corriente
    """
    R2 = Vcc/(I*(1+k_r))
    return R2

def closest(R,tol=10,err=0.1):
    """
    Esta función retorna el valor comercial con
    un margen de error "err". Si se retona 0, aumente 
    ligeramente el margen de error.
    """
    if tol==10:
        R1_com = 0
        for i in range(-2,6):
            for j in range(0,12):
                if (np.abs(R-Res10per[j]*10.0**i)<(R*err)):
                    R1_com = Res10per[j]*10.0**i
    return R1_com
        

def R1_given_R2(R2,k_r):
    R1 = k_r*R2
    return R1

def R2_given_R1(R1,k_r):
    R2 = R1/k_r
    return R2

