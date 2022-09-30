
# here we define mod value
mod=5000

# importing openpyxl and nan and loading workbook
try:
    from cmath import nan
    import openpyxl

    wb = openpyxl.load_workbook(r'C:\Users\DELL\OneDrive\Desktop\temp_octant\input_octant_transition_identify - Copy.xlsx')
except:
    print("there is error in loading workbook check your file directory and import openpyxl")
    exit()


    # calculation average value
try:
    sheet = wb.active
    Uavg=0
    Vavg=0
    Wavg=0
    lst=[]
    for row in sheet.iter_rows(row_minm=1, col_minm=1,row_maxm=29746, col_maxm=4):
        lst1=[]
        for cell in row:
            lst1.append(cell.value)
        lst.append(lst1)
    for i in range(1,29746):
        Uavg=Uavg+lst[i][1]
        Vavg=Vavg+lst[i][2]
        Wavg=Wavg+lst[i][3]
    Uavg=(Uavg/29745)
    Vavg=(Vavg/29745)
    Wavg=(Wavg/29745)

    lst_avg=[["Uavg","Vavg","Wavg"],[Uavg,Vavg,Wavg]]
except:
    print("there is error in calculating average value")
    exit()

#  nan in tansition value is written

try:
    i=0
    for row in sheet.iter_rows(row_minm=1, col_minm=12,row_maxm=29777, col_maxm=21):
        j=0
        for cell in row:
            cell.value=nan
            j=j+1
        i=i+1
except:
    print("there is some error in transition count")
#create octant of provided value