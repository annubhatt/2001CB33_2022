import csv
from math import ceil, floor

def get_octant(x, y, z):
    if(x>=0 and y>=0 and z>=0):
        return("quadrant=1")
    elif(x>=0 and y>=0 and z<0):
        return("quadrant=-1")
    elif(x<0 and y>=0 and z>=0):
        return("quadrant=2")
    elif(x<0 and y>=0 and z<0):
        return("quadrant=-2")
    elif(x<0 and y<0 and z>=0):
        return("quadrant=3")
    elif(x<0 and y<0 and z<0):
        return("quadrant=-3")
    elif(x>=0 and y<0 and z>=0):
        return("quadrant=4")