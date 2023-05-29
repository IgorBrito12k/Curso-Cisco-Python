numbers = [10, 5, 7, 2, 1]

# Indexando listas
numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers)  # Imprimindo o conteúdo original da lista.
print()

numbers[0] = 111
print("Novo conteúdo da lista: ", numbers)  # Conteúdo atual da lista.
print()

numbers[1] = numbers[4]  # Copiando o valor do quinto elemento para o segundo.
print("Novo conteúdo da lista:", numbers)  # Printing Conteúdo atual da lista.
print()

# Acesso ao conteúdo da lista
print(numbers[0]) # Acessando o primeiro elemento da lista
print()

numbers = [10, 5, 7, 2, 1]
print("Conteúdo da lista original:", numbers) # Imprimindo o conteúdo da lista original.
print()

print ("\nList length:", len (numbers)) # Imprimindo o comprimento da lista.
print()

print(numbers) # Imprimindo toda a lista.
print()

# A função len()
#Remover elementos de uma lista
del numbers[1]
print(len(numbers))
print()
print(numbers)
print()

# Os índices negativos são legais
numbers = [111, 7, 2, 1]
print(numbers[-1])
print()
numbers = [111, 7, 2, 1]
print(numbers[-2])
print()

# LAB   Básico de listas

hat_list = [1, 2, 3, 4, 5]  # Esta é uma lista atual de números ocultos no hat.
# Etapa 1: escreva uma linha de código que solicita ao usuário
# que substitua o número do meio por um número inteiro inserido pelo usuário.
hat_list[2] = int(input("Insira um número inteiro: "))
# Etapa 2: escreva uma linha de código que remova o último elemento da lista.
hat_list.pop()
# Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual.
print(len(hat_list))
print(hat_list)
print()

# Funções x métodos

# Adicionando elementos a uma lista: append() e insert()
numbers = [111, 7, 2, 1]

print(len(numbers))
print(numbers)
print()

numbers.append(4) # Ele pega o valor do argumento e o coloca no final da lista
print()

print(len(numbers))
print(numbers)
print()

numbers.insert(0, 222) # Ele pode adicionar um novo elemento em qualquer lugar na lista

print(len (numbers))
print(numbers)
print()

# Criando uma lista vazia.

# append
my_list = [] 

for i in range(5):
   my_list.append (i + 1)

print (my_list)

# insert
my_list = [] 

for i in range(5):
   my_list.insert (0, i + 1)

print (my_list)
print()

# Utilização de listas

my_list = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list)):

  total += my_list[i]

print(total)

# O segundo aspecto do loop

my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)
print()

# Listas em ação

# jeito tradicional de trocar valores das variáveis
auxiliary = 0
variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
print('variavel 1: ',variable_1, '. Variavel 2: ',variable_2)

# O Python oferece uma maneira mais conveniente de fazer a troca

variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1
print('variavel 1: ',variable_1, '. Variavel 2: ',variable_2)
print()

my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
print()

# LAB   O básico de listas ‒ os Beatles

# Etapa 1: criar uma lista vazia chamada beatles
beatles = []

# Etapa 2: use o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney e George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Etapa 3: Use o loop for e o método append() para solicitar que o usuário adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best
for _ in range(2):
    member = input("Digite o nome de um membro da banda: ")
    beatles.append(member)

# Etapa 4: use a instrução del para remover Stu Sutcliffe e Pete Best da lista
del beatles[3:5]
# Ou del beatles[3:5] se quiser ser mais explícito

# Etapa 5: Use o método insert() para adicionar Ringo Starr ao início da lista
beatles.insert(0, "Ringo Starr")

# Imprimir a lista atualizada
print(beatles)
print()

# RESUMO DA SEÇÃO

# A lista é um tipo de dados em Python usado para armazenar vários objetos
my_list = [1, None, True, "eu sou um barbante", 256, 0]
 
# 2. As listas podem ser indexadas e atualizadas
my_list = [1, None, True, 'eu sou um barbante', 256, 0]
print(my_list[3])  # outputs: eu sou um barbante
print(my_list[-1])  # outputs: 0
print()

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'eu sou um barbante', 256, 0]
print()

my_list.insert(0, "primeiro")
my_list.append("último")
print(my_list)  # outputs: ['primeiro', 1, '?', True, 'eu sou um barbante', 256, 0, 'último']
print()

# As listas podem ser aninhadas
my_list = [1, 'a', ["lista", 64, [0, 1], False]]

# Os elementos e as listas podem ser excluídos
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
print()

del my_list  # exclui toda a lista

# As listas podem ser iteradas usando o loop for
my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
 
for color in my_list:
    print(color)
print()

# A função len() pode ser usada para verificar o comprimento da lista
my_list = ["branco", "roxo", "azul", "amarelo", "verde"]
print(len(my_list))  # outputs 5
 
del my_list[2]
print(len(my_list))  # outputs 4