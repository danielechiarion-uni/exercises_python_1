# define rule to check password length
def rule1(password):
    PASSWORD_LENGTH = 8
    return len(password) >= 8
    
# define rule to check if the 
# password contains a capital case letter
def rule2(password):
    for character in password:
        if character >= 'A' and character <= 'Z':
            return True
    
    return False
    
# define rule to check if the 
# password contains a lower case letter
def rule3(password):
    for character in password:
        if character >= 'a' and character <= 'z':
            return True
            
    return False
    
# define rule to check if the 
# password contains at least a number
def rule4(password):
    for character in password:
        if character >= '0' and character <= '9':
            return True
    
    return False
    
# define rule to check if the password contains
# at least a special character
def rule5(password):
    for character in password:
        if (character <= 'A' or character <= 'Z') and (character <= 'a' or character >= 'z') and (character <= '0' or character >= '9'):
            return True
            
    return False
    
# define rule to check if the password
# does not contain spaces
def rule6(password):
    return not ' ' in password
    
# define rule to check if the password
# does not contain repeated characters
def rule7(password):
    for character in password:
        if password.count(character) > 1:
            return False
    
    return True

# define function to see if the password is valid
def isValid(password):
    validity = True # define operator to use inside the control
    
    # check every rule and
    # display the error
    if not rule1(password):
        print("La password non e' lunga almeno 8 caratteri")
        validity = False
    if not rule2(password):
        print("La password non contiene lettere maiuscole")
        validity = False
    if not rule3(password):
        print("La password non contiene lettere minuscole")
        validity = False
    if not rule4(password):
        print("La password non contiene numeri")
        validity = False
    if not rule5(password):
        print("La password non contiene caratteri speciali")
        validity = False
    if not rule6(password):
        print("La password non deve contenere spazi")
        validity = False
    if not rule7(password):
        print("La password non deve contenere caratteri ripetuti")
        validity = False
        
    return validity

# define bool for the first time
# then repeat till the password is OK
first_time = True
password = ""
while first_time or not isValid(password):
    first_time = False
    password = input("Inserisci la password: ")
    
print("Password OK")
