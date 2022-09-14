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

            # Finding average values
            Uavg=Uavg/n
            Vavg=Vavg/n
            Wavg=Wavg/n

            for i in range(0,n):
                x=U[i]-Uavg
                U_.append(x)

                y=V[i]-Vavg
                V_.append(y)
                
                z=W[i]-Wavg
                W_.append(z)

            nr=ceil(n/mod)

            # overall octant frequency (using a dict)
            fo={1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}

            # range wise octant frequency
            f={}

            for i in range (0,nr):
                f[i]={1:0, -1:0, 2:0, -2:0, 3:0, -3:0, 4:0, -4:0}

            for i in range (0,n):
                r=int(i/mod)
                o=get_octant(U_[i], V_[i], W_[i])
                f[r][o]+=1
                fo[o]+=1

            with open('octant_output.csv', 'w', newline='') as fileoutput:

                # The names of field
                fn=['Time', 'U','V', 'W' ,'U Avg','V Avg','W Avg',"U'=U - U avg","V'=V - V avg","W'=W - W avg", "Octant"," ","Octant ID", "+1","-1","+2","-2","+3","-3","+4","-4"]

                writer=csv.writer(fileoutput)

