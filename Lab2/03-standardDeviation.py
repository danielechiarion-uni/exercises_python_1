# define variables
inputData = ""
sum = 0
sum_pow2 = 0
num_counter = 0

while True:
    inputData = input("Inserisci un numero intero (o STOP per terminare): ")
    # if it's not an input data, just continue
    if inputData == "STOP":
        break;
        
    intValue = int(inputData)
    sum += intValue
    sum_pow2 += intValue ** 2
    num_counter += 1

# if less than two number have been typed in
# return an error
if num_counter < 2:
    print("ERRORE! Deviazione standard non calcolabile con meno di due numeri")
else:
    deviation = ((sum_pow2 - sum*sum/num_counter)/(num_counter-1))**(1/2)
    print("La deviazione standard calcolata e' "+str(deviation))
