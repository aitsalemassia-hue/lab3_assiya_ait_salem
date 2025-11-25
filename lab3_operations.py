a=15
b=4
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a} // {b} = {a // b}")    
print(f"{a} % {b} = {a % b}")      
print(f"{a} ** {b} = {a ** b}")    
x = 20
y = 15

print(x == y)   # False
print(x != y)   # True
print(x < y)    # False
print(x >= y)   # True
print("\n")
age = 22
permis = True
casier_vierge = False

peut_conduire = (age >= 18) and permis
print(peut_conduire)

peut_louer_voiture = (age >= 21) or (permis and casier_vierge)
print(peut_louer_voiture)

sanction = not casier_vierge
print(sanction)
