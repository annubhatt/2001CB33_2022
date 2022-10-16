import openpyxl
from datetime import datetime

workbook = openpyxl.load_workbook(filename='output_octant_longest_subsequence_with_range.xlsx')
sheet = workbook.active
    # The title values are modified accordingly
sheet['M1'], sheet['P1'], sheet['Q1'], sheet['R1'], sheet['S1'] = 'Octant', '', 'Octant', 'Longest Subsequence Length', 'Count'
    # We save the workbook
workbook.save(filename='output_octant_longest_subsequence_with_range.xlsx')