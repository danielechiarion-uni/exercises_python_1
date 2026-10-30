input_string = input("Inserisci una stringa: ")

# method to strip duplicates, so removing
# consecutive double characters
counter = 0 # use the actual counter without doubles
new_string = ""
for i in range(len(input_string)):
    if i == 0 or input_string[i] != input_string[i-1]:
        new_string += input_string[i]

print(new_string)

