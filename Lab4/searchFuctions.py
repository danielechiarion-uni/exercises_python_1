# linear search algorithm
def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
            
    return -1
    
    
# function containing binary search method
# using iteration. 
def iterativeBinarySearch(array, element):
    array.sort() # sort the list in order to make the research

    # define the index values to use
    # inside this function
    starting_index = 0
    ending_index = len(array)-1
    
    while starting_index <= ending_index:
        mid_index = (starting_index + ending_index) // 2
        
        if array[mid_index] == element:
            return mid_index
        elif array[mid_index] < element:
            # change the indexes and search 
            # inside the right half
            starting_index = mid_index + 1
        elif array[mid_index] > element:
            # change the indexes and search 
            # inside the left half
            ending_index = mid_index - 1
    
    return -1
    
def binary_search_step(array, starting_index, ending_index, element):
    if starting_index > ending_index:
        return -1
    
    mid_index = (starting_index + ending_index) // 2 # calculate mid index to complete the research
    if array[mid_index] == element:
        return mid_index
    elif array[mid_index] < element:
        # change the indexes and search 
        # inside the right half
        return binary_search_step(array, mid_index+1, ending_index, element)
    elif array[mid_index] > element:
        # change the indexes and search 
        # inside the left half
        return binary_search_step(array, starting_index, mid_index-1, element)

# function containing binary search method
# using recursion
def recursiveBinarySearch(array, element):
    if not array: # check immediately if the array is empty
        return -1

    array.sort() # sort the array before completing any operation
    
    return binary_search_step(array, 0, len(array)-1, element)
    
# ask to input the list and the number to search
number_input = ' '
number_list = [] # create the empty list
print('Inserisci i numeri della lista (INVIO per terminare): ')

while (string_input:=input()) != '':
    number_list.append(int(string_input))
    
print("Lista inserita: " + str(number_list))

search_number = int(input("Inserisci il numero da ricercare: "))

# search the number using all the methods developed in this file
linear_result = linearSearch(number_list, search_number)
iterative_binary_result = iterativeBinarySearch(number_list, search_number)
recursive_binary_result = recursiveBinarySearch(number_list, search_number)

# print the results
print("Risultato ricerca lineare: " + str(linear_result))
print("Risultato ricerca binaria iterativa: ", str(iterative_binary_result))
print("Risultato ricerca binaria ricorsiva: ", str(recursive_binary_result))
