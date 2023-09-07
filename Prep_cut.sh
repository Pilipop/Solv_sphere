#!/bin/bash

for name in p6.txt

do


###echo "36" > pest.dat
######echo " " >> try_2
head -n 38 p6.txt | tail -n +3 >> pest.dat
head -n 38 p6.txt | tail -n +3 > pest_n_less.dat

##head -n 38 p6.txt |i
tail -n +39 p6.txt  > try_3

done

exit
