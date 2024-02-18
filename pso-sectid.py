#!/usr/bin/python

#this code returns the sector id for a phantasy star online ep 1 character
#as calculated by numerical value for digits with modulus of each char, each char added together
#and identified by 0-9. The sect Id determines what drops for your char more often.

import array
import logging

def get_values(string):
    namevalarr = []
    sum = 0
    for char in string:
        utfval=(ord(char))
        logging.info('integer type ' + str(type(utfval)))
        modi = utfval % 10 
        namevalarr += str(modi)
        logging.info('value of utf ' + str((utfval)))
        logging.info('value of modi ' + str(modi))
        
    #print("UTF values" + str(namevalarr))
    for i in namevalarr:
        sum = sum + int(i)
    logging.info('the sum ' + str(sum))
    sum = sum % 10 

    return(sum)
    
def sectionid(int):
    match int:
        case 0: sectid = "Viridia: dark green: shots most often, slicers least often"
        case 1: sectid = "Greenill: light green: rilfes most often, swords least often"
        case 2: sectid = "Skyly: light blue: swords most often, mechguns least often"
        case 3: sectid = "Bluefull: dark blue:  Find partisan most often, wands least often"
        case 4: sectid = "Purplenum: purple: Find mechguns most often, swords and partisans least often"
        case 5: sectid = "Pinkal: pink: Find wands most often, rifles least often"
        case 6: sectid = "Redria: red: mostly balanced, slicers most often, daggers least often"
        case 7: sectid = "Oran: orange: daggers most often, rods least often"
        case 8: sectid = "Yellowboze: yellow: balanced, more mesta dropped"
        case 9: sectid = "Whitill: white: somewhat balanced, slicers most, shots least"
        case _:
            sectid = "Something went horribly wrong"
    return(sectid)

def main ():
    #logging
    #logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.ERROR)
    #get user input for name
    strname = input("Enter Name to determine: ")
    
    #get utf values and put in array for letters
    modmathint=get_values(strname)
    logging.info('returned value ' + str(modmathint))
    #get section id based on the return of the digit
    sectid=sectionid(modmathint)
    print(strname + " is a " + sectid)
    return 0


if __name__ == "__main__":
    main()
