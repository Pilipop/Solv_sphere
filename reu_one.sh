#!/bin/bash

for name in p6.txt

do

tail -n +2 cat.dat > cat_temp.dat
cat cat_sphere.xyz cat_temp.dat >> cat_wat.xyz


cat pest_sphere.xyz pest_n_less.dat >> pest_wat.xyz


done

exit
