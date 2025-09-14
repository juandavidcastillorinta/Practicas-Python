# ================================================
# OPERACIONES MÁS USADAS EN PYTHON
# ================================================

# -------------------------
# 1. OPERACIONES ARITMÉTICAS BÁSICAS
# -------------------------

# Suma
a = 10 + 5  # 15

# Resta
b = 10 - 3  # 7

# Multiplicación
c = 4 * 3   # 12

# División (siempre devuelve float)
d = 10 / 3  # 3.333...

# División entera (descarta los decimales)
e = 10 // 3  # 3

# Módulo (residuo de la división)
f = 10 % 3   # 1

# Potencia
g = 2 ** 3   # 8


# -------------------------
# 2. OPERACIONES RELACIONALES (COMPARACIONES)
# -------------------------

# Igualdad
x = (5 == 5)  # True

# Desigualdad
y = (5 != 3)  # True

# Mayor que
z = (7 > 3)   # True

# Menor que
k = (2 < 8)   # True

# Mayor o igual
m = (5 >= 5)  # True

# Menor o igual
n = (3 <= 7)  # True


# -------------------------
# 3. OPERACIONES LÓGICAS
# -------------------------

# AND (True solo si ambos son True)
resultado_and = True and False  # False

# OR (True si al menos uno es True)
resultado_or = True or False  # True

# NOT (invierte el valor lógico)
resultado_not = not True  # False


# -------------------------
# 4. OPERADORES DE ASIGNACIÓN COMPUESTA
# -------------------------
num = 10

num += 5  # num = num + 5 -> 15
num -= 3  # num = num - 3 -> 12
num *= 2  # num = num * 2 -> 24
num /= 4  # num = num / 4 -> 6.0
num //= 2 # num = num // 2 -> 3.0
num %= 2  # num = num % 2 -> 1.0
num **= 3 # num = num ** 3 -> 1.0


# -------------------------
# 5. OPERACIONES DE CADENAS
# -------------------------

texto = "Python"

# Concatenación
concatenado = texto + " es genial"  # "Python es genial"

# Repetición
repetido = texto * 3  # "PythonPythonPython"

# Pertenencia (in)
tiene_py = "Py" in texto  # True
no_tiene_java = "Java" not in texto  # True


# -------------------------
# 6. OPERACIONES CON LISTAS
# -------------------------

lista = [1, 2, 3, 4]

# Indexación
primero = lista[0]  # 1

# Slicing (sublista)
sublista = lista[1:3]  # [2, 3]

# Concatenación de listas
lista2 = lista + [5, 6]  # [1,2,3,4,5,6]

# Repetición
lista3 = [0] * 5  # [0,0,0,0,0]

# Pertenencia
existe = 3 in lista  # True

# Longitud
longitud = len(lista)  # 4


# -------------------------
# 7. OPERACIONES CON CONJUNTOS
# -------------------------

A = {1, 2, 3}
B = {3, 4, 5}

# Unión
union = A | B  # {1,2,3,4,5}

# Intersección
interseccion = A & B  # {3}

# Diferencia
diferencia = A - B  # {1,2}

# Diferencia simétrica
dif_sim = A ^ B  # {1,2,4,5}


# -------------------------
# 8. OPERACIONES CON DICCIONARIOS
# -------------------------

dic = {"a": 1, "b": 2, "c": 3}

# Acceso
valor_a = dic["a"]  # 1

# Obtener valor con get (evita error si no existe la clave)
valor_x = dic.get("x", "No existe")  # "No existe"

# Verificar clave
existe_b = "b" in dic  # True

# Obtener solo claves
claves = dic.keys()  # dict_keys(['a','b','c'])

# Obtener solo valores
valores = dic.values()  # dict_values([1,2,3])

# Obtener pares (clave, valor)
items = dic.items()  # dict_items([("a",1),("b",2),("c",3)])


# -------------------------
# 9. OPERACIONES BIT A BIT (AVANZADAS)
# -------------------------

# NOTA: Se usan a nivel binario.
p = 6   # binario 110
q = 3   # binario 011

# AND bit a bit
bit_and = p & q  # 110 & 011 = 010 (2)

# OR bit a bit
bit_or = p | q   # 110 | 011 = 111 (7)

# XOR bit a bit
bit_xor = p ^ q  # 110 ^ 011 = 101 (5)

# Desplazamiento a la izquierda (multiplica por potencias de 2)
shift_left = p << 1  # 110 << 1 = 1100 (12)

# Desplazamiento a la derecha (divide por potencias de 2)
shift_right = p >> 1 # 110 >> 1 = 11 (3)


# -------------------------
# 10. OPERACIONES ESPECIALES
# -------------------------

# Comparación de identidad (evalúa si apuntan al mismo objeto en memoria)
lista_a = [1, 2, 3]
lista_b = lista_a
identidad = lista_a is lista_b  # True

# Comparación de no identidad
diferente = lista_a is not [1, 2, 3]  # True, porque aunque sean iguales en valor no son el mismo objeto