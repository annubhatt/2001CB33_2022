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
    else:
        return("quadrant=-4")

def octact_identification(mod=5000):
    
    # original values as empty lists
    T, U, V, W=[], [], [], []

    # values to be used in program
    U_, V_, W_=[], [], []

    # sum values
    Uavg, Vavg, Wavg=0, 0, 0