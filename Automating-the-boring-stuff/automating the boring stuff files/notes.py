import re

# Phone number example
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
print(match_obj.group())   # '415-555-4242'


# the point of the backslashed characters is that it means that they will be interpreted,
# without this they will be ignored
pattern = re.compile(r'Cat(?:erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(match.group())   # 'Catch'

# the | means pipe, basically gives options and can interpret any of them
# If any of the strings in pipe are present in x message,
# it will return the string before and whichever pipe was in x message
# NOTE: used (?:...) non-capturing group so .findall() returns whole matches
match = pattern.findall('Cat, catastrophe, catch, category')
print(match)   # ['Cat', 'catastrophe', 'catch', 'category']


# In addition to a search() method, Pattern objects have a findall() method.
# While search() will return a Match object of the first matched text in the searched string,
# the findall() method will return the strings of every match in the searched string.


# shorthand character classes
"""
\d  -> Any numeric digit from 0 to 9.
\D  -> Any character that is not a numeric digit from 0 to 9.
\w  -> Any letter, numeric digit, or the underscore character. (Think “word” characters.)
\W  -> Any character that is not a letter, numeric digit, or underscore.
\s  -> Any space, tab, or newline character. (Think “space” characters.)
\S  -> Any character that is not a space, tab, or newline character.
"""

# Example: one or more digits, followed by space, followed by word characters
pattern = re.compile(r'\d+\s\w+')
print(pattern.findall('12 drummers, 11 pipers, 10 lords'))  
# ['12 drummers', '11 pipers', '10 lords']


# the dot . matches any character except for new line
at_re = re.compile(r'.at')
print(at_re.findall('The cat in the hat sat on the flat mat.'))
# ['cat', 'hat', 'sat', 'lat', 'mat']


'''
The [A-Z] or [a-z] character class matches uppercase or lowercase letters, respectively, but not both.
You need to use [A-Za-z] to match both cases.
The [A-Za-z] character class matches only plain, unaccented letters. 
The \w character class matches all letters (including accented letters and characters from other alphabets).
But it also matches numbers and the underscore character.
Straight and smart quotes (' " ‘ ’ “ ”) are considered completely different from each other and must be specified separately.
Reference: https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/.
'''


# the ? flag means the expression before it is optional
pattern = re.compile(r'42!?')
print(pattern.search('42!').group())   # '42!'


# this can be used in the phone number thing as
pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match1 = pattern.search('My number is 415-555-4242')
print(match1.group())   # '415-555-4242'


# another qualifier is * meaning match zero or more
pattern = re.compile('Eggs(and spam)*')
print(pattern.search('Eggs').group())          # 'Eggs'
print(pattern.search('Eggs and spam').group()) # 'Eggs and spam'


# match one or more qualifier is +, qualifier must appear at least once

# you can match a specific number of qualifiers by doing something like (ha){3} which would mean HaHaHa
haRegex = re.compile(r'(Ha){3}')
match1 = haRegex.search('HaHaHa')
print(match1.group())   # 'HaHaHa'

match = haRegex.search('HaHa')
print(match == None)    # True


# greedy matches (default) → match as many as possible
greedy_pattern = re.compile(r'(Ha){3,5}')
match1 = greedy_pattern.search('HaHaHaHaHa')
print(match1.group())   # 'HaHaHaHaHa'

# lazy matches → stop at minimum match
lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())   # 'HaHaHa'


# matching everything
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
print(name_match.group(1))  # 'Al'
print(name_match.group(2))  # 'Sweigart'


# Matching newline characters
no_newline_re = re.compile('.*')
print(no_newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# 'Serve the public trust.'

newline_re = re.compile('.*', re.DOTALL)
print(newline_re.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# 'Serve the public trust.\nProtect the innocent.\nUphold the law.'


# Matching at the start and end of a string
'''
^spam  → must begin with "spam"
spam$  → must end with "spam"
^$     → entire string must match
'''


# case insensitive matching
pattern = re.compile(r'robocop', re.I)
print(pattern.search('RoboCop is part man, part machine, all cop.').group())
# 'RoboCop'


# Regex can also substitute in new text
agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.'))
# 'CENSORED contacted CENSORED.'


# managing complex regexes with verbose mode
# it ignores whitespace and comments in the regex function
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?       # Area code
    (\s|-|\.)?               # Separator
    \d{3}                    # First three digits
    (\s|-|\.)                # Separator
    \d{4}                    # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)


# combining ignorecase, dotall and verbose
some_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)