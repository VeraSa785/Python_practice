greetings = ['hello', 'hi', 'hey', 'hola']

# with list comprehensions - create new list with 2nd letter
letter_list = [ letter[1] for letter in greetings]
print (letter_list)

# create new list with 2nd letter
letter_list = []
for letter in greetings:
    letter_list.append(letter[1])
print (letter_list)
