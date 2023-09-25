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
# task2
string = input ("Enter a string: ")
searching = input ("Enter symbol for searching: ")
variable = 0
for answer in string:
    if answer == searching:
        variable += 1
print (f"Symbol '{searching}' used {variable} times in string")
