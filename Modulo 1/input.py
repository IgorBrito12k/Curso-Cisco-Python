# A função input()
print("Conte-me qualquer coisa...")
anything = input()
print("Hum...", anything, "...Realmente?")
print()

# A função input() com um argumento
algo = input("A Camila é a minha namorada...")
print("Hum...", algo, "...Realmente?")
print()

# O resultado da função input()
# numero = input("Digite um número: ")
# resultado = numero ** 2.0
# print(numero, "elevado a 2 é", resultado) #Erro

# Conversão de tipo (tipo de conversões)
numero = float(input("Digite um número: "))
resultado = numero ** 2.0
print(numero, "elevado a 2 é", resultado)
print()

# Mais informações sobre input() e conversão de tipos
perna_a  = float(input("Insira o comprimento da primeira perna: "))
perna_b  = float(input("Insira o comprimento da segunda perna: "))
hipotenusa = (perna_a ** 2 + perna_b ** 2) ** .5
print("O comprimento da hipotenusa é: ", hipotenusa)
print()

# Operadores de string
nome = input("Posso ter seu primeiro nome, por favor? ")
sobrenome = input("Posso ter seu sobrenome nome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + nome + " " + sobrenome + ".\n")

# Replicação
print("Igor" * 3)
print(3 * "an")
print("2" * 5)
print()

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+\n")

# LAB Simples entradas e saídas
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("\nIsso é tudo, pessoal!\n")

# LAB Operadores e Expressões
x = float(input("Digite o valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)
print()

# LAB Operadores e Expressões 2
hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
mins = mins + dura # encontre um total de todos os minutos
hour = hour + mins // 60 # encontre um número de horas escondido em minutos e atualize a hora
mins = mins % 60 # minutos corretos para cair no intervalo (0..59)
hour = hour % 24 # horas corretas para cair no intervalo (0..23)

print("\nSaída prevista: ", hour, ":", mins, sep='')
print()

# Resumo
name = input("Digite seu nome: ")
print("Olá, " + name + ". Prazer em conhecê-lo!")
print()

num_1 = input("Digite o primeiro número: ") # Digite 12
num_2 = input("Digite o segundo número: ") # Digite 21
 
print(num_1 + num_2) # o programa retorna 1221
print()

my_input = input("digite alguma coisa: ") # Exemplo de entrada: Olá
print(my_input * 3) # Saída esperada: OláOláOlá