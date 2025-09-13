# -------- DICT --------
print("\n=== DICT ===")
persona = {"nombre": "Juan", "edad": 25}

# .get(clave): obtiene el valor de una clave, devuelve None si no existe.
print(persona.get("nombre"))     # Juan

# .keys(): devuelve un objeto con todas las claves del diccionario.
print(persona.keys())            # dict_keys(['nombre', 'edad'])

# .values(): devuelve un objeto con todos los valores.
print(persona.values())          # dict_values(['Juan', 25])

# .items(): devuelve pares (clave, valor) como tuplas.
print(persona.items())           # dict_items([('nombre', 'Juan'), ('edad', 25)])

# .update(): actualiza el diccionario con otro diccionario o pares clave=valor.
persona.update({"edad": 26})
print(persona)  # {'nombre': 'Juan', 'edad': 26}

# .pop(clave): elimina una clave y devuelve su valor.
persona.pop("edad")
print(persona)  # {'nombre': 'Juan'}

# .clear(): elimina todos los elementos del diccionario.
persona.clear()
print(persona)  # {}