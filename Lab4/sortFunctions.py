# sort function using selection method
def selectionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array))
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    

# ask to input the list and the number to search
number_input = ' '
number_list = [] # create the empty list
print('Inserisci i numeri della lista (INVIO per terminare): ')

while (string_input:=input()) != '':
    number_list.append(int(string_input))
    
print("Lista inserita: " + str(number_list))
