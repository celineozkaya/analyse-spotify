#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:44:28 2024

@author: yowenpierre
"""

import csv

import pandas as pd

import numpy as np
OCEANIA = pd.read_csv("Oceania.csv")
south_america= pd.read_csv("South_America.csv")
europe= pd.read_csv("Europe.csv")
africa= pd.read_csv("Africa.csv")
central_america= pd.read_csv("Central_America.csv")
north_america= pd.read_csv("North_America.csv")
asia= pd.read_csv("Asia.csv")


def moyenepays(matrice,pays,attribue):
    return matrice[matrice['country'] == pays][attribue].mean()


def indic(matrice):
    edges_list = []
    Listepays=matrice["country"].unique()
    ListeAttribut=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
    for pays in Listepays:
        for attribut in ListeAttribut:
            if moyenepays(matrice, pays, attribut) > matrice[attribut].mean() :
                edges_list.append([pays, attribut])
    return edges_list
        

def nodes(matrice):
    Listepays=matrice["country"].unique()
    ListeAttribut=['danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo']
    NODES= []
    for k in range(len(Listepays)):
        NODES.append((Listepays[k]))
    for i in range(len(ListeAttribut)):
        NODES.append((ListeAttribut[i]))
    return NODES  
    
def list_to_csv(input_list, file_name):
    """
    Write a 1D Python list to a single-column CSV file.

    Parameters:
    input_list (list): The 1D list to be written.
    file_name (str): The name of the CSV file to write to.

    Returns:
    None
    """
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write each element of the list as a new row
        for item in input_list:
            writer.writerow([item])
            

try:
    with open('edges_OCEANIA.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(OCEANIA))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
try:
    with open('edges_ASIA.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(asia))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('edges_Africa.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(africa))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('edges_Europe.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(europe))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('edges_north_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(north_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('edges_central_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(central_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
try:
    with open('edges_south_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(south_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")


      
    
try:
    with open('edges_south_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(indic(south_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
    
    
#fichier NODES 

try:
    with open('nodes_OCEANIA.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(OCEANIA))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
try:
    with open('nodes_ASIA.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(asia))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('nodes_Africa.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(africa))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('nodes_Europe.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(europe))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('nodes_north_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(north_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

try:
    with open('nodes_central_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(central_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
try:
    with open('nodes_south_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(south_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")

    
try:
    with open('nodes_south_america.csv', 'x', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(nodes(south_america))
    print("Le fichier a été créé avec succès.")
except FileExistsError:
    print("Le fichier existe déjà.")
    
