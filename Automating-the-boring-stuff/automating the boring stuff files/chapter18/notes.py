# -*- coding: utf-8 -*-
"""
Data Serialization Formats: CSV, JSON, XML
Study Notes - Fully commented for Python / VS Code
"""

# ----------------------------
# CSV FILES
# ----------------------------

# CSV = Comma Separated Values
# Each line = a row, commas separate cells
# Limitations vs Excel:
# - No multiple data types; all values stored as strings
# - No font formatting, colors
# - No multiple worksheets
# - Cannot merge cells
# - Cannot specify column width/row height
# - Cannot embed images or charts

import csv

# Reading CSV files
example_file = open('example3.csv', encoding='utf-8')
example_reader = csv.reader(example_file)

# Convert reader to list for easier access
example_data = list(example_reader)
print("CSV Data as List of Lists:", example_data)

example_file.close()

# Accessing individual cells
print("First row, first column:", example_data[0][0])
print("First row, second column:", example_data[0][1])

# Looping through rows
for row in example_data:
    print("Row:", row)

# Writing CSV files
output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)

# Write rows
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])
output_file.close()

# Tab-separated values (TSV)
output_file = open('output.tsv', 'w', newline='')
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n')
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_file.close()

# Working with headers (DictReader / DictWriter)
example_file = open('exampleWithHeader3.csv')
dict_reader = csv.DictReader(example_file)

for row in dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

# Writing CSV with DictWriter
output_file = open('output_dict.csv', 'w', newline='')
dict_writer = csv.DictWriter(output_file, fieldnames=['Name', 'Pet', 'Phone'])
dict_writer.writeheader()
dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_file.close()

# ----------------------------
# JSON FILES
# ----------------------------

import json

json_string = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Science"]}'

# JSON string → Python data structure
python_data = json.loads(json_string)
print("JSON to Python:", python_data)

# Python data structure → JSON string
json_string2 = json.dumps(python_data)
print("Python to JSON:", json_string2)

# Pretty-print JSON
json_string_pretty = json.dumps(python_data, indent=2)
print("Pretty JSON:\n", json_string_pretty)

# ----------------------------
# XML FILES
# ----------------------------

import xml.etree.ElementTree as ET
import xmltodict

# Example XML string
xml_string = """
<person>
  <name>Alice Doe</name>
  <age>30</age>
  <programmer>true</programmer>
  <car xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>
  <address>
    <street>100 Larkin St.</street>
    <city>San Francisco</city>
    <zip>94102</zip>
  </address>
  <phone>
    <phoneEntry>
      <type>mobile</type>
      <number>415-555-7890</number>
    </phoneEntry>
    <phoneEntry>
      <type>work</type>
      <number>415-555-1234</number>
    </phoneEntry>
  </phone>
</person>
"""

# Parsing XML
root = ET.fromstring(xml_string)
print("Root tag:", root.tag)

# Iterating through elements
for elem in root.iter():
    print(elem.tag, "--", elem.text)

# Extracting specific elements
for elem in root.iter('number'):
    print("Number element:", elem.text)

# XML → Python dictionary using xmltodict
python_data_from_xml = xmltodict.parse(xml_string)
print("XML to Python dict:", python_data_from_xml)

# Writing XML with ElementTree
person = ET.Element('person')
name = ET.SubElement(person, 'name')
name.text = 'Alice Doe'
age = ET.SubElement(person, 'age')
age.text = '30'
programmer = ET.SubElement(person, 'programmer')
programmer.text = 'true'
car = ET.SubElement(person, 'car')
car.set('xsi:nil', 'true')
car.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')

xml_string_out = ET.tostring(person, encoding='utf-8').decode('utf-8')
print("Constructed XML:\n", xml_string_out)

# ----------------------------
# PRACTICE QUESTIONS
# ----------------------------

# 1. Features Excel has but CSV doesn’t: Font size, color, multiple worksheets, merged cells, cell widths/height, embedded images/charts
# 2. Arguments for csv.reader() and csv.writer(): File objects opened in 'r' or 'w' mode
# 3. Modes for CSV file objects: Reader = 'r', Writer = 'w'
# 4. Method to write a list row: writerow()
# 5. delimiter vs lineterminator: delimiter separates cells, lineterminator separates rows
# 6. Formats editable with text editor: CSV, JSON, XML
# 7. JSON string → Python: json.loads()
# 8. Python → JSON string: json.dumps()
# 9. Serialization format like HTML: XML
# 10. JSON None value: null
# 11. JSON Boolean: true / false