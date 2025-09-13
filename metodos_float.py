print("=== FLOAT ===")
x = 3.14

# .is_integer(): devuelve True si el valor es un número entero (ejemplo: 3.0)
print(x.is_integer())        # False
print((3.0).is_integer())    # True

# .hex(): devuelve la representación hexadecimal del número flotante.
print(x.hex())               # '0x1.91eb851eb851fp+1'

# .as_integer_ratio(): devuelve una tupla (numerador, denominador)
# que representa exactamente al número flotante como fracción.
print(x.as_integer_ratio())  # (7070651414971679, 2251799813685248)