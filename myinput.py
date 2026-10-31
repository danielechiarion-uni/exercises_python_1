# function to check if the number is 
# an integer
def isDecimalInteger(s):
    number = s.strip() # remove strarting and final spaces, to see if it is allowed
    
    # then control if it has + or - operator
    # at the start, otherwise it is an error
    if number.find('+') > 0 or number.find('-') > 0:
        return False
        
    # then check if all the other characters are
    # just numbers, without spaces or everything else
    for character in number[1:]:
        if character <= '0' or character >= '9':
            return False
    return True
    
def isFloating(s):
    number = s.strip() # remove strarting and final spaces, to see if it is allowed
    
    # then control if it has + or - operator
    # at the start, otherwise it is an error
    if number.find('+') > 0 or number.find('-') > 0:
        return False
        
    # then check if all the other characters are
    # just numbers, without spaces or everything else
    for character in number:
        if character <= '0' or character >= '9':
            return False
    return True
    

