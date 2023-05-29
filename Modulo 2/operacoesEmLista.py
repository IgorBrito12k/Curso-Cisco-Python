# A vida interior das listas
list_1 = [1]
list_2 = list_1
list_1 [0] = 2
print(list_2)

# Os poderes do fatiamento
list_1 = [1]
list_2 = list_1[:] # [:] é capaz de produzir uma nova lista.
list_1[0] = 2
print(list_2)
print()

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
print()

# Fatias - índices negativos

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
print()

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# Mais sobre a instrução del 
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
print()

# excluir todos os elementos
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
print()

# Os operadores in e not in

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
print()

# Listas - alguns programas simples
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)
print()

# Agora vamos encontrar a localização de um determinado elemento dentro de uma lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
print()

# LAB   Operações com listas ‒ básico
# Lista de origem (exemplo)
numbers = [1, 2, 3, 4, 4, 5, 2, 6, 1]

# Lista temporária para armazenar os números não repetidos
unique_numbers = []

# Percorrendo a lista de origem
for number in numbers:
    # Verificando se o número já existe na lista temporária
    if number not in unique_numbers:
        # Adicionando o número à lista temporária se ele ainda não estiver lá
        unique_numbers.append(number)

# Imprimindo a lista resultante sem repetições
print(unique_numbers)
print()

# RESUMO DA SEÇÃO
# Se você tiver uma lista list_1, a seguinte atribuição: list_2 = list_1 
# não faz uma cópia da lista list_1, mas faz com que as variáveis list_1 e
# list_2 apontem para uma mesma lista na memória.

vehicles_one = ['carro', 'bicicleta', 'motor']
print(vehicles_one) # outputs: ['carro', 'bicicleta', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # exclui 'carro'
print(vehicles_two) # outputs: ['bicicleta', 'motor']
print()

# Se quiser copiar uma lista ou parte da lista, você pode fazer isso dividindo
colors = ['vermelho', 'verde', 'laranja']
 
copy_whole_colors = colors[:]  # copie a lista inteira
copy_part_colors = colors[0:2]  # copiar parte da lista

# Você também pode usar índices negativos para executar fatias.
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
print()

# Os start de end e fim são opcionais ao executar uma fatia: list[start:end]
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
print()

# Você pode excluir fatias usando a instrução del
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
 
del my_list[:]
print(my_list)  # deletes the list content, outputs: []
print()

# Você pode testar se alguns itens existem em uma lista ou não estão usando as palavras-chave in e not in
my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False