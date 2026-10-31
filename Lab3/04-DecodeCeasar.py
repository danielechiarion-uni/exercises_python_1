input_string = input("Inserisci una stringa: ")
input_string = input_string.upper() # change to upper for better solving, lower would have been the same

number = int(input("Inserisci il numero: "))
number = number % 26 # having 26 or more is just making one more cycle, so take the module

new_string = ""
for character in input_string:
    if character != " ":
        new_string += chr((ord(character) + number - 65)%26 + 65) # to avoid the addition goes over than the number of character requested
    else:
        new_string += " "
print(new_string)
