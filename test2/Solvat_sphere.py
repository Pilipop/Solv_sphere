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
import subprocess
import shutil


a_0 = physical_constants["Bohr radius"][0]
centi = constants.centi
angstrom = constants.angstrom





################################################

n_of_wat = 15
n_of_cat = 1
n_of_Wat_Cat = "16\n"

################################################

radius_1_2 = 4.0  # Radius of the solvation sphere pest 
radius_2_3 = 2.0  # Radius of the solvation sphere cat
cr = 1

### critère solv
#actuellemnt c'est arbitraire 

criteria_O_H = 3.0
criteria_O_N = 3.5
criteria_O_C = 3.5
criteria_O_O = 4.0
criteria_O_Cl = 4.0

criteria_H_H = 4.0
criteria_H_N = 3.5 
criteria_H_C = 3.0
criteria_H_Cl = 3.0
# ici ce n'est plus arbitraire # article de J. L. Fulton J. Phys. Chem

criteria_Ca_O = 2.8
criteria_Ca_H = 3
criteria_Ca_Cl = 2.8
criteria_Ca_O_H = 3.0
#criteria_Ca_H je ne pense pas qu'il ait de sens

################################################

# ici on va juste faire une copie du fichier pour pas le saccager



shutil.copyfile('fen5_gb.xyz', 'fen5_gb_backup.xyz')




##################################################
#ici on va preparer le fichier .xyz en .dat et convertir les atomes



xyz = open("fen5_gb.xyz", "rt")
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


# print("i did it")

# z = 0
# with open("p6.txt", 'r') as hello:
# #    kek() = hello.readlines(z)
#     while z != 36:
    
#         print(hello.readline()[z])
        
#         z = z + 1


#########################

subprocess.call('./Prep_cut.sh')


# def filtre(try_3, try_4):
#     fs = open(try_3, 'r')
#     fd = open(try_4, 'w')
#     txt = fs.readline()
#     while txt:
#         if txt[:6] == '20':
#             fd.write(txt+'\n')
#             txt = fs.readline()
#     fs.close()
#     fd.close()



fileR = open("try_3", "r")
text = fileR.read()
fileR.close()
 
 
fileW = open("try_4", "w")
fileW.write(n_of_Wat_Cat + text)
 
fileW.close() 

class wat_cat:
    
    def __init__(self):
        self.atom_charges_w = NotImplemented  # type: np.ndarray
        self.atom_coords_w = NotImplemented  # type: np.ndarray
        self.natm_w = NotImplemented  # type: int


    def construct_from_dat_file_wat_cat(self, file_path: str):
        with open(file_path,"r") as p:
            

            
            dat_w = np.array([line.split() for line in p.readlines()][1:])
               
            self.atom_charges_w = np.array(dat_w[:, 0], dtype=int)
            
            self.atom_coords_w = np.array(dat_w[:, 1:4], dtype=float)
            self.natm_w = self.atom_charges_w.shape[0]
            
    def print_bond_length(self):      
            
            with open(try_path,"w") as file:
                file.write(str(n_of_wat)+ os.linesep)
                for b in range(self.natm_w):
                    if  (self.atom_charges_w[b] != 20):
                        file.write(str(self.atom_charges_w[b]) + " " + str(self.atom_coords_w[b]) + os.linesep)
                        
                        
    def construct_from_dat_file_wat_cat_2(self, file_path: str):
        with open(file_path,"r") as p:
            
            dat_w = np.array([line.split() for line in p.readlines()][1:])
               
            self.atom_charges_w = np.array(dat_w[:, 0], dtype=int)
            
            self.atom_coords_w = np.array(dat_w[:, 1:4], dtype=float)
            self.natm_w = self.atom_charges_w.shape[0]
            
            with open(try_2_path,"w") as file:
                file.write(str(n_of_cat)+ os.linesep)
                for b in range(self.natm_w):
                    if  (self.atom_charges_w[b] == 20):
                        file.write(str(self.atom_charges_w[b]) + " " + str(self.atom_coords_w[b]) + os.linesep)                        
                        
                        
                        
                      

