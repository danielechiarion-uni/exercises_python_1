# function to check if the DNA string
# contains only the letters available (A, C, G, T)
def check_dna_string(dna_string):
    # just convert the string to upper
    # and verify that the count of the letters 
    # is the length of the string, otherwise other letters
    # have been typed
    dna_string = dna_string.upper()
    return dna_string.count('A') + dna_string.count('C') + dna_string.count('G') + dna_string.count('T') == len(dna_string)
    
def change_dna_string(dna_string):
    for character in dna_string:
        if character == 'A':
            character = 'T'
        elif character == 'T':
            character = 'A'
        elif character == 'C':
            character = 'G'
        elif character == 'G': # put the elif even in the end in case the dna string check doesn´t work
            character = 'C' 
    return dna_string

# take a string in input and 
# control if it contains only letters A,C,G,T
starting_point = True
input_string = ''
while starting_point or not check_dna_string(input_string):
    starting_point = False
    input_string = input('Inserisci una sequenza di DNA (A, C, G, T): ')
    input_string = input_string.strip().upper()
    
# change the letters without using replace
# because there could be some errors
dna_string = change_dna_string(input_string)
dna_string = dna_string[::-1] # reverse the string
print(dna_string) # print the string 
