# Uma tupla é um tipo de sequência imutável. Pode se comportar como uma lista, mas não pode ser modificado in situ

# Tuplas
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)
print()

# Como criar uma tupla
empty_tuple = ()

# Como usar uma tupla
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
print()

for elem in my_tuple:
 print(elem)
print()

# O que mais as tuplas podem fazer por você?
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)
print()

# Dicionários

# Como fazer um dicionário
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(dictionary['gato'])
print(phone_numbers['Suzy'])
print()

# O código a seguir pesquisa com segurança algumas palavras em francês
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")
print()

# Quando você escreve uma expressão grande ou longa, pode ser uma boa ideia mantê-la alinhada verticalmente.
# recuo suspenso
# Exemplo 1:
dictionary = {
              "gato": "chat",
              "cachorro": "chien",
              "cavalo": "cheval"
}
# Exemplo 2:
phone_numbers = {'chefe': 5551234567,
              'Suzy': 22657854310
}
 
# Métodos e funções de dicionário

# O método keys()
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
print()

# Vamos agora dar uma olhada em um método de dicionário chamado items()
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for english, french in dictionary.items():
    print(english, "->", french)
print()

# Modificação e adição de valores

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)
print()

# A função sorted()
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for french in dictionary.values():
    print(french)
print()

# Adição de uma nova chave
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['swan'] = 'cygne'
print(dictionary)
print()

# Você também pode inserir um item em um dicionário usando o método update()
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)
print()

# Removendo uma chave
#a remoção de uma chave sempre causará a remoção do valor associado. Os valores não podem existir sem as chaves.
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
del dictionary['cachorro']
print(dictionary)
print()

# Para remover o último item de um dicionário, você pode usar o método popitem()
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary.popitem()
print(dictionary)    # saídas: {'gato': 'chat', 'cachorro': 'chien'}
 
# Tuplas e dicionários podem trabalhar juntos
school_class = {}

while True:
 name = input("Digite o nome do aluno: ")
 if name == '':
    break
 
 score = int(input("Insira a pontuação do aluno (0-10): "))
 if score not in range(0, 11):
    break
 
 if name in school_class:
    school_class[name] += (score,)
 else:
    school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
 adding = 0
 counter = 0
 for score in school_class[name]:
    adding += score
    counter += 1
 print(name, ":", adding / counter)
print()

# RESUMO DA SEÇÃO

# As tuplas são ordenadas e coleções imutáveis (imutáveis) de dados.
my_tuple = (1, 2, True, "um barbante", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "um barbante", (3, 4), [5, 6], None]
print(my_list)
print()

#Você pode criar uma tupla vazia como esta:
empty_tuple = ()
print(type(empty_tuple))    # saídas: 
print()

# Uma tupla de um elemento pode ser criada da seguinte forma:
one_elem_tuple_1 = ("um", )    # Colchetes e uma vírgula.
one_elem_tuple_2 = "um",       # Sem colchetes, apenas vírgula.
 
# Se você remover a vírgula, você dirá ao Python para criar uma variável, não uma tupla

# Você pode acessar elementos de tupla indexando-os
my_tuple = (1, 2.0, "corda", [3, 4], (5, ), True)
print(my_tuple[3])    # saídas: [3, 4]
print()

# Você pode percorrer os elementos de uma tupla (exemplo 1), 
# verificar se um elemento específico está (não) presente em uma tupla (exemplo 2), 
# usar a função len() para verificar quantos elementos existem em uma tupla (exemplo 3) , 
# ou até mesmo juntar / multiplicar tuplas (exemplo 4):

# Exemplo 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
print()

# Exemplo 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
print()

# Exemplo 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_2)
print()

# Exemplo 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)
print()

# Pontos chave: dicionários
#Os dicionários são conjuntos de dados indexados *, mutáveis e indexados. 

# my_dictionary = {
#     key1: value1,
#     key2: value2,
#     key3: value3,
# }
 
# Se você quiser acessar um item de dicionário, faça isso fazendo uma referência à sua chave dentro de um par de colchetes (por exemplo, 1) 
# ou usando o método get() (por exemplo, 2):
pol_eng_dictionary = {
    "kwiat": "flor",
    "woda": "água",
    "gleba": "solo"
    }
 
item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # saídas: solo
 
item_2 = pol_eng_dictionary.get("woda")    # ex. 2
print(item_2)    # saídas: água
print()

# Para adicionar ou remover uma chave (e o valor associado), use a seguinte sintaxe:
phonebook = {}    # um dicionário vazio
 
phonebook["Adão"] = 3456783958    # criar/adicionar um par chave-valor
print(phonebook)    # saídas: {'Adão': 3456783958}
 
del phonebook["Adão"]
print(phonebook)    # saídas: {}
print()

# Você também pode inserir um item em um dicionário usando o método update() e remover o último elemento usando o método popitem(), por exemplo:
pol_eng_dictionary = {"kwiat": "flor"}
 
pol_eng_dictionary.update({"gleba": "solo"})
print(pol_eng_dictionary)    # saídas: {'kwiat': 'flor', 'gleba': 'solo'}
 
pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # saídas: {'kwiat': 'flor'}
 
# Você pode usar o loop for para percorrer um dicionário, por exemplo
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
for item in pol_eng_dictionary:
    print(item)
print()
#          woda
#          gleba
 
# Se você deseja percorrer as chaves e os valores de um dicionário, pode usar o método items()
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
print()

# Para verificar se uma determinada chave existe em um dicionário, você pode usar a palavra-chave in
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
if "zamek" in pol_eng_dictionary:
   print("Sim")
else:
   print("Não")
print()

# Você pode usar a palavra-chave del para remover um item específico ou excluir um dicionário. Para remover todos os itens do dicionário, você precisa usar o método clear()
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
print(len(pol_eng_dictionary))    # saídas: 3
del pol_eng_dictionary["zamek"]    # remover um item
print(len(pol_eng_dictionary))    # saídas: 2
 
pol_eng_dictionary.clear()   # remove todos os itens
print(len(pol_eng_dictionary))    # saídas: 0
 
del pol_eng_dictionary    # remove o dicionário
print() 

# Para copiar um dicionário, use o método copy()
pol_eng_dictionary = {
    "zamek": "castelo",
    "woda": "água",
    "gleba": "solo"
    }
 
copy_dictionary = pol_eng_dictionary.copy()
 
