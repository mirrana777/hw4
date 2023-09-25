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
# task3
string = input ("Enter the string: ")
change = input ("Eneter a word to change: ")
changed = input ("Enter a word for raplecment: ")
resault = string.replace(change, changed)
print ("resault string:" + resault)

#task 4
#1
string = "Let the sky tear down the unworthy"
print(string[2])
#2
string = "Let the sky tear down the unworthy"
print(string[-2])
#3
string = "Let the sky tear down the unworthy"
print(string[:5])
#4
string = "Let the sky tear down the unworthy"
print(string[:-2])
#5
string = "Let the sky tear down the unworthy"
print(string[:2])
#6
string = "Let the sky tear down the unworthy"
print(string[1::2 ])
#7
string = "Let the sky tear down the unworthy"
print(string[::-1])
#8
string = "Let the sky tear down the unworthy"
print(string[-1::-2])
#9
string = "Let the sky tear down the unworthy"
print(len(string))
