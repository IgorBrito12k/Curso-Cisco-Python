# A ordenção em bolhas

# Agora que você pode efetivamente manipular os elementos das listas,
# é hora de aprender a classificá-las. Muitos algoritmos de classificação 
# foram inventados até agora, que diferem muito na velocidade e na
# complexidade. Vamos mostrar um algoritmo muito simples, fácil de
# entender, mas infelizmente não muito eficiente. É usado muito raramente,
# e certamente não para listas grandes e extensas.

# Digamos que uma lista pode ser classificada de duas maneiras:

# crescente (ou mais precisamente - não decrescente) - 
# se, em cada par de elementos adjacentes, o primeiro elemento não for maior que o último;
# diminuindo (ou mais precisamente - não aumentando) -
# se em cada par de elementos adjacentes o primeiro elemento não for menor que o último.

# Ordenando uma lista
my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
print()

# A ordenação por bolhas - versão interativa
my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))
print()

for i in range(num):
 val = float(input("Entre com a lista de elementos:"))
 my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
print()

# Se você quiser que o Python classifique sua lista
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# RESUMO DA SEÇÃO

# Você pode usar o método sort() para classificar elementos de uma lista
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
print()

# Há também um método de lista chamado revers(), que você pode usar para reverter a lista
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]