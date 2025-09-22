
"""isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers (alphanumerics) and isn’t blank

isdecimal() Returns True if the string consists only of numeric characters and isn’t blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and isn’t blank

istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters"""

#start or end of string

'Hello, world!'.startswith('Hello')

'Hello, world!'.endswith('Hello')



#join
', '.join(['cats', 'rats', 'bats'])
#split
'My name is Simon'.split()

#justifying text
'Hello'.rjust(10)
'Hello'.ljust(10)
'Hello'.rjust(20, '*')#fills gaps to left with *

#removing whitespace

spam = 'lalalala.   mamama'
spam.strip()

#converting to unicode

ord('A')
#converting back
chr(ord('A'))
chr(ord('A')+1)


#copy and pasting
import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()
