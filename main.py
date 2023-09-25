# task1
string = input ("string: ")
digits = 0
letters = 0
for symbol in string:
    if symbol.isdigit ():
        digits += 1
    elif symbol.isalpha ():
        letters += 1
print ("Digits: ", digits)
print ("Letters: ", letters)
