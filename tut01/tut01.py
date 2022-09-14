import csv
from math import ceil, floor

def get_octant(x, y, z):
    if(x>=0 and y>=0 and z>=0):
        return("octant=1")
    elif(x>=0 and y>=0 and z<0):
        return("octant=-1")
    elif(x<0 and y>=0 and z>=0):
        return("octant=2")
    elif(x<0 and y>=0 and z<0):
        return("octant=-2")
    elif(x<0 and y<0 and z>=0):
        return("octant=3")
    elif(x<0 and y<0 and z<0):
        return("octant=-3")
    elif(x>=0 and y<0 and z>=0):
        return("octant=4")
    else:
        return("octant=-4")

def octact_identification(mod=5000):
    
    # original values as empty lists
    T, U, V, W=[], [], [], []

    # values to be used in program
    U_, V_, W_=[], [], []

    # sum values
    Uavg, Vavg, Wavg=0, 0, 0

    # count of values
    n=0  

    try:
        with open('octant_input.csv', 'r') as fileinput:
            csvreader=csv.reader(fileinput)

            # skipping the heading row
            next(csvreader)

            for line in csvreader:
                Uavg= Uavg +float(line[1])
                U.append(float(line[1]))

                Vavg= Vavg +float(line[2])
                V.append(float(line[2]))

                Wavg= Wavg +float(line[3])
                W.append(float(line[3]))

                T.append(line[0])
                n=n+1

