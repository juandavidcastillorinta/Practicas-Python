# ===============================
# MÉTODOS MÁS USADOS DE str EN PYTHON
# ===============================

# 1. split()
texto = "juan,lorenzo,wilmar"
textoProcesado = texto.split(",")
print(textoProcesado[1])  # lorenzo

# 2. join()
nombres = ["juan", "lorenzo", "wilmar"]
resultado = "-".join(nombres)
print(resultado)  # juan-lorenzo-wilmar

# 3. strip()
texto = "   hola mundo   "
print(texto.strip())  # "hola mundo"

# 4. lstrip() y rstrip()
texto = "---hola---"
print(texto.lstrip("-"))  # "hola---"
print(texto.rstrip("-"))  # "---hola"

# 5. replace()
texto = "hola juan"
print(texto.replace("juan", "lorenzo"))  # hola lorenzo

# 6. find() y rfind()
texto = "programacion en python"
print(texto.find("python"))  # 16
print(texto.find("java"))    # -1

# 7. index() y rindex()
texto = "hola mundo"
print(texto.index("mundo"))  # 5
# print(texto.index("java"))  # ValueError si no existe

# 8. startswith() y endswith()
texto = "python avanzado"
print(texto.startswith("py"))  # True
print(texto.endswith("do"))    # True

# 9. upper() y lower()
texto = "Python"
print(texto.upper())  # PYTHON
print(texto.lower())  # python

# 10. capitalize() y title()
texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"
print(texto.title())       # "Hola Mundo"

# 11. casefold()
texto = "PYThOn"
print(texto.casefold())  # "python"

# 12. count()
texto = "banana"
print(texto.count("a"))  # 3

# 13. isdigit(), isalpha(), isalnum()
print("123".isdigit())     # True
print("juan".isalpha())    # True
print("juan123".isalnum()) # True

# 14. isspace()
print("   ".isspace())  # True

# 15. islower() y isupper()
print("hola".islower())  # True
print("HOLA".isupper())  # True

# 16. zfill()
texto = "42"
print(texto.zfill(5))  # 00042

# 17. center(), ljust(), rjust()
texto = "python"
print(texto.center(10, "-"))  # --python--
print(texto.ljust(10, "."))   # python....
print(texto.rjust(10, "."))   # ....python

# 18. splitlines()
texto = "hola\nmundo\npython"
print(texto.splitlines())  # ['hola', 'mundo', 'python']

# 19. partition() y rpartition()
texto = "juan-lorenzo-wilmar"
print(texto.partition("-"))   # ('juan', '-', 'lorenzo-wilmar')
print(texto.rpartition("-"))  # ('juan-lorenzo', '-', 'wilmar')

# 20. format() y f-strings
nombre = "Juan"
edad = 25
print("Mi nombre es {} y tengo {}".format(nombre, edad))
print(f"Mi nombre es {nombre} y tengo {edad}")
