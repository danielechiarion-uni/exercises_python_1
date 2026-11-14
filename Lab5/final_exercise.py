# create function which counts vowels
def conta_vocali(parola):
    counter = 0 # define counter for vowels

    parola = parola.lower() # put it all to lowercase
    for character in parola:
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            counter += 1
    
    return counter
    
# function which selects words with a minimum
# of vowels given in input by the user
def parole_con_vocali(parole, n):
    output = []
    
    for parola in parole:
        if conta_vocali(parola) >= n:
            output.append(parola)
            
    return output
    
FILE_PATH = "parole.txt" # find the file where to read

word_list = []
with open(FILE_PATH, "r") as file:
    print("Lettura file "+FILE_PATH+" in corso...")
    for row in file:
        parola = row.strip()
        print(f"'{parola}' - {conta_vocali(parola)} vocali")
        word_list.append(parola)
        
# ask the minimum of vowels to find
n = 0
while n <= 0:
    n = int(input("Inserisci il numero minimo di vocali: "))
    
word_list = parole_con_vocali(word_list, n)
print(f"Parole con almeno {n} vocali: {word_list}")
    

