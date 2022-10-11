from math import ceil
#importing openpyxl, workbook and datetime
import openpyxl
from openpyxl import Workbook
from datetime import datetime

starttime = datetime.now()

def get_octant(x, y, z):
    if(x>=0 and y>=0 and z>=0):
        return(1)
    elif(x<0 and y>=0 and z>=0):
        return(2)
    elif(x<0 and y<0 and z>=0):
        return(3)
    elif(x>=0 and y<0 and z>=0):
        return(4)
    elif(x>=0 and y>=0 and z<0):
        return(-1)
    elif(x<0 and y>=0 and z<0):
        return(-2)
    elif(x<0 and y<0 and z<0):
        return(-3)
    else:
        return(-4)
