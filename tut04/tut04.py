import openpyxl
from datetime import datetime

workbook = openpyxl.load_workbook(filename='output_octant_longest_subsequence_with_range.xlsx')
sheet = workbook.active
    # The title values are modified accordingly
sheet['M1'], sheet['P1'], sheet['Q1'], sheet['R1'], sheet['S1'] = 'Octant', '', 'Octant', 'Longest Subsequence Length', 'Count'
    # We save the workbook
workbook.save(filename='output_octant_longest_subsequence_with_range.xlsx')
def octant_longest_subsequence_count_with_range():
    try:
        from platform import python_version
        import pandas as pd
        from openpyxl import load_workbook
        ver = python_version()

        if ver == "3.8.10":
            print("Correct Version Installed")
        else:
            print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

        # We open the input excel file and read it to a pandas dataframe
        inputTable = pd.read_excel('input_octant_longest_subsequence_with_range.xlsx')

        # The mean values of U, V and W are calculated using pandas' inbuilt mean() method
        inputTable.at[0, 'U Avg'] = inputTable['U'].mean()
        inputTable.at[0, 'V Avg'] = inputTable['V'].mean()
        inputTable.at[0, 'W Avg'] = inputTable['W'].mean()

        # The values of U', V' and W' are calculated by ibtaining the difference of the corresponding column and it's average value
        inputTable["U'=U - U avg"] = inputTable['U'] - inputTable['U Avg'][0]
        inputTable["V'=V - V avg"] = inputTable['V'] - inputTable['V Avg'][0]
        inputTable["W'=W - W avg"] = inputTable['W'] - inputTable['W Avg'][0]

        # The octants are identified for each combination of U', V' and W' by looping through the datframe and using a simple if-else block
        for i in range(len(inputTable)):
            if(inputTable["U'=U - U avg"][i] > 0 and inputTable["V'=V - V avg"][i] > 0):
                inputTable.at[i, 'Octant'] = int(1)
            if(inputTable["U'=U - U avg"][i] < 0 and inputTable["V'=V - V avg"][i] > 0):
                inputTable.at[i, 'Octant'] = int(2)
            if(inputTable["U'=U - U avg"][i] < 0 and inputTable["V'=V - V avg"][i] < 0):
                inputTable.at[i, 'Octant'] = int(3)
            if(inputTable["U'=U - U avg"][i] > 0 and inputTable["V'=V - V avg"][i] < 0):
                inputTable.at[i, 'Octant'] = int(4)
            if(inputTable["W'=W - W avg"][i] < 0):
                inputTable.at[i, 'Octant'] = inputTable['Octant'][i] * -1

    except ImportError:
        print("The module 'Pandas' could not be imported, please make sure it is installed.")
    except FileNotFoundError:
        print("The file could not be found in the parent directory. Please make sure it exists.")
    except PermissionError:
        print("It seems you do not have the nescessary permissions to read/write in the parent directory. Please grant the nescessary permissions or change the working directory.")

# This shall be the last lines of the code.
start_time = datetime.now()

octant_longest_subsequence_count_with_range

end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))