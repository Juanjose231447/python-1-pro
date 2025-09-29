import random

print ("calculadora de numeros primos")
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

numero = int(input("ingresa un numero:"))
if es_primo(numero):
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} no es un numero primo")

#estaba aburrido y no sabia que aser XD
print ("steel ball run sale mañana")
