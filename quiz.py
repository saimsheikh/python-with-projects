# This program takes string input and then prints out a mixed order version of the string
# Program Parts
# ● program flow gathers the word list, modifies the case and order, and prints
# ○ get string input, input like a poem, verse or saying
# ○ split the string into a list of individual words
# ○ determine the length of the list
# ○ Loop the length of the list by index number and for each list index:
# ■ if a word is short (3 letters or less) make the word in the list lowercase
# ■ if a word is long (7 letters or more) make the word in the list uppercase
# ○ call the word_mixer function with the modified list
# ○ print the return value from the word_mixer function



qoute=input("Enter a qoute: ")
qoute=qoute.split()
for i in range(len(qoute)):
    if len(qoute[i])<=3:
        qoute[i]=qoute[i].lower()
    elif len(qoute[i])>=7:
        qoute[i]=qoute[i].upper()

def word_mixer(qoute):
    qoute=qoute[::-1]
    return qoute

print(word_mixer(qoute))
