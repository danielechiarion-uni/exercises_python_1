# input the numbers value
number = 0
while number < 2:
    number = int(input("Indica su quanti numeri vuoi verificare il crivello di Eratostene: "))
    
number_flags = [True] * (number+1)
# go from 2 to the half of the number
for i in range (2, number // 2 + 1):
    current_number = i
    # if the number is not a prime one
    # all his multiples will have already been found
    if not number_flags[current_number]:
        continue
    
    # add the number till it goes over 
    # the number given
    current_number += i
    while current_number <= number:
        number_flags[current_number] = False
        current_number += i
        
# cycle all the list and find prime numbers
print("I numeri primi sono: ")
for i in range(2, number):
    if number_flags[i]:
        print(i)
