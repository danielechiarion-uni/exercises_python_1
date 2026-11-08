# sort function using selection method
def selectionSort(array):
    for i in range(len(array)-1):
        min_pos = i
        for j in range(i+1, len(array)):
            if array[j] < array[i]:
                min_pos = j
                
        array[i], array[min_pos] = array[min_pos], array[i]

# sort function using insertion method
def insertionSort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        
        j = i # define index
        while j > 0 and current_value < array[i-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = current_value
        
# function to merge two arrays 
# in one bigger array
def merge(array, left, right):
    # define index for left and
    # right part
    index_left = 0
    index_right = 0
    index_array = 0
    
    # compare the two parts
    # between them and populate the original array
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            array[index_array] = left[index_left]
            index_left += 1
        else:
            array[index_array] = right[index_right]
            index_right += 1
        index_array += 1 # update the index of the array anyway
    
    # copy the last elements of the list
    while index_left < len(left):
        array[index_array] = left[index_left]
        index_left += 1
        index_array += 1
    while index_right < len(right):
        array[index_array] = right[index_right]
        index_right += 1
        index_array += 1

# sort function using merge method
def mergeSort(array):
    # if the array has just one element
    # return it
    if(len(array) <= 1):
        return array
        
    # otherwise separate the array
    # in two equal parts and then merge them
    mid_index = len(array) // 2
    left = array[:mid_index]
    right = array[mid_index:]
    
    mergeSort(left)
    mergeSort(right)
    merge(array, left, right) # merge the two parts 

# ask to input the list and the number to search
number_input = ' '
number_list = [] # create the empty list
print('Inserisci i numeri della lista (INVIO per terminare): ')

while (string_input:=input()) != '':
    number_list.append(int(string_input))
    
print("Lista inserita: " + str(number_list))

choice = -1
while not (1 <= choice <=3):
    choice = int(input("Scegli l'algoritmo da implementare:\n1) Selection Sort\n2) Insertion Sort\n3) Merge sort\n"))
    
match choice:
    case 1:
        selectionSort(number_list)
    case 2:
        insertionSort(number_list)
    case _:
        mergeSort(number_list)

print("Lista ordinata: " + str(number_list))
