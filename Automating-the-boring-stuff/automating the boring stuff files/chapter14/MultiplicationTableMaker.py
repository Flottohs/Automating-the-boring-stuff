#Create a program multiplicationTable.py that takes a number N from the command line and creates an N×N multiplication table in an Excel spreadsheet. For example, when the program is run like this


import openpyxl

def multtable(N, filename = 'multtableforn'):

    wb = openpyxl.Workbook()  # Creates a new workbook
    sheet = wb.active
    sheet.title = 'N-value-excel-wb'
    
    
    
    sheet = wb['N-value-excel-wb']
    
    sheet['A1'] = 'Hello world!'

    
    for row in range(1,N+1):

        for col in range(1,N+1):
            value = row * col
            sheet.cell(row=row, column=col).value = value
            
    wb.save(filename)
    
    
    
            

            

    

    
    
    

    
    
print("input N")
N = int(input())
multtable(N)

