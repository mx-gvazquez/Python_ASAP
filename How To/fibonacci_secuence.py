"""
Explotando la manera de apuntar a los objetos de una Lista.

Creamos el arreglo Fibonacci con los primeros 2 términos.

Usamos los punteros [-1] y [-2] para sumar el último y penúltimo valores

y con ellos creamos un nuevo valor, que añadimos al FINAL de la LISTA

con el comando '.append' que hace justamente eso.
"""

num_terms = 10
fibonacci = [0, 1]

while len(fibonacci) < num_terms:
    next_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_term)

print(fibonacci)