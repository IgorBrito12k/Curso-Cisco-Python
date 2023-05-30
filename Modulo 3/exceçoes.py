# Erros - o pão diário do desenvolvedor

# Erros nos dados vs. erros no código

#  Quando os dados não são o que deveriam ser
value = int(input('Digite um número natural: '))
print('O recíproco de', value, 'é', 1/value)
print()

# O ramo de tentativa exceto
#try:
 # Esse é um lugar
 # que você pode fazer algo
 # sem pedir permissão.
#except:
 # Esse lugar é dedicado
 # apenas para implorar por persão.

# A exceção confirma a regra
try:
 value= int (input('Insira um número natural:')) 
 print('O recíproco de', value, 'é', 1 / value) 
except: 
 print('Não sei o que fazer.')
print()

# Como lidar com mais de uma exceção

# Duas exceções após um try
try:
 value = int(input('Digite um número natural: '))
 print('O recíproco de', value, 'é', 1/value) 
except ValueError:
 print('Eu não sei o que fazer.') 
except ZeroDivisionError:
 print('A divisão por zero não é permitida em nosso Universo.')

# A exceção padrão e como usá-la

try:
 value = int (input('Insira um número natural:')) 
 print('O recíproco de', value, 'é', 1 / value) 
except ValueError:
 print('Não sei o que fazer.' ) 
except ZeroDivisionError:
 print('Divisão por zero não é permitida em nosso universo.') 
except: 
 print('algo de estranho aconteceu aqui ... Desculpe! ')

# Algumas exceções úteis

#ZeroDivisionError
#sso aparece quando você tenta forçar o Python a executar qualquer operação que provoque uma divisão na qual o divisor é zero ou é indistinguível de zero.

# ValueError
# Espere essa exceção ao lidar com valores que podem ser usados de forma inadequada em algum contexto.

# TypeError
# Essa exceção aparece quando você tenta aplicar dados cujo tipo não pode ser aceito no contexto atual. 
short_list = [1]
one_value = short_list[0.5]

# AttributeError
#Essa exceção chega, entre outras ocasiões, quando você tenta ativar um método que não existe em um item com o qual está lidando.
short_list = [1]
short_list.append(2)
short_list.depend(3)

#SyntaxError
# Essa exceção é gerada quando o controle atinge uma linha de código que viola a gramática do Python.
