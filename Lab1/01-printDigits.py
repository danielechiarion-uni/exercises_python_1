textNumber = int(input('Inserisci numero: ')) # input the number

# divide per progressive powers of 10
print(str(int(textNumber/10000)%10))
print(str(int(textNumber/1000)%10))
print(str(int(textNumber/100)%10))
print(str(int(textNumber/10)%10))
print(str(int(textNumber/1)%10))
