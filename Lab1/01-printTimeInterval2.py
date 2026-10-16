time1 = int(input("Inserisci primo orario: "))
time2 = int(input("Inserisci secondo orario: "))

# calculate the difference
# if the difference between time one and two is positive, take the module of 24 in order not to have more than a day's difference
# if it's negative, it means we have to consider the 24 hours, which remain the same after the module
difference = time1 - time2

# calculate hours and minutes
hours = int((24 + difference / 100) % 24)
minutes = (difference % 100)
print(f"Tempo trascorso: {hours} ore e {minutes} minuti")
