#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:50:23 2024

@author: yowenpierre
"""

import csv

import pandas as pd

import numpy as np
GG = pd.read_csv("artists.csv")
teste = [['id_genre', 'id_artiste']]
GG.drop_duplicates(subset = ["artists"], inplace = True)

def fonctiontest():
    B=[['id_artiste', 'artiste']]
    for k in range(1,len(GG)):
        B.append([str(GG.iloc[k, 0]), str(GG.iloc[k, 4])])
    return B 

IDNOM=fonctiontest()
        
def montre(matrice, motachercher,k):
    B=str(matrice.iloc[k, 2])
    if motachercher in B:
        return 1

def modif(MAT, longueurfichier):
    a=0
    b=0
    for k in range(1,longueurfichier):
        if montre(MAT,'house',k)==1:
            a='house' 
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'hip hop',k)==1:
            a='hip hop'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'pop',k)==1:
            a='pop'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'amapiano',k)==1:
            a='amapiano'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'funk',k)==1:
            a='funk'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'v-pop',k)==1:
           a='v-pop'
           b= str(MAT.iloc[k, 0])
           M=([a, b])
           teste.append(M)
        if montre(MAT,'cumbia',k)==1:
            a='cumbia'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'k-pop',k)==1:
            a='k-pop'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'trap',k)==1:
            a='trap'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'rap',k)==1:
            a='rap'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'country',k)==1:
            a='country'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'r&b',k)==1:
            a='r&b'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'dembow',k)==1:
            a='dembow'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'corrido',k)==1:
            a='corrido'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'rock',k)==1:
            a='rock'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'sierreno',k)==1:
            a='sierreno'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'drill',k)==1:
            a='drill'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'bachata',k)==1:
            a='bachata'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
        if montre(MAT,'urbano latino',k)==1:
            a='urbano latino'
            b= str(MAT.iloc[k, 0])
            M=([a, b])
            teste.append(M)
    return teste 


try:
    with open('id_genre_id_artist2.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(modif(GG,len(GG)))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
