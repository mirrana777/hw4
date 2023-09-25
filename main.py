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

#task 4.1

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

#4.2
text = ("like many great poets, Auroth just wants time to write, but the Winter Wyvern's life is full of interruptions. The epics of the Eldwurms have a long and colorful history,"
        " but some fear that the remaining dragon scholars are not as prolific as they once were, with few lines added to the Eldwurm Eddas since the last age of greatness.")
words = text.split()
for i in range(0,len(words)):
    if words[i-1].endswith(('.',',')):
            words[i] = words[i].capitalize()
result = ' '.join(words)
print(result)
#i just decide to broke sentences into words, than i gone through this words and if it ends with . , then after it starts capital letter
#4.3
text = ("like many great poets,4 Auroth just wants time to write, but the Winter Wyvern's life 3 is full of interruptions. The epics of the Eldwurms have a long and colorful history,"
        " but some fear that 5the remaining dragon scholars8 are not as prolific as 5 they once were, with few lines added to the Eldwurm Eddas since the last age of greatness.")
digits = 0
for numbers in text:
    if numbers.isdigit():
        digits += 1
print("Numbers in text: ",digits)
#there i left some hidden numbers and my code reads them
text = ("like many great poets, Auroth just wants time to write, but the Winter Wyvern's life is full of interruptions. The epics of the Eldwurms have a long and colorful history,"
        " but some fear that the remaining dragon scholars are not as prolific as they once were, with few lines added to the Eldwurm Eddas since the last age of greatness.")
dots = 0
points = 0
for symbol in text:
    if symbol == '.':
        points += 1
    elif symbol == ',':
        dots += 1

print("Points: ", points)
print("Dots: ", dots)

#4.4
text = ("like many great poets, Auroth just wants time to write, but the Winter Wyvern's life is full of interruptions. The epics of the Eldwurms have a long and colorful history!"
        " but some fear that the remaining dragon scholars are not as prolific as they once were, with few lines added !to the Eldwurm Eddas since the last age of greatness.!")
sign = 0
for symbol in text:
    if symbol == '!':
        sign += 1

print("Sign: ", sign)
