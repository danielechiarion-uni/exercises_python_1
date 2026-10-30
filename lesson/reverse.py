# function to reverse the string
def reverse(string):
    if len(string) == 1 or len(string) == 0:
        return string
    elif len(string) == 2:
        return string[1] + string[0]
    else:
        return string[-1] + reverse(string[1:len(string)-1]) + string[0]

string = input("Inserisci una stringa: ")
print("Stringa vuota: ", reverse(string))