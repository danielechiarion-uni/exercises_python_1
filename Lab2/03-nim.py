import random

# function to find the perfect number
# to use for the computer]
# extract the highest possible in order to finish it quickly
def find_perfect_number(number):
    # starting from two find the closest 
    # number to the one indicated
    pow2 = 2
    while pow2 - 1 < number:
        pow2 *= 2
    
    if pow2 - 1 == number:
        return pow2 - 1
    else:
        return pow2 // 2 - 1
        
# function to return if a number
# is already private number
def is_perfect_number(number):
    return find_perfect_number(number) == number
    
# function to understand if it's user time
def is_user_time(counter, starting_turn):
    return (counter % 2 == 0 and not starting_turn) or (counter % 2 != 0 and starting_turn)

# define starting variables
command_input = ""
while command_input != "STOP":
    marbles_number = random.randint(10, 100) # generate the number of marbles
    pc_mode = random.randint(0,1) # select respectively stupid or clever mode of the pc
    starting_turn = random.randint(0,1) # select whether the user or the pc has to start first\
    counter = 0 # counter to understand the turn
    
    # print the current game information
    print(f"Si gioca con {marbles_number} biglie")
    print(f"Il pc gioca in modalita' {'STUPIDO' if not pc_mode else 'INTELLIGENTE'}")
    print(f"Inizia il gioco: {'UTENTE' if not starting_turn else 'PC'}")
    
    while marbles_number > 1:
        # select whether the user or the 
        # pc has to do the move
        if is_user_time(counter, starting_turn):
            print("E' il turno di UTENTE!")
            input_marbles = 0
            while input_marbles < 1 or input_marbles > marbles_number // 2:
                input_marbles = int(input("Inserisci un numero di biglie per continuare: "))
        else:
            print("E' il turno di PC!")
            if pc_mode and not is_perfect_number(marbles_number):
                input_marbles = find_perfect_number(marbles_number)
            else:
                input_marbles = random.randint(1, marbles_number//2)
        
        # report the result
        marbles_number -= input_marbles
        print(f"Sono state estratte {input_marbles} biglie")
        print(f"Sono rimaste {marbles_number}  biglie")
        counter += 1 # update the counter
        
    if is_user_time(counter, starting_turn):
        print("Ha vinto il PC! Utente SEI STUPIDO!")
    else:
        print("Ha vinto l'UTENTE! Questo codice te l'ha detto Emma AI!")
    
    command_input = input("Desideri proseguire? Spero di NO, quindi digita 'STOP'\n")
            
