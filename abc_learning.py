# Python3 accepts input 
# I wrote this to help my child learn the A B C's and a bit about Python3

abc_dict = {
    'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'dog', 'e': 'elephant',
    'f': 'fox', 'g': 'gorilla', 'h': 'horse', 'i': 'igloo',
    'j': 'jellyfish', 'k': 'kangaroo', 'l': 'lamb', 'm': 'moon', 
    'n': 'net', 'o': 'ostrich', 'p': 'penguin', 'q': 'queen',
    'r': 'raccoon', 's': 'summer', 't': 'turkey', 'u': 'umbrella', 
    'v': 'violin', 'w': 'winter', 'x': 'xylophone', 'y': 'yarn', 'z': 'zebra',
    } 

# accepts letter in any case
# rejects non-alphabetic characters with friendly message
prompt = "\nPlease pick a letter:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    abc = input(prompt).lower()
    
    if abc == 'quit':
        break
    if not abc.isalpha():
        print("\n***That is not a letter*** Please choose a letter.")
        continue
    else:
        if abc in abc_dict:
            print("\n" + abc.capitalize() + " is for " + 
            abc_dict[abc].capitalize() + "!")
