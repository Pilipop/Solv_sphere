#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 12:08:31 2023

@author: desdion
"""

import numpy as np
from molmass import ELEMENTS
from scipy import constants
from scipy.constants import physical_constants
import os
import sys
import subprocess
import shutil


a_0 = physical_constants["Bohr radius"][0]
centi = constants.centi
angstrom = constants.angstrom

################################################

dico_elem = {"1 ":"H ",
            "6 ": "C ",
            "8 ": "O ",
            "17": "Cl",
            "7 ": "N ",
            "20": "Ca"}


dico_elem_vis = {"H ":"1 ",
                "C ": "6 ",
                "O ": "8 ",
                "Cl": "C17",
                "N ": "7 ",
                "Ca": "20"}

#test avec git

################################################

#les choses à changer sont ici

# Name of the input file

######## Soyez sur que le xyz n'ait AUCUNE ligne vide apres la derniere ligne de coord
inp = "fen10_gb.xyz"

# N of atoms for water molecules ( if 20 H20 => 60 atoms :)))) )
n_of_wat = 30

# N of calcium (i don't know if exceding 1 it works)
n_of_cat = 1

# N wat + cat
n_of_wat_cat = n_of_cat + n_of_wat

# Same value as before but u have to kept the "\n"
n_of_Wat_Cat = "31\n"

# Number of atoms in the pesticide, keep the "\n"
n_of_a_pest = "36\n"
n_of_p = 36

################################################

### Solvatation Criteria

# For the moment it's arbitrary 

criteria_O_H = 3.0
criteria_O_N = 3.5
criteria_O_C = 3.5
criteria_O_O = 4.0
criteria_O_Cl = 4.0

criteria_H_H = 3.0
criteria_H_N = 3.5 
criteria_H_C = 3.0
criteria_H_Cl = 3.0


# Not arbitrary anymore cf: # article de J. L. Fulton J. Phys. Chem

criteria_Ca_O = 2.8
criteria_Ca_H = 3.0
criteria_Ca_Cl = 2.8
#criteria_Ca_O_H = 3.0
#criteria_Ca_H je ne pense pas qu'il ait de sens

################################################

# ici on va juste faire une copie du fichier pour pas le saccager
# uncomment if you wanna save your inp

#shutil.copyfile('fen5_gb.xyz', 'fen5_gb_backup.xyz')


################################################## PART 1

#ici on va preparer le fichier .xyz en .dat et convertir les atomes

# In this part we will prepare the inp into 3 files that are used in the 2 next classes
# a pest.dat, made by a sh script (but i will probably code it in python soon)
# a cat.dat and a wat.dat already in the python code

xyz = open(inp, "rt")
txt_p1 = open("p1.txt", "wt")

for line in xyz:
    txt_p1.write(line.replace('Ca', '20'))


txt_p1 = open("p1.txt", "rt")
txt_p2 = open("p2.txt", "wt")

for line in txt_p1:
    txt_p2.write(line.replace('C ', '6 '))

txt_p2 = open("p2.txt", "rt")
txt_p3 = open("p3.txt", "wt")

for line in txt_p2:
    txt_p3.write(line.replace('H ', '1 '))

txt_p3 = open("p3.txt", "rt")
txt_p4 = open("p4.txt", "wt")

for line in txt_p3:
    txt_p4.write(line.replace('O ', '8 '))
    
txt_p4 = open("p4.txt", "rt")
txt_p5 = open("p5.txt", "wt")

for line in txt_p4:
    txt_p5.write(line.replace('Cl ', '17 '))    

txt_p5 = open("p5.txt", "rt")
txt_p6 = open("p6.txt", "wt")

for line in txt_p5:
    txt_p6.write(line.replace('N ', '7 '))        
    


txt_p1.close()
txt_p2.close()
txt_p3.close()
txt_p4.close()
txt_p5.close()
txt_p6.close()
xyz.close()

#######

fileW = open("pest.dat", "w")
fileW.write(n_of_a_pest)
fileW.close() 
 

subprocess.call('./Prep_cut.sh')

########

fileR = open("try_3", "r")
text = fileR.read()
fileR.close()
 
 
fileW = open("try_4", "w")
fileW.write(n_of_Wat_Cat + text)
fileW.close() 

try_path = 'try.txt'
try_2_path = 'try_2.txt'


shutil.copyfile('try_4', 'try_4_backup')

########################################### Water cutting in the file 

with open("try_4", "r") as input:
    with open("try_4_v2", "w") as output:
        # iterate all lines from file
        for line in input:
            # if line starts with substring 'time' then don't write it in temp file
            if not line.strip("\n").startswith('20 '):
                output.write(line)

# replace file with original name
os.replace('try_4_v2', 'try.txt')

quoicoubeh = open("try.txt", "rt")
apanyan = open("wat.dat", "wt")

for line in quoicoubeh:
    apanyan.write(line.replace(str(n_of_wat_cat), str(n_of_wat)))
quoicoubeh.close()
apanyan.close()
###########################################

########################################### Cation cutting in the file 

with open("try_4", "r") as input:
    with open("try_4_v3", "w") as output:
        # iterate all lines from file
        for line in input:
            # if line starts with substring 'time' then don't write it in temp file
            if not line.strip("\n").startswith('1 ') and not line.strip("\n").startswith('8 ') :
#            if not line.strip("\n").startswith('1 '):    
                output.write(line)

# replace file with original name
os.replace('try_4_v3', 'try_v2.txt')

quoicoubeh = open("try_v2.txt", "rt")
apanyan = open("cat.dat", "wt")

for line in quoicoubeh:
    apanyan.write(line.replace(str(n_of_wat_cat), str(n_of_cat)))
quoicoubeh.close()
apanyan.close()


################################################


################################################## PART 2

### So this is the Class Molecule which calculate the near neighbours of the pesticide
# the cation isn't take in account


class Molecule:

    def __init__(self):
        self.atom_charges = NotImplemented  # type: np.ndarray
        self.atom_coords = NotImplemented  # type: np.ndarray
        self.natm = NotImplemented  # type: int
        
    def __init2__(self):
        self.atom_charges_2 = NotImplemented  # type: np.ndarray
        self.atom_coords_2 = NotImplemented  # type: np.ndarray
        self.natm_2 = NotImplemented  # type: int
            
        
        
        
########################################

#### fichier pest
        
    def construct_from_dat_file(self, file_path: str):
        # Input: Read file from `file_path`
        # Attribute modification: Obtain atom charges to `self.atom_charges`
        # Attribute modification: Obtain coordinates to `self.atom_coords`
        # Attribute modification: Obtain atom numbers in molecule to `self.natm`
        with open(file_path, "r") as f:
            # Ignore the redundant first line
            dat_1 = np.array([line.split() for line in f.readlines()][1:])
            self.atom_charges = np.array(dat_1[:, 0], dtype=int)
            self.atom_coords = np.array(dat_1[:, 1:4], dtype=float)
            self.natm = self.atom_charges.shape[0]
            
 

########################################  

#### fichier eau
          
    def construct_from_dat_file_2(self, file_path: str):
        # Input: Read file from `file_path`
        # Attribute modification: Obtain atom charges to `self.atom_charges`
        # Attribute modification: Obtain coordinates to `self.atom_coords`
        # Attribute modification: Obtain atom numbers in molecule to `self.natm`
        with open(file_path, "r") as j:
            # Ignore the redundant first line
            dat_2 = np.array([line.split() for line in j.readlines()][1:])
            self.atom_charges_2 = np.array(dat_2[:, 0], dtype=int)
            self.atom_coords_2 = np.array(dat_2[:, 1:4], dtype=float)
            self.natm_2 = self.atom_charges_2.shape[0]
            
#            print(self.natm_2) 
#            print(self.atom_charges_2)
#            print(self.atom_coords_2)         
################################################

# petit calcul des d entre f1 et f2
# en fait je pense même pas que ça soit utile je crois que je l'appelle jamais 
    
    def bond_length(self, i: int, j: int) -> float:
        # Input: `i`, `j` index of molecule's atom
        # Output: Bond length from atom `i` to atom `j`
        return np.linalg.norm(self.atom_coords[i] - self.atom_coords_2[j])


    def print_bond_length(self): 
        # Usage: Print all bond length
        print("=== d entre a_pesticide et a_eau(x) ===")
        with open(pesticide_path,"w") as file:
            for i in range(self.natm):
                for j in range(self.natm_2):

                    
#######################################
#### Discrimination depuis l'Oxygene de l'eau

# pour la partie print de la Molecule d'eau je n'ai plus qu'à changer self.atom_charge par _coord

            
                    if  (self.atom_charges_2[j] == 8):

                        if (self.atom_charges[i] == 1) and (self.bond_length(i, j)<= criteria_O_H):
#                            print("===== Molecule(s) Eau(x) (O) proche d'un H pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
                                    
#                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )

###### on va essayer de lui faire écrire charge puis coord

#                                    file.write(str(self.atom_charges_2[j]) + " ")
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
###### 
        
                        elif (self.atom_charges[i] == 8) and (self.bond_length(i, j)<= criteria_O_O):
#                            print("===== Molecule(s) Eau(x) (O) proche d'un O pest =====")
#                            print( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")

                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
#                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )

                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)

    #                                print(self.atom_charges_2[j],self.atom_charges_2[h], M_H2O)
    
                            
                        elif (self.atom_charges[i] == 6) and (self.bond_length(i, j)<= criteria_O_C):

#                            print("===== Molecule(s) Eau(x) (O) proche d'un C pest =====")
#                            print( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                            
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
#                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                            
                        elif (self.atom_charges[i] == 7) and (self.bond_length(i, j)<= criteria_O_N):

#                            print("===== Molecule(s) Eau(x) (O) proche d'un N pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                                                        
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
#                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                        elif (self.atom_charges[i] == 17) and (self.bond_length(i, j)<= criteria_O_Cl):
#                            print("===== Molecule(s) Eau(x) (O) proche d'un Cl pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                                                        
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
#                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
     

                            
#### Discrimination depuis l'Hydrogene de l'eau

                    if  (self.atom_charges_2[j] == 1):

                        if (self.atom_charges[i] == 1) and (self.bond_length(i, j) <= criteria_H_H):
#                            print("===== Molecule(s) Eau(x) (H) proche d'un H pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            
                                 
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
#                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                            
                            
                        elif (self.atom_charges[i] == 8) and (self.bond_length(i, j)<= criteria_O_H):
                            
#                            print("===== Molecule(s) Eau(x) (H) proche d'un O pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
#                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                                              
                        elif (self.atom_charges[i] == 6) and (self.bond_length(i, j)<= criteria_H_C):

#                            print("===== Molecule(s) Eau(x) (H) proche d'un N pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
 #                                           print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
     
                            
                        elif (self.atom_charges[i] == 7) and (self.bond_length(i, j)<= criteria_H_N):
#                            print("===== Molecule(s) Eau(x) (H) proche d'un N pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
 #                                           print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                                            
                                            
                        
                        elif (self.atom_charges[i] == 17) and (self.bond_length(i, j)<= criteria_H_Cl):
#                            print("===== Molecule(s) Eau(x) (H) proche d'un Cl pest =====")
#                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
#                                           print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 

##############################################################


    def print_solution_01(self):
        print("=== Atom Charges Pesticide ===")
        print(self.atom_charges)
        print("=== Atom Charges Eau(x) ===")
        print(self.atom_charges_2)
        print("=== Coordinates Pesticide ===")
        print(self.atom_coords)
        print("=== Coordinates Eau(x) ===")
        print(self.atom_coords_2)
#        print("=== d entre a_pesticide et a_eau(x) ===")

        self.print_bond_length()


################################################ PART 3

### So this is the Class Clation which calculate the near neighbours of the cation
# the pesticde isn't take in account

class Cation:
    
    def __init__(self):
        self.atom_charges_2 = NotImplemented  # type: np.ndarray
        self.atom_coords_2 = NotImplemented  # type: np.ndarray
        self.natm_2 = NotImplemented  # type: int
        
    def __init3__(self):
        self.atom_charges_3 = NotImplemented  # type: np.ndarray
        self.atom_coords_3 = NotImplemented  # type: np.ndarray
        self.natm_3 = NotImplemented  # type: int   
        
        
        
        
        
    def construct_from_dat_file_2(self, file_path: str):
        # Input: Read file from `file_path`
        # Attribute modification: Obtain atom charges to `self.atom_charges`
        # Attribute modification: Obtain coordinates to `self.atom_coords`
        # Attribute modification: Obtain atom numbers in molecule to `self.natm`
        with open(file_path, "r") as j:
            # Ignore the redundant first line
            dat_2 = np.array([line.split() for line in j.readlines()][1:])
            self.atom_charges_2 = np.array(dat_2[:, 0], dtype=int)
            self.atom_coords_2 = np.array(dat_2[:, 1:4], dtype=float)
            self.natm_2 = self.atom_charges_2.shape[0]
            
#            print(self.natm)
#            print(self.atom_charges)
#            print(self.atom_coords)
        
#### fichier cat
          
    def construct_from_dat_file_3(self, file_path: str):
        # Input: Read file from `file_path`
        # Attribute modification: Obtain atom charges to `self.atom_charges`
        # Attribute modification: Obtain coordinates to `self.atom_coords`
        # Attribute modification: Obtain atom numbers in molecule to `self.natm`
        with open(file_path, "r") as j:
            # Ignore the redundant first line
            dat_3 = np.array([line.split() for line in j.readlines()][1:])
            self.atom_charges_3 = np.array(dat_3[:, 0], dtype=int)
            self.atom_coords_3 = np.array(dat_3[:, 1:4], dtype=float)
            self.natm_3 = self.atom_charges_3.shape[0]
            
#            print(self.natm_2) 
#              print(self.atom_charges_2)
#            print(self.atom_coords_2)             
        
########################### calcul sphere 2_3

    def bond_length_2(self, k: int, l: int) -> float:
        # Input: `i`, `j` index of molecule's atom
        # Output: Bond length from atom `i` to atom `j`
        return np.linalg.norm(self.atom_coords_2[k] - self.atom_coords_3[l])

    def print_bond_length_2(self):
        # Usage: Print all bond length
        
        
        
#        print("=== Bond Length ===")
        with open(cation_path,"w") as file:
            for k in range(self.natm_2):
                for l in range(self.natm_3):
#                print("{:3d} - {:3d}: {:10.5f} Bohr".format(i, j, self.bond_length(i, j)))

# bon la c'est une version de blédard, il me dit oui non si c'est dans ce que j'ai defini par radius
# Enlever les # pour tout print 



#                print((self.atom_coords_2[k], self.atom_coords_3[l], self.bond_length_2(k, l)))
#                    if  self.bond_length_2(k, l) <= radius_2_3:
                    
                    if  (self.atom_charges_2[k] == 8) and (self.bond_length_2(k, l)<= criteria_Ca_O):
                        print("===== Molecule(s) Eau(x) (O) proche d'un Ca =====")
                        print ( "d ",self.atom_charges_3[l],"Ca","_", self.atom_charges_2[k],"eau","=" ,self.bond_length_2(k, l),"A")
                        for h in range(self.natm_2):
                            
                            M_H2O = np.linalg.norm(self.atom_coords_2[k] - self.atom_coords_2[h])
                            
                            if (M_H2O <= 1.0) and (M_H2O!= 0.0):    
                    
                                    print(" | ", self.atom_charges_2[k]," | "," | ",self.atom_coords_2[k]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[k]) + " " + str(self.atom_coords_2[k]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                                    


 
     
                    elif (self.atom_charges_2[k] == 1) and (self.bond_length_2(k, l) <= criteria_Ca_H):
                        
                        print("===== Molecule(s) Eau(x) (H) proche d'un Ca  =====")
                        print ( "d ",self.atom_charges_3[l],"Ca","_", self.atom_charges_2[k],"eau","=" ,self.bond_length_2(k, l),"A")                            

                    
                        for h in range(self.natm_2):
                            M_H2O = np.linalg.norm(self.atom_coords_2[k] - self.atom_coords_2[h])
                            
                            if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                    
                                for n in range(self.natm_2):
                                    M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                    
                                    if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                        print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                        
                                        file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                        file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                   
################################################


    def print_solution_02(self):
        print("=== Atom Charges Cation(s) ===")
        print(self.atom_charges_3)
        print("=== Atom Charges Eau(x) ===")
        print(self.atom_charges_2)
        print("=== Coordinates Cation(s) ===")
        print(self.atom_coords_3)
        print("=== Coordinates Eau(x) ===")
        print(self.atom_coords_2)
        print("=== d entre a_cation(s) et a_eau(x) ===")
        self.print_bond_length_2()

################################################ 

######### à suppr, c'est un essaie pour essayer de faire check le label de l'atome
# en fait non je suis con


pesticide_path = 'pesticide.txt'
cation_path = 'cation.txt'



###################


    
if __name__ == '__main__':
    mole = Molecule()
    mole.construct_from_dat_file("pest.dat")
    mole.construct_from_dat_file_2("wat.dat")
    mole.print_solution_01()

if __name__ == '__main__':
    
    cat = Cation()
    cat.construct_from_dat_file_2("wat.dat")
    cat.construct_from_dat_file_3("cat.dat")
    cat.print_solution_02()

################################################## PART 4

# just there we will transform our both .txt into something with only unique lines
# because our code return all neighbours but a water molecule can appear multiple times
# eh mon anglais est degueu

uniqlines_1 = set(open('pesticide.txt').readlines())
uniqlines_pest = open('uniqlines_pest', 'w').writelines(uniqlines_1)
print(uniqlines_1) 

uniqlines_2 = set(open('cation.txt').readlines())
uniqlines_pest = open('uniqlines_cat', 'w').writelines(uniqlines_2)
print(uniqlines_2)    

# this is the rythm of the night, oh yeaaaaaaaaaaaaaaaaaaah
######## on enleve les crochets fichier sphere cation
# we adapt our file to make it readable
# but in the end there number of atom in the first line is missing .. so

u_cat = open("uniqlines_cat", "rt")
f_cat = open("cat_f", "wt")

for line in u_cat:
    
    f_cat.write(line.replace('[', ' '))
    
u_cat.close()
f_cat.close()

u_cat = open("cat_f", "rt")
ff_cat = open("cat_sphere.xyz", "wt")

for line in u_cat:
    
    ff_cat.write(line.replace(']', ' '))
    
u_cat.close()
ff_cat.close()

######## on enleve les crochets fichier sphere Pest

u_pest = open("uniqlines_pest", "rt")
f_pest = open("pest_f", "wt")

for line in u_pest:
    
    f_pest.write(line.replace('[', ' '))
    
u_pest.close()
f_pest.close()

u_pest = open("pest_f", "rt")
ff_pest = open("pest_sphere.xyz", "wt")

for line in u_pest:
    
    ff_pest.write(line.replace(']', ' '))
    
u_pest.close()
ff_pest.close()

#############################################
# Creation of the xyz file

n_n_fin_cat_wat = sum(1 for _ in open('cat_sphere.xyz'))
n_fin_cat_wat = n_n_fin_cat_wat + n_of_cat
fileW = open("cat_wat.xyz", "w")
fileW.write(str(n_fin_cat_wat)+os.linesep)
fileW.write(os.linesep)
fileW.close()



n_n_fin_pest_wat = sum(1 for _ in open('pest_sphere.xyz'))
n_fin_pest_wat = n_n_fin_pest_wat + n_of_p
fileW = open("pest_wat.xyz", "w")
fileW.write(str(n_fin_pest_wat)+ os.linesep)
fileW.write(os.linesep)
fileW.close()




subprocess.call('./reu_one.sh')



fileR = open("pest_wat.xyz", "r")
fileW = open("pest_wat_f.xyz","w")
check = 0
for line in fileR:
    if check>=2:
        fileW.write(line[0:2].replace(str(line[0:2]), str(dico_elem.get(line[0:2])))+line[2:])
    else:
        fileW.write(line)    
    check += 1

fileW.close()
fileR.close()


fileR = open("cat_wat.xyz", "r")
fileW = open("cat_wat_f.xyz","w")
check = 0
for line in fileR:
    if check>=2:
        fileW.write(line[0:2].replace(str(line[0:2]), str(dico_elem.get(line[0:2])))+line[2:])
    else:
        fileW.write(line)    
    check += 1

fileW.close()
fileR.close()



#### Merci Aurelien  



#############################################
# as there is a lot of file created with my stupid code, i have to delete it


os.remove("p1.txt")
os.remove("p2.txt")
os.remove("p3.txt")
os.remove("p4.txt")
os.remove("p5.txt")
os.remove("p6.txt")
os.remove("pest_f")
os.remove("cat_f")
os.remove("try_3")
os.remove("try_4")
os.remove("try_4_backup")
os.remove("try_v2.txt")
os.remove("try.txt")

## à commenter si probleme avec la sortie des m_h2O 

os.remove("uniqlines_cat")
os.remove("uniqlines_pest")
os.remove("pesticide.txt")
os.remove("cation.txt")

## à commenter si problème dans les classes pour regarder les inputs

os.remove("cat.dat")
os.remove("pest.dat")
os.remove("wat.dat")

##

os.remove("pest_n_less.dat")
os.remove("pest_sphere.xyz")
os.remove("cat_temp.dat")
os.remove("cat_sphere.xyz")
os.remove("cat_wat.xyz")
os.remove("pest_wat.xyz")

