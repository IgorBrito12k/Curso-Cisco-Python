# Expressões lógicas
# Exemplo 1:
var = 0
print(var > 0)
print(not (var <= 0))
 
 
# Exemplo 2:
print(var != 0)
print(not (var == 0))

# Valores lógicos vs. bits únicos

# i = 1
# j = not not i

# Operadores bit a bit
# Aqui estão todos eles:

# & (e comercial) - conjunção bit a bit;
# | (barra) - disjunção bit a bit;
# ~ (til) - negação bit a bit;
# ^ (circunflexo) ‒ bit a bit exclusivo ou (xor).

#Deslocamento binário para a esquerda e deslocamento binário para a direita
var = 17
var_right = var >> 1
var_left = var << 2
print (var, var_left, var_right)

# Prioridade	Operadora	
# 1	        ~, +, -	    unário
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	    ⁪binário
# 5	        <<, >>	
# 6	        <, <=, >, >=	
# 7	        ==, !=	
# 8	        &	
# 9	        |	
# 10	        =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	

# RESUMO DA SEÇÃO
# 1. O Python é compatível com os seguintes operadores lógicos:

# and → se ambos os operandos forem verdadeiros, a condição é verdadeira, por exemplo, (True and True) é True,
# or → se qualquer um dos operandos for verdadeiro, a condição é verdadeira, por exemplo, (True or False) é True,
# not → retorna falso se o resultado for verdadeiro e retorna verdadeiro se o resultado for falso, por exemplo, not True for

x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
print()

x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
print()