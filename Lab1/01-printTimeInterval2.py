time1 = int(input("Inserisci primo orario: "))
time2 = int(input("Inserisci secondo orario: "))

# before calculating the difference transform the 
# time given all to minutes, so as to avoid conflicts between
# decimal and time system
time1 = time1//100*60 + time1%100;
time2 = time2//100*60 + time2%100;

# calculate the difference
# if the difference between time one and two is positive, take the module of 24 in order not to have more than a day's difference
# if it's negative, it means we have to consider the 24 hours, which remain the same after the module
difference = (time2 - time1) % (24*60)

# calculate hours and minutes
hours = difference // 60
minutes = difference % 60
print(f"Tempo trascorso: {hours} ore e {minutes} minuti")
