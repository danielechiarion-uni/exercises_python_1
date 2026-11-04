def minimum_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    return min(numbers[0], minimum_number(numbers[1:]))
    
numbers = [] # create the list
# take the numbers in input
input_number = " "
while input_number != '':
    input_number = input("Inserisci un numero (INVIO per terminare): ")
    if input_number != '':
        try:
            numbers.append(int(input_number))
        except:
            pass 
            
if numbers:
    minimum = minimum_number(numbers)
print("Il numero minimo e' "+str(minimum))

