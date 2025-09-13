# ===============================
# MÉTODOS MÁS USADOS DE str EN PYTHON
# ===============================

# 1. split()
# Divide una cadena en una lista usando un separador.
# Por defecto separa en los espacios en blanco, pero se le puede indicar otro.
texto = "juan,lorenzo,wilmar"
textoProcesado = texto.split(",")
print(textoProcesado[1])  # lorenzo

# 2. join()
# Une una lista de cadenas en una sola, usando como separador el string sobre el que se invoca.
nombres = ["juan", "lorenzo", "wilmar"]
resultado = "-".join(nombres)
print(resultado)  # juan-lorenzo-wilmar

# 3. strip()
# Elimina los espacios (u otros caracteres indicados) al inicio y al final de la cadena.
texto = "   hola mundo   "
print(texto.strip())  # "hola mundo"

# 4. lstrip() y rstrip()
# lstrip() elimina caracteres al inicio de la cadena.
# rstrip() elimina caracteres al final de la cadena.
texto = "---hola---"
print(texto.lstrip("-"))  # "hola---"
print(texto.rstrip("-"))  # "---hola"

# 5. replace()
# Reemplaza todas las apariciones de un substring por otro.
texto = "hola juan"
print(texto.replace("juan", "lorenzo"))  # hola lorenzo

# 6. find() y rfind()
# find() devuelve la posición de la primera aparición de un substring, o -1 si no existe.
# rfind() hace lo mismo, pero busca desde la derecha (última aparición).
texto = "programacion en python"
print(texto.find("python"))  # 16
print(texto.find("java"))    # -1

# 7. index() y rindex()
# Igual que find() y rfind(), pero generan un error ValueError si no encuentran el substring.
texto = "hola mundo"
print(texto.index("mundo"))  # 5
# print(texto.index("java"))  # ValueError si no existe

# 8. startswith() y endswith()
# startswith() verifica si la cadena comienza con un prefijo dado.
# endswith() verifica si la cadena termina con un sufijo dado.
texto = "python avanzado"
print(texto.startswith("py"))  # True
print(texto.endswith("do"))    # True

# 9. upper() y lower()
# upper() convierte toda la cadena a mayúsculas.
# lower() convierte toda la cadena a minúsculas.
texto = "Python"
print(texto.upper())  # PYTHON
print(texto.lower())  # python

# 10. capitalize() y title()
# capitalize() pone en mayúscula la primera letra y lo demás en minúscula.
# title() convierte a mayúscula la primera letra de cada palabra.
texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"
print(texto.title())       # "Hola Mundo"

# 11. casefold()
# Convierte tod.o el texto a minúsculas, pero de forma más agresiva que lower(),
# útil para comparaciones sin importar mayúsculas/minúsculas en distintos idiomas.
texto = "PYThOn"
print(texto.casefold())  # "python"

# 12. count()
# Devuelve cuántas veces aparece un substring en la cadena.
texto = "banana"
print(texto.count("a"))  # 3

# 13. isdigit(), isalpha(), isalnum()
# isdigit(): True si todos los caracteres son dígitos.
# isalpha(): True si todos los caracteres son letras.
# isalnum(): True si todos son letras o números (sin espacios ni símbolos).
print("123".isdigit())     # True
print("juan".isalpha())    # True
print("juan123".isalnum()) # True

# 14. isspace()
# Devuelve True si la cadena contiene solo espacios en blanco, tabs o saltos de línea.
print("   ".isspace())  # True

# 15. islower() y isupper()
# islower(): True si todos los caracteres alfabéticos están en minúscula.
# isupper(): True si todos los caracteres alfabéticos están en mayúscula.
print("hola".islower())  # True
print("HOLA".isupper())  # True

# 16. zfill()
# Rellena la cadena con ceros a la izquierda hasta alcanzar el tamaño indicado.
texto = "42"
print(texto.zfill(5))  # 00042

# 17. center(), ljust(), rjust()
# Ajustan el texto a un ancho específico, rellenando con un carácter indicado.
# center(): centra el texto. ljust(): alinea a la izquierda. rjust(): alinea a la derecha.
texto = "python"
print(texto.center(10, "-"))  # --python--
print(texto.ljust(10, "."))   # python....
print(texto.rjust(10, "."))   # ....python

# 18. splitlines()
# Divide una cadena en una lista por saltos de línea.
texto = "hola\nmundo\npython"
print(texto.splitlines())  # ['hola', 'mundo', 'python']

# 19. partition() y rpartition()
# partition() divide la cadena en 3 partes: antes, el separador y después de la primera aparición.
# rpartition() hace lo mismo pero tomando la última aparición del separador.
texto = "juan-lorenzo-wilmar"
print(texto.partition("-"))   # ('juan', '-', 'lorenzo-wilmar')
print(texto.rpartition("-"))  # ('juan-lorenzo', '-', 'wilmar')

# 20. format() y f-strings
# format() permite insertar variables dentro de una cadena usando llaves {}.
# f-strings (desde Python 3.6) permiten lo mismo de forma más legible y eficiente.
nombre = "Juan"
edad = 25
print("Mi nombre es {} y tengo {}".format(nombre, edad))
print(f"Mi nombre es {nombre} y tengo {edad}")