## si ça marche, transformer wat.dat.dat.dat en .dat

u_inp = open("try.txt", "rt")
f_inp = open("wat.dat.dat", "wt")

for line in u_inp:
    
    f_inp.write(line.replace('[', ' '))
    
u_inp.close()
f_inp.close()

u_inp = open("wat.dat.dat", "rt")
ff_inp = open("wat.dat.dat.dat", "wt")

for line in u_inp:
    
    ff_inp.write(line.replace(']', ' '))
    
u_inp.close()
ff_inp.close()
                       

  
## si ça marche, transformer wat.dat.dat.dat en .dat

u_inp_2 = open("try_2.txt", "rt")
f_inp_2 = open("cat.dat.dat", "wt")

for line in u_inp_2:
    
    f_inp_2.write(line.replace('[', ' '))
    
u_inp_2.close()
f_inp_2.close()

u_inp_2 = open("cat.dat.dat", "rt")
ff_inp_2 = open("cat.dat.dat.dat", "wt")

for line in u_inp_2:
    
    ff_inp_2.write(line.replace(']', ' '))
    
u_inp_2.close()
ff_inp_2.close()
                       
print("cat.dat.dat.dat")    
                
         
        
                    



##################################################


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
            
            


            
#            print(self.natm)
#            print(self.atom_charges)
#            print(self.atom_coords)

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
    
    def bond_length(self, i: int, j: int) -> float:
        # Input: `i`, `j` index of molecule's atom
        # Output: Bond length from atom `i` to atom `j`
        return np.linalg.norm(self.atom_coords[i] - self.atom_coords_2[j])

################################################################ ici ça marche 12h58 jeudi 27 juillet

#    def print_bond_length(self):
        # Usage: Print all bond length
#        print("=== Bond Length ===")
#        for i in range(self.natm):
#            for j in range(self.natm_2):
#                print("{:3d} - {:3d}: {:10.5f} Bohr".format(i, j, self.bond_length(i, j)))
                
# actuellement il me calcul bien toutes les d entre f1 et f2                



#                print((self.atom_coords[i], self.atom_coords_2[j], self.bond_length(i, j)))
#                if  self.bond_length(i, j) <= radius_1_2:
#                    print("oui_pest",(self.atom_coords[i], self.atom_coords_2[j], self.bond_length(i, j)))

#                    with open(pesticide_path,"w") as file:
#                        file.writelines(str(self.bond_length(i, j))+ os.linesep)

#                if  self.bond_length(i, j) <= radius_1_2:
#                    print("oui_pest",(self.atom_coords[i], self.atom_coords_2[j], self.bond_length(i, j)))

#                    with open(pesticide_path,"w") as file:
#                        file.writelines(str(self.bond_length(i, j))+ os.linesep)                    

#                else:
#                    print("non_pest")  
                    
##############################################################

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
                            print("===== Molecule(s) Eau(x) (O) proche d'un H pest TEEEEEEEEEESSSSSSSSSTTTTTTT =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
                                    
                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )

###### on va essayer de lui faire écrire charge puis coord

#                                    file.write(str(self.atom_charges_2[j]) + " ")
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
###### 
        
                        elif (self.atom_charges[i] == 8) and (self.bond_length(i, j)<= criteria_O_O):
#                            print("===== Tentative de discrimination Oxygene - Oxygene =====")
#                            print(self.atom_charges_2[j],self.atom_charges[i] ,self.bond_length(i, j) )
                            print("===== Molecule(s) Eau(x) (O) proche d'un O pest =====")
                            print( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")

                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )

                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)

    #                                print(self.atom_charges_2[j],self.atom_charges_2[h], M_H2O)
    
                            
                        elif (self.atom_charges[i] == 6) and (self.bond_length(i, j)<= criteria_O_C):
