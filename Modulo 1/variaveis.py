var = 1
print(var)
print()

#Como usar uma variável
var = 2
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print()

var = "3.8.5"
print("Versao Python: " + var)
print ()

#Como atribuir um novo valor a uma variável já existente
var = 1
print(var)
var = var + 1
print(var)
print()

#Solução de problemas matemáticos simples
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)
print ()

#LAB Variáveis

john = 3
mary = 5
adam = 6

print(john, mary, adam, sep=',')

total_apples = john + mary + adam
print(total_apples)
print ()

#Operadores atalhos
# x = x * 2
# x *= 2

# sheep = sheep + 1
# sheep += 1

#LAB Variáveis ‒ um simples conversor
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
#round de arredondar
print(miles, "milhas e", round(miles_to_kilometers, 2), "quilometros")
print(kilometers, "quilometros e", round(kilometers_to_miles, 2), "milhas")
print ()

#LAB Operadores e Expressões
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)