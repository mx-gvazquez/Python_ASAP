# Usamos la propiedad 'slicing' de TRES parámetros

txt = "Hello World"[::-1]
print(txt)


print("---------")

# Ejemplo, con función parametrizada

name = "German"

def reverse_name(word):
    print(word[::-1])

reverse_name(name)