#                            print("===== Tentative de discrimination Oxygene - Carbone =====")
#                            print(self.atom_charges_2[j],self.atom_charges[i] ,self.bond_length(i, j) )

                            print("===== Molecule(s) Eau(x) (O) proche d'un C pest =====")
                            print( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
#                            print(self.atom_coords_2[j])
                            
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                            
                        elif (self.atom_charges[i] == 7) and (self.bond_length(i, j)<= criteria_O_N):
#                            print("===== Tentative de discrimination Oxygene - Azote =====")
#                            print(self.atom_charges_2[j],self.atom_charges[i] ,self.bond_length(i, j) ) 
                            print("===== Molecule(s) Eau(x) (O) proche d'un N pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                                                        
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                        elif (self.atom_charges[i] == 17) and (self.bond_length(i, j)<= criteria_O_Cl):
#                            print("===== Tentative de discrimination Oxygene - Azote =====")
#                            print(self.atom_charges_2[j],self.atom_charges[i] ,self.bond_length(i, j) ) 
                            print("===== Molecule(s) Eau(x) (O) proche d'un Cl pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")
                                                        
                            for h in range(self.natm_2):
                                
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                    
                                    print(" | ", self.atom_charges_2[j]," | "," | ",self.atom_coords_2[j]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[j]) + " " + str(self.atom_coords_2[j]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
     

                            
#### Discrimination depuis l'Hydrogene de l'eau

                    if  (self.atom_charges_2[j] == 1):
#                        print("=== Tentative de discrimination Oxygene - atom ===")
#                        print("yes",self.atom_charges_2[j], self.bond_length(i, j))
                        if (self.atom_charges[i] == 1) and (self.bond_length(i, j) <= criteria_H_H):
                            print("===== Molecule(s) Eau(x) (H) proche d'un H pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            
                                 
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                            
                            
                        elif (self.atom_charges[i] == 8) and (self.bond_length(i, j)<= criteria_O_H):
                            
                            print("===== Molecule(s) Eau(x) (H) proche d'un O pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
                                              
                        elif (self.atom_charges[i] == 6) and (self.bond_length(i, j)<= criteria_H_C):

                            print("===== Molecule(s) Eau(x) (H) proche d'un N pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
 
     
                            
                        elif (self.atom_charges[i] == 7) and (self.bond_length(i, j)<= criteria_H_N):
                            print("===== Molecule(s) Eau(x) (H) proche d'un N pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
                                            file.write(str(self.atom_charges_2[n]) + " " + str(self.atom_coords_2[n]) + os.linesep)
                                            file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                                            
                                            
                        
                        elif (self.atom_charges[i] == 17) and (self.bond_length(i, j)<= criteria_H_Cl):
                            print("===== Molecule(s) Eau(x) (H) proche d'un Cl pest =====")
                            print ( "d ",self.atom_charges[i],"pest","_", self.atom_charges_2[j],"eau","=" ,self.bond_length(i, j),"A")                            

                        
                            for h in range(self.natm_2):
                                M_H2O = np.linalg.norm(self.atom_coords_2[j] - self.atom_coords_2[h])
                                
                                if (M_H2O <= 1.0) and (M_H2O!= 0.0):
                                                                        
                                    for n in range(self.natm_2):
                                        M_O_H2O = np.linalg.norm(self.atom_coords_2[h] - self.atom_coords_2[n])
                                        
                                        if (M_O_H2O <= 1.0) and (M_O_H2O != 0.0):
                                            print(" | ",self.atom_charges_2[n]," | "," | ",self.atom_coords_2[n]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ",M_O_H2O)
                                            
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
#        self.print_atom()

#uniqlines_1 = set(open('/Users/desdion/Desktop/Coding/Python/Sph_cut/pesticide.txt').readlines())
#uniqlines_pest = open('/Users/desdion/Desktop/Coding/Python/Sph_cut/uniqlines_pest', 'w').writelines(uniqlines_1)

#print(uniqlines_1)    
   ### à surveiller à la fin, ça a l'air de faire ça en premier donc ça va merder 

   #uniqlines_pest.close()


################################################ 

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
                        print ( "d ",self.atom_charges_3[l],"pest","_", self.atom_charges_2[k],"eau","=" ,self.bond_length_2(k, l),"A")
                        for h in range(self.natm_2):
                            
                            M_H2O = np.linalg.norm(self.atom_coords_2[k] - self.atom_coords_2[h])
                            
                            if (M_H2O <= 1.0) and (M_H2O!= 0.0):    
                    
                                    print(" | ", self.atom_charges_2[k]," | "," | ",self.atom_coords_2[k]," | "," | ",self.atom_charges_2[h]," | "," | ",self.atom_coords_2[h]," | ", " | ",M_H2O," | " )
                                    
                                    file.write(str(self.atom_charges_2[k]) + " " + str(self.atom_coords_2[k]) + os.linesep)
                                    file.write(str(self.atom_charges_2[h]) + " " + str(self.atom_coords_2[h]) + os.linesep)
                                    


 
     
                    elif (self.atom_charges_2[k] == 1) and (self.bond_length_2(k, l) <= criteria_Ca_H):
                        
                        print("===== Molecule(s) Eau(x) (H) proche d'un Ca  =====")
                        print ( "d ",self.atom_charges_3[l],"pest","_", self.atom_charges_2[k],"eau","=" ,self.bond_length_2(k, l),"A")                            

                    
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
try_path = 'try.txt'
try_2_path = 'try_2.txt'


###################
    
if __name__ == '__main__':
    mole = Molecule()
#    mole.construct_from_dat_file("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/acetaldehyde.dat")
    mole.construct_from_dat_file("pest.dat")
#    mole.construct_from_dat_file_2("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/2W.dat")
    mole.construct_from_dat_file_2("wat.dat")
    mole.print_solution_01()

if __name__ == '__main__':
    
    cat = Cation()
#    cat.construct_from_dat_file_2("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/2W.dat")
    cat.construct_from_dat_file_2("wat.dat")
#    cat.construct_from_dat_file_3("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/cat.dat")
    cat.construct_from_dat_file_3("cat.dat")
    cat.print_solution_02()

if __name__ == '__main__':
    
    wat_cat = wat_cat()
#    cat.construct_from_dat_file_2("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/2W.dat")
    wat_cat.construct_from_dat_file_wat_cat("try_4")
#    cat.construct_from_dat_file_3("/Users/desdion/Desktop/Coding/Python/Sph_cut/input/cat.dat")
    wat_cat.construct_from_dat_file_wat_cat_2("try_4")


#uniqlines_1 = set(open('/Users/desdion/Desktop/Coding/Python/Sph_cut/pesticide.txt').readlines())
#uniqlines_pest = open('/Users/desdion/Desktop/Coding/Python/Sph_cut/uniqlines_pest', 'w').writelines(uniqlines_1)
#print(uniqlines_1) 

#uniqlines_2 = set(open('/Users/desdion/Desktop/Coding/Python/Sph_cut/cation.txt').readlines())
#uniqlines_pest = open('/Users/desdion/Desktop/Coding/Python/Sph_cut/uniqlines_cat', 'w').writelines(uniqlines_2)
#print(uniqlines_2) 


uniqlines_1 = set(open('pesticide.txt').readlines())
uniqlines_pest = open('uniqlines_pest', 'w').writelines(uniqlines_1)
print(uniqlines_1) 

uniqlines_2 = set(open('cation.txt').readlines())
uniqlines_pest = open('uniqlines_cat', 'w').writelines(uniqlines_2)
print(uniqlines_2)    


######## on enleve les crochets fichier sphere cation

u_cat = open("uniqlines_cat", "rt")
f_cat = open("cat_f", "wt")

for line in u_cat:
    
    f_cat.write(line.replace('[', ' '))
    
u_cat.close()
f_cat.close()

u_cat = open("cat_f", "rt")
ff_cat = open("cat_ff", "wt")

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
ff_pest = open("pest_ff", "wt")

for line in u_pest:
    
    ff_pest.write(line.replace(']', ' '))
    
u_pest.close()
ff_pest.close()
