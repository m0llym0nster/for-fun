#!/usr/bin/python
"""
this code returns the sector id for a phantasy star online ep 1 character
as calculated by numerical value for digits with modulus of each char, each char added together
and identified by 0-9. The sect Id determines what drops for your char more often.
"""
import logging

def get_values(string):
    """Get the utf values for string & then calculated sum modulus"""
    namevalarr = []
    namesum = 0
    for char in string:
        utfval= ord(char)
        logging.info('integer type %s ',(type(utfval)))
        modi = utfval % 10
        namevalarr += str(modi)
        logging.info('value of utf %s ',utfval)
        logging.info('value of modi %s ',modi)
    #print("UTF values" + str(namevalarr))
    for i in namevalarr:
        namesum = namesum + int(i)
    logging.info('the sum %s',namesum)
    namesum = namesum % 10
    return namesum

def sectionid(valuenum):
    """use sum modulus to get the section id"""
    match valuenum:
        case 0:
            sectid = "Viridia: dark green: shots most often, slicers least often"
        case 1:
            sectid = "Greenill: light green: rilfes most often, swords least often"
        case 2:
            sectid = "Skyly: light blue: swords most often, mechguns least often"
        case 3:
            sectid = "Bluefull: dark blue:  Find partisan most often, wands least often"
        case 4:
            sectid = "Purplenum: purple: Find mechguns most often, swords & partisans least often"
        case 5:
            sectid = "Pinkal: pink: Find wands most often, rifles least often"
        case 6:
            sectid = "Redria: red: mostly balanced, slicers most often, daggers least often"
        case 7:
            sectid = "Oran: orange: daggers most often, rods least often"
        case 8:
            sectid = "Yellowboze: yellow: balanced, more mesta dropped"
        case 9:
            sectid = "Whitill: white: somewhat balanced, slicers most, shots least"
        case _:
            sectid = "Something went horribly wrong"
    return sectid

def pso_sectid (yourname):
    """start of sectid"""
    #logging
    #logging.basicConfig(level=logging.INFO)
    logging.basicConfig(level=logging.ERROR)
    #get user input for name
    #strname = input("Enter Name to determine: ")
    strname = yourname
    #get utf values and put in array for letters
    modmathint=get_values(strname)
    logging.info('returned value %s ',modmathint)
    #get section id based on the return of the digit
    sectid=sectionid(modmathint)
    #print(strname + " is a " + sectid)
    return sectid

#if __name__ == "__main__"
    #main()
