#!/usr/bin/env python3

#comboinationsex is a program designed to spark creativity from mashing up two words together
#by Josh Stepp (joshstepp.com)

import random

#random to read the master file
lines = open('masterlist.txt').read().splitlines()

#printing random lines x 2
myline =random.choice(lines)
myline2 =random.choice(lines)

#user input for number of lines
numberOfLines = input("How many matches would you like? ")


#simple while loop to get 10 results
counter = 0

while (counter < numberOfLines):
    myline =random.choice(lines)
    myline2 =random.choice(lines)
    print (myline)+(" ")+(myline2)
    counter = counter + 1
