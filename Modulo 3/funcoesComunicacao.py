# Funções parametrizadas
def message(number):
    print("Digite um número:", number)

message(5)
print()

# É legal e possível ter uma variável com o mesmo parâmetro de função
def message(number):
    print("Digite um número:", number)
 
number = 1234
message(1)
print(number)
print()


def message(what, number):
    print("Entrar", what, "número", number)
 
message("telefone", 11)
message("preço", 5)
message("número", "número")
print()

# Passagem de parâmetros posicionais

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
print()

# Passagem de parametro por palavra-chave
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
print()


# Mistura de argumentos posicionais e de palavras-chave
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(4, 3, c = 2)
print()

# Funções parametrizadas – mais detalhes
def introduction(first_name="John", last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)

introduction("James", "Doe")
introduction("Henry")
introduction()
print()

# RESUMO DA SEÇÃO

#  Você pode passar informações para funções usando parâmetros
def hi(name):
    print("Oi,", name)
 
hi("Greg")
print()

# Um exemplo de função de dois parâmetros:

def hi_all(name_1, name_2):
    print("Oi,", name_2)
    print("Oi,", name_1)
 
hi_all("Sebastian", "Konrad")
print()

# Um exemplo de função de três parâmetros:
def address(street, city, postal_code):
    print("Seu endereço é:", street, "St.,", city, ",", postal_code)
 
s = input("Street: ")
p_c = input("Código postal: ")
c = input("Cidade: ")
address(s, c, p_c)
print()

# Você pode passar argumentos para uma função usando as seguintes técnicas
#Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # saídas: 3
subtra(2, 5) # saídas: -3
print()
 
#Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # saídas: 3
subtra(b=2, a=5) # saídas: 3
print()
#Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # saídas: 3
subtra(5, 2) # saídas: 3
print()

# Você pode usar a técnica de passagem de argumento da palavra-chave para predefinir um valor para um determinado argumento
def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # saídas: Andy Smith
name("Betty", "Johnson") # saídas: Betty Johnson (the keyword argument replaced by "Johnson")