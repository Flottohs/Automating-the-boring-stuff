#Create a program blankRowInserter.py that takes two integers and a filename string as command line arguments. Let’s call the first integer N and the second integer M. Starting at row N, the program should insert M blank rows into the spreadsheet.





import openpyxl

def blankrowinserter(N,M, filename):
    try:
        wb = openpyxl.load_workbook(filename)  
        print('input sheet name')
        sheetname = input()
        sheet = wb[sheetname]
        sheet.insert_rows(N, M)    
        wb.save(filename)
    except Exception as exc:
        print(f"Error occured {exc} ")
        exit()
      
print("input N, starting position and M, number of blank spaces")
N = int(input())
M = int(input())
print("input filename")
filename = input()
blankrowinserter(N,M,filename)

