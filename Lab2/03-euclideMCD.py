inputA = int(input("Inserisci il primo numero: "))
inputB = int(input("Inserisci il secondo numero (<= al primo): "))

# just keep the initial values 
# till the end of the program
first_number, second_number = inputA, inputB

# to make the formula proper, 
# just swap the numbers
if first_number < second_number:
    first_number, second_number = second_number, first_number

while second_number != 0 and first_number % second_number != 0:
    first_number, second_number = second_number, first_number % second_number
    
print(f"MCD({inputA},{inputB})={second_number}")
