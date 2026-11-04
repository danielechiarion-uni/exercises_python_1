def euclide_MCD(m, n):
    # apply the rule of Euclide given to solve the problem
    if m % n == 0:
        return n
        
    return euclide_MCD(n, m%n)

m = int(input("Inserisci il primo numero: "))
n = int(input("Inserisci il secondo numero: "))

# make sure m>n in order to make the function work
if m < n:
    m,n = n,m
    
mcd = euclide_MCD(m,n)
print(f"Il MCD secondo Euclide tra {m} e {n} e' {mcd}")
