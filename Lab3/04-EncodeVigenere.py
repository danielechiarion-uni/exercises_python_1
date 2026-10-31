input_string = input("Inserisci una stringa: ")
input_string = input_string.upper() # change to upper for better solving, lower would have been the same

password = ""
while len(password) != len(input_string):
    password = input("Inserisci password: ")
password = password.upper()

new_string = ""
for i in range(len(input_string)):
    if input_string[i] != " ":
        new_string += chr((ord(input_string[i]) + ord(password[i]) - 130)%26 + 65) # calculate the sum then add the ascii character
    else:
        new_string += " "
print(new_string)
