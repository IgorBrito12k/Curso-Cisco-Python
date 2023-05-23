# Um loop infinito

# while True:
#     print("Estou preso dentro de um loop.")

# Armazene o maior número atual aqui.
largest_number = -999999999
 
# Insira o primeiro valor.
number = int(input("Digite um número ou digite -1 para parar: "))
 
# Se o número não for igual a -1, continue.
while number != -1:
    # O número é maior que o maior_número?
    if number > largest_number:
        # Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar: "))
 
# Imprima o maior número.
print("O maior número é:", largest_number)
print()

# O loop while: mais exemplos

# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.
 
odd_numbers = 0
even_numbers = 0
 
# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))
 
# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))
 
# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)
print()

# Usando uma variável counter para sair do loop

counter = 5
while counter != 0:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)
print()

#  LAB   Adivinhe o número secreto

secret_number = 777
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
print()

# Fazendo um loop no seu código com for

for i in range(10):
   print("O valor de i é atualmente", i)
print()

# Mais sobre o loop for e a funçao range() com três argumentos
for i in range(2, 8, 3):
  print("O valor de i é atualmente", i)
print()

power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2
print()

# LAB   Essenciais do loop for – contando mississippy
import time 

for i in range(6):
   print(i, "Mississippi")
   time.sleep(1)
print("Pronto ou não, aqui vou eu!")
print()

# As instruções break e continue

# break - exemplo

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")


# continue - exemplo

print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")
print()

# As instruções break e continue: mais exemplo

largest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > maior_numero:
        maior_numero = number

if counter != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")
print()

# LAB   A declaração break – Preso em um loop
counter = 0
chupa = 'Chupacabra'

while True:
    string = str(input("Digite um uma palavra ou digite 'a' para terminar o programa: "))
    if string == "a":
        break
    if string == "Chupacabra":
            chupa = string
            print(chupa)
            break
    else:
        print("Você saiu do loop com sucesso")
print()

# O loop while e o ramo else
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
print()

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# O loop for e o ramo else
for i in range(5):
 print(i)
else:
 print("else:", i)

 #LAB   Essenciais do loop while

