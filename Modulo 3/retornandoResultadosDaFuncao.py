# Efeitos e resultados: a instrução return

# return sem uma expressão
def happy_new_year(wishes=True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return
print("Feliz Ano Novo!")
print()

# return com uma expressão
def boring_function():
    return 123 
x = boring_function()
print("A aborrecimento_função retornou seu resultado. Isso é:", x)
print()

def boring_function():
    print("'Modo de tédio' ON.") 
    return 123
print("Esta lição é interessante!") 
boring_function() 
print("Essa aula é chata...")
print()

# Algumas palavras sobre None

value = None 
if value is None: print("Desculpe, você não carrega nenhum valor")
print()

def strange_function(n):
 if(n % 2 == 0):
    return True
(print(strange_function(4)))

print(strange_function(2))
print(strange_function(1))
print()

# Efeitos e resultados: listas e funções
def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
print(list_sum([5, 4, 3]))
print()

# uma lista pode ser um resultado de função?
def strange_list_fun(n):
 strange_list = []
 
 for i in range(0, n):
    strange_list.insert(0, i)
 return strange_list

print(strange_list_fun(5))
print()

# LAB   Um ano bissexto: escrevendo suas próprias funções
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
print()

#  LAB   Quantos dias: escrevendo e usando suas próprias funções

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month == 2 and is_year_leap(year):
        return 29
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month - 1]

def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        return None
    
    if day > days_in_month(year, month):
        return None
    
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(year, m)
    day_of_year += day
    
    return day_of_year

print(day_of_year(2000, 12, 31))
print()

# LAB   Números primos ‒ como encontrá-los
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
print()

# LAB   Convertendo o consumo de combustível
def liters_100km_to_miles_gallon(liters):
    liters_per_gallon = 3.78541  # 1 galão = 3.78541 litros
    miles_per_100km = 62.1371    # 1 km = 0.621371 milhas
    
    miles = miles_per_100km / (liters / liters_per_gallon)
    gallons = 100 / miles
    
    return round(gallons, 2)

def miles_gallon_to_liters_100km(miles):
    miles_per_gallon = 0.621371  # 1 milha = 0.621371 km
    liters_per_gallon = 3.78541  # 1 galão = 3.78541 litros
    
    kilometers = miles / miles_per_gallon
    liters = liters_per_gallon / (kilometers / 100)
    
    return round(liters, 2)
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# RESUMO DA SEÇÃO

# Você pode usar a palavra-chave return para informar uma função para retornar algum valor.

def multiply(a, b): 
    return a * b 
print(multiply(3, 4)) 
# saídas: 12 def multiply(a, b): return print(multiply(3, 4)) # saídas: None
print()

# O resultado de uma função pode ser facilmente atribuído a uma variável
def wishes(): 
    return "Feliz aniversário!" 
w = wishes()
print(w) # saídas: Feliz aniversário!
print()

# Veja a diferença de saída nos dois exemplos a seguir
# Exemplo 1
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
wishes()    # saídas: Meus desejos
 
 
# Exemplo 2
def wishes():
    print("Meus desejos")
    return "Feliz aniversário!"
 
print(wishes())
 
# saídas: Meus desejos
#          Feliz aniversário!
print()

# Você pode usar uma lista como argumento de função

def hi_everybody(my_list):
    translations = {
        "woda": "água"
    }
    for name in my_list:
        translated_name = translations.get(name, name)
        print("Oi,", translated_name)

hi_everybody(["Adão", "John", "Lucy"])
print()

# Uma lista também pode ser um resultado de função
def create_list(n): 
    my_list = [] 
    for i in range(n): my_list.append(i) 
    return my_list 
print(create_list(5))