print("\n=== SET ===")
a = {1, 2, 3}
b = {3, 4, 5}

# .add(elem): agrega un elemento al conjunto.
a.add(6)
print(a)  # {1, 2, 3, 6}

# .remove(elem): elimina un elemento. Error si no existe.
a.remove(2)
print(a)  # {1, 3, 6}

# .discard(elem): elimina un elemento. NO da error si no existe.
a.discard(10)
print(a)  # {1, 3, 6}

# .union(): devuelve un conjunto con todos los elementos de ambos.
print(a.union(b))  # {1, 3, 4, 5, 6}

# .intersection(): devuelve elementos comunes entre conjuntos.
print(a.intersection(b))  # {3}

# .difference(): devuelve los elementos que están en A pero no en B.
print(a.difference(b))  # {1, 6}

# .issubset(): verifica si A es subconjunto de otro.
print(a.issubset({1, 3, 6}))  # True

# .issuperset(): verifica si A contiene todos los elementos de otro conjunto.
print(a.issuperset({1, 3}))  # True