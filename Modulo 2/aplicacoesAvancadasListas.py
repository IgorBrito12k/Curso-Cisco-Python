from pickle import EMPTY_LIST

# -------------------------------------------
squares = [x ** 2 for x in range(10)]
print()

# -------------------------------------------
twos = [2 ** i for i in range(8)]
print()

# -------------------------------------------
odds = [x for x in squares if x % 2 != 0 ]
print()

# Matrizes bidimensionais

board = []
 
for i in range(8):
    row = [EMPTY_LIST for i in range(8)]
    board.append(row)

# Natureza multidimensional das listas: aplicações avançadas
temps = [[0.0 for h in range(24)] for d in range(31)]

#
# A matriz é magicamente atualizada aqui.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura média ao meio-dia:", average)

# Agora, encontre a temperatura mais alta durante todo o mês
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("A maior temperatura foi:", highest)

# Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "dias estavam quentes.")

# RESUMO DA SEÇÃO

#A compreensão da lista permite criar novas listas a partir das existentes de forma concisa e elegante.
cubed = [num ** 3 for num in range(5)]
print(cubed) # outputs: [0, 1, 8, 27, 64]
print()

# Você pode usar listas aninhadas
# Uma tabela de quatro colunas/quatro linhas ‒ uma matriz bidimensional (4x4)
 
table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print('Tabela: ')
print(table)
print()
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'
print()

#  Você pode aninhar quantas listas desejar, criando assim listas n-dimensionais
# Cubo - uma matriz tridimensional (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print('Cubo: ')
print(cube)
print()
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
print()