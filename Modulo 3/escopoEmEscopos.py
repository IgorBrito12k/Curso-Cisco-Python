# Funções e escopos
def my_function():
 print("Eu conheço aquela variável?", var)


var = 1
my_function()
print(var)
print()

# Vamos fazer uma pequena alteração no código
def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
 
var = 1
my_function()
print(var)
print()

#  Funções e escopos: a palavra-chave global
def my_function():
 global var
 var = 2
 print("Eu conheço aquela variável?", var)

var = 1
my_function()
print(var)
print()

# Como a função interage com seus argumentos
def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)

var = 1
my_function(var)
print(var)
print()

# alterar o valor do parâmetro não se propaga fora da função
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
print()

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
print()

# RESUMO DA SEÇÃO

#  Uma variável que existe fora de uma função tem escopo dentro do corpo da função
# Exemplo 1
var = 2
 
def mult_by_var(x):
    return x * var
 
print(mult_by_var(7)) # saídas: 14

# a menos que a função defina uma variável com o mesmo nome (exemplo 2 e exemplo 3)
#Exemplo 2:
def mult(x):
    var = 5
    return x * var

print(mult(7)) # saídas: 35

# Exemplo 3:

def mult(x):
    var = 7
    return x * var

var = 3
print(mult(7)) # saídas: 49

#Exemplo 4:
def adding(x):
    var = 7
    return x + var

print(adding(4)) # saídas: 11
print(var) # NameError
print()

# Você pode usar a palavra-chave global seguida por um nome de variável para tornar o escopo da variável global
var = 2
print(var) # saídas: 2
 
def return_var():
    global var
    var = 5
    return var

print(return_var()) # saídas: 5
print(var) # saídas: 5