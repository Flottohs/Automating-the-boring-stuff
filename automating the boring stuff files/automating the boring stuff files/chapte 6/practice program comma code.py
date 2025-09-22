'Say you have a list value like this:'

spam = ['apples', 'bananas', 'tofu', 'cats']
'Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return' 'apples, bananas, tofu, and cats' 'But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.'

def commacode(spam):
    output = ''
    lengthspam = len(spam)
    if lengthspam == 0:
        return 'invalid list'
    if lengthspam == 1:
        return str(spam[0])
    else:

        for i in range(lengthspam - 1):
            output += str(spam[i]) + ','+' '
        output += 'and' +' ' + str(spam[-1])
        print (output)
#tested - works

commacode(spam)