'''Say you have a spreadsheet of data from the 2010 US Census and you’ve been given the boring task of going through its thousands of rows to count both the population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract. We’ll name the spreadsheet file censuspopdata.xlsx, and you can download it from this book’s online resources. Its contents look like Figure 14-2.

'''



import openpyxl,pprint

print('opening workbook...')


wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['population by census tract']


county_data = {}


print(' reading rows...')



for row in range(2,sheet.max_row+1):
    state = sheet['B' + str(row)].value
    county= sheet['C' + str(row)].value
    pop   = sheet['D' + str(row)].value
    
    
    county_data.setdefault(state,{})
    county_data[state].setdefault(county,{'tracts':0,'pop':0})
    
    county_data[state][county]['tracts']+=1
    
    county_data[state][county]['pop']+=int(pop)
    
    
    print('writing results...')
result_file = open('census2010.py','w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()
print('done')

