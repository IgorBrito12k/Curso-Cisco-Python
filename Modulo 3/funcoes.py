# Sua primeira função
print("Entre um valor: ")
a = int(input())

print("Entre um valor: ")
b = int(input())

print("Entre um valor: ")
c = int(input())
print()

# primeira função

def message():
    print("Entre um valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
print()

# RESUMO DA SEÇÃO

# Você pode definir uma função que não aceita argumentos
def message(): # definindo uma função
    print("Olá") # o corpo da função
 
message() # chamando a função
print()

# Você pode definir uma função que aceita argumentos

def hello(name): # definindo uma função
    print("Olá,", name) # o corpo da função
 
 
name = input("Entre um nome: ")
 
hello(name) # chamando a função