#!/bin/bash

# Assign the filename
filename="bonds.lammpsdumpbonds"
suffix=".bkp"
backup="$filename$suffix"
cp $filename $backup

c1was='c_1\[1\]'
c1is='atom1'
c2was='c_1\[2\]'
c2is='atom1'
c3was='c_1\[3\]'
c3is='btype'


search=$c1was
replace=$c1is
sed -i "s/$search/$replace/" $filename
search=$c2was
replace=$c2is
sed -i "s/$search/$replace/" $filename
search=$c3was
replace=$c3is
sed -i "s/$search/$replace/" $filename
