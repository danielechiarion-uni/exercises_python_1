# function to calculate if a character is a number
def isNumber(character):
    return character >= '0' and character <= '9'

# function to check if the number is 
# an integer
def isDecimalInteger(s):
    number = s.strip() # remove starting and final spaces, to see if it is allowed
    
    # then control if it has + or - operator
    # at the start, otherwise it is an error
    if number.find('+') > 0 or number.find('-') > 0:
        return False
        
    # then check if all the other characters are
    # just numbers, without spaces or everything else
    for character in number:
        if not (isNumber(character) or character == '+' or character == '-'):
            return False
    return True
    
def isFloating(s):
    number = s.strip() # remove starting and final spaces, to see if it is allowed
    
    # control if there are max 2 operators,
    # otherwise the float number is not valid
    if number.count('+') + number.count('-') > 2:
        return False
    
    # then control if it has + or - operator
    # at the start, otherwise it is an error
    # in a floating number control even if there is
    # an operator after the e and a number
    e_finder = number.find('e')
    if number.count('e') > 1 or (e_finder != -1 and len(number) >= e_finder+2 and ((number[e_finder+1] != '+' and number[e_finder+1] != '-') or not isNumber(number[e_finder+2]))):
        return False
    if (number.find('+') != e_finder+1 and number.find('+') > 0) or (number.find('-') != e_finder+1 and number.find('-') > 0):
        return False  
    
    # then find if there is just one point and,
    # control if after the point there is at least a number
    if number.count('.') > 1:
        return False
    point_finder = number.find('.')
    if point_finder > 0 and len(number) > point_finder+1 and not isNumber(number[point_finder+1]):
        return False
        
    # then check if all the other characters are
    # just numbers or the characters controlled before
    for character in number:
        if not (isNumber(character) or character == '+' or character == '-' or character == 'e' or character == '.'):
            return False
    return True
    
# function to control if the string provided
# in the input matches the yes, no question
def inputYesNo(message, yes, no):
    # convert all the message to lower case
    # and strip possible spaces
    input_user = input(message).lower()    

    yes = yes.lower().strip()
    no = no.lower().strip()
    
    if input_user == yes:
        print('AFFIRMATIVE')
        return True
    print('NEGATIVE')
    return False
    
# function to see if the string starts with the input provided.
# if the string is empty, return the original string
def inputStringStartingWith(message, startingString):
    print(message)
    
    input_string = message
    # then check the string starting with
    # the input typed
    while input_string != '':
        input_string = input("Inserisci una stringa: ")
        if startingString == '' or (input_string != '' and input_string.startswith(startingString)):
            print(input_string+" OK")
            return input_string
    
    print("String not found")
    return '' # otherwise return an empty string
    
# function to see if the string ends with the input provided.
# if the string is empty, return the original string
def inputStringEndingWith(message, endingString):
    print(message)
    
    input_string = ' '
    # then check the string starting with
    # the input typed
    while input_string != '':
        input_string = input("Inserisci una stringa: ")
        if endingString == '' or (input_string != '' and input_string.endswith(endingString)):
            print(input_string+" OK")
            return input_string
    
    print("String not found")
    return '' # otherwise return an empty string
    
# function to see if the string contains input provided.
# if the string is empty, return the original string
def inputStringContaining(message, substring):
    print(message)
    
    input_string = ' '
    # then check the string starting with
    # the input typed
    while input_string != '':
        input_string = input("Inserisci una stringa: ")
        if substring == '' or (input_string != '' and substring in input_string):
            print(input_string+" OK")
            return input_string
    
    print("String not found")
    return '' # otherwise return an empty string
# *** INPUT FUNCTIONS ***
# functions trying to return numbers typed by the users
def inputDecimalInteger(message):
    print(message)
    
    while True:
        number = input("Inserici un numero intero: ")
        if isDecimalInteger(number):
            print(number + " OK")
            return int(number)
            
def inputPositiveDecimalInteger(message):
    print(message)
    while number := inputDecimalInteger('') <= 0:
        print("Corretto numero intero, ma non e' positivo")
        
    return number
    
def inputNegativeDecimalInteger(message):
    print(message)
    while number := inputDecimalInteger('') >= 0:
        print("Corretto numero intero, ma non e' negativo")
        
    return number

def inputNonPositiveDecimalInteger(message):
    print(message)
    while number := inputDecimalInteger('') > 0:
        print("Corretto numero intero, ma deve essere non positivo")
        
    return number
    
def inputNonNegativeDecimalInteger(message):
    print(message)
    while number := inputDecimalInteger('') <= 0:
        print("Corretto numero intero, ma non e' non negativo")
        
    return number

def inputFloating(message):
    print(message)
    
    while True:
        number = input("Inserici un numero intero: ")
        if isFloating(number):
            print(number + " OK")
            return float(number)
            

# launch main function only
# if is not a module
if __name__ == "__main__":
    function_name = ' '
    while function_name != '':
        function_name = input("Digita il nome di una funzione per continuare, INVIO per terminare: ").strip()
        
        match function_name:
            case "inputDecimalInteger":
                inputDecimalInteger("Collaudo della funzione inputDecimalInteger\nScrivi, nell'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,i n risposta alle richieste del programma: \"+ 23\", \" - 34\", \"x\", \"12x\", \"12\".\n Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
            case "inputPositiveDecimalInteger":
                inputPositiveDecimalInteger("Collaudo della funzione inputDecimalInteger\nScrivi, nell'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,i n risposta alle richieste del programma: \"+ 23\", \" - 34\", \"x\", \"12x\", \"12\".\n Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
            case "inputNegativeDecimalInteger":
                inputNegativeDecimalInteger("Collaudo della funzione inputDecimalInteger\nScrivi, nell'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,i n risposta alle richieste del programma: \"+ 23\", \" - 34\", \"x\", \"12x\", \"12\".\n Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
            case "inputNonPositveDecimalInteger":
                inputNonPositiveDecimalInteger("Collaudo della funzione inputDecimalInteger\nScrivi, nell'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,i n risposta alle richieste del programma: \"+ 23\", \" - 34\", \"x\", \"12x\", \"12\".\n Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
            case "inputNonNegativeDecimalInteger":
                inputNonNegativeDecimalInteger("Collaudo della funzione inputDecimalInteger\nScrivi, nell'ordine, le seguenti stringhe, senza le virgolette ma con attenzione agli spazi,i n risposta alle richieste del programma: \"+ 23\", \" - 34\", \"x\", \"12x\", \"12\".\n Soltanto l'ultima stringa deve essere accettata e visualizzata dal programma.")
            case "inputFloating":
                inputFloating("Collaudo della funzione inputFloating.\nScrivi nell'ordine le seguenti stringhe, senza virgolette, ma con attenzione agli ultimi spazi:\n' -3', '+2.0e+1027\nEntrambe le stringhe possono essere riconosciute come valide")
            case "inputYesNo":
                inputYesNo("Inserisci SI o NO: ", "SI", "NO")
            case "inputStringStartingWith":
                inputStringStartingWith("Trova la stringa che inizia con la parola 'fic': ", 'fic')
            case "inputStringEndingWith":
                inputStringEndingWith("Trova la stringa che finisce con la parola 'fic': ", 'fic')
            case "inputStringContaining":
                inputStringContaining("Trova la stringa che contiene con la parola 'fic': ", 'fic')
            case "":
                print("Fine del programma")
            case _:
                print("Funzione non trovata, riprova")
    

