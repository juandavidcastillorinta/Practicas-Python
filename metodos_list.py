print("\n=== LIST ===")
numeros = [1, 2, 3]

# .append(): agrega un elemento al final de la lista.
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]

# .extend(): agrega todos los elementos de un iterable (lista, tupla, etc.)
numeros.extend([5, 6])
print(numeros)  # [1, 2, 3, 4, 5, 6]

# .insert(pos, elem): inserta un elemento en una posición específica.
numeros.insert(0, 0)
print(numeros)  # [0, 1, 2, 3, 4, 5, 6]

# .pop(): elimina y devuelve el último elemento (o el índice especificado).
numeros.pop()
print(numeros)  # [0, 1, 2, 3, 4, 5]

# .remove(elem): elimina la primera aparición de un valor específico.
numeros.remove(3)
print(numeros)  # [0, 1, 2, 4, 5]

# .sort(): ordena la lista en orden ascendente (puede recibir key y reverse).
numeros.sort()
print(numeros)  # [0, 1, 2, 4, 5]

# .reverse(): invierte el orden de la lista.
numeros.reverse()
print(numeros)  # [5, 4, 2, 1, 0]