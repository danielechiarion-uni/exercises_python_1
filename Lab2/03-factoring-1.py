def next_prime_number(last_prime_number):
    current_number = last_prime_number+1 # define last prime number
    while True:
        result = True # true means there is a prime number, false otherwise
        if current_number >= 3:
            for i in range(int(current_number ** 0.5) + 1):
                # if we have a prime number break the cycle
                if i == 0:
                    break
                elif current_number % i == 0:
                    result = False
                    break
        
        # if the prime number has found return it, 
        # otherwise continue the cycle
        if result:
            return current_number
        else:
            current_number += 1
            
inputData = 0
while inputData <= 1:
    inputData = int(input("Inserisci i valori in input: "))
    
# then process and found all prime numbers
# starting from the lowest one
prime_number = 2
while inputData > 1:
    while inputData % prime_number == 0:
        print(str(prime_number)+",")
        inputData = int(inputData / prime_number)
    # when a prime number has finished to divide,
    # call the next one
    prime_number = next_prime_number(prime_number)
