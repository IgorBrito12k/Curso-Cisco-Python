# Igualdade: o operador de igualdade (==)
var = 0 
print(var == 0)
var = 1 
print(var == 0)
print()

# Desigualdade: o operador de desigualdade (!=)
var = 0  
print(var != 0)
var = 1  
print(var != 0)
print()

# Operadores de comparação: maior que
amazonas = ''
nilo = ''
nilo > amazonas

#Operadores de comparação: maior ou igual a
velocidadeMaxima = 0
velocidadeMaxima <= 120

# Prioridade	Operadora	
#     1	        +, -	        unário
#     2	        **	
#     3	        *, /, //, %	
#     4	        +, -	        ⁪binário
#     5	        <, <=, >, >=	
#     6	        ==, !=	

# Lab Variaveis
n = int(input("Digite um número: "))
print(n >= 100)
print()

# Condições e execução condicional
var = tempo_bom = ''
var = va_caminhar = ''
var = va_jantar = ''

if tempo_bom:
    va_caminhar()
va_jantar()

# Execução condicional: o comando if
var = contador_ovelha = 0
var = dormir_e_sonhar = False
var = faca_cama = True
var = tome_banho = True
var = alimentar_cachorro = True

if contador_ovelha >= 120: # Avaliar uma expressão de teste
        dormir_e_sonhar()  # Execute se a expressão de teste for verdadeira

if contador_ovelha >= 120:
      faca_cama()
      tome_banho()
      dormir_e_sonhar()

alimentar_cachorro()


# Execução condicional: o comando if-else
var = condicao_True_False = False
var = faca_se_for_true = ''
var = faca_se_for_false = ''

if condicao_True_False:
    faca_se_for_true
else:
    faca_se_for_false

# O comando if-else: mais execução condicional
var = vai_teatro = True
var = divirta = True
var = curte_filme = True
if tempo_bom:
    va_caminhar()
else:
    vai_teatro()
va_jantar()


if tempo_bom:
    va_caminhar()
    divirta()
else:
    vai_teatro()
    curte_filme()
va_jantar()

# Comandos if-else aninhados
var = encontrar_bom_restaurante = True
var = coma_lanche = True
var = ingresso_disponivel = False
var = vai_shopping = False

if tempo_bom:
        if encontrar_bom_restaurante:
          va_jantar()
        else:
            coma_lanche()
else:
    if ingresso_disponivel:
     vai_teatro()
    else:
     vai_shopping()

# O comando elif
var = mesa_pronta = True
var = jogue_xadrez = False

if tempo_bom:
    va_caminhar()
elif ingresso_disponivel:
    vai_teatro()
elif mesa_pronta:
    va_jantar()
else:
    jogue_xadrez()

# Análise de amostras de código

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
 
if numero1 > numero2:
    maiorNumero = numero1
else:
    maiorNumero = numero2
 
print("O maior número é:", maiorNumero)
print()

# Exemplo 2
#Ler dois números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
 
# Escolha o número maior
if numero1 > numero2: maiorNumero = numero1
else: maiorNumero = numero2
 
# Imprimir o resultado
print("O maior número é:", maiorNumero)
print()

# Exemplo 3
# Leia três números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
 
# Assumimos temporariamente que o primeiro número
# é o maior deles.
# Em breve verificaremos isso.
maiorNumero = numero1
 
# Nós verificamos se o segundo número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if numero2 > maiorNumero:
    maiorNumero = numero2
 
# Nós verificamos se o terceiro número é maior que o maior_número atual
# e atualize o maior_número, se necessário.
if numero3 > maiorNumero:
    maiorNumero = numero3
 
# Imprimir o resultado
print("O maior número é:", maiorNumero)

# Pseudocódigo e introdução aos loops
 
 
