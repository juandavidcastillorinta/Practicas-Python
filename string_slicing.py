# string_slicing.py
# Este script demuestra el uso avanzado de slicing (rebanado) en cadenas de texto (strings) en Python.
# El slicing permite extraer subcadenas de una cadena utilizando la notación [inicio:fin:paso].
# A continuación, se explican los conceptos clave y se proporcionan ejemplos prácticos con comentarios detallados.

# Definimos una cadena de ejemplo para trabajar con slicing
texto = "¡Python es increíble!"

# 1. Slicing básico: Extraer una subcadena usando [inicio:fin]
# - 'inicio': Índice donde comienza el slice (incluido).
# - 'fin': Índice donde termina el slice (excluido).
# - Si no se especifica 'inicio', se asume 0. Si no se especifica 'fin', se asume len(texto).
print("Slicing básico:")
subcadena = texto[0:6]  # Extrae desde el índice 0 hasta el 5 (excluye el 6)
print(f"texto[0:6] -> '{subcadena}'")  # Imprime: ¡Pytho

# 2. Omitiendo índices: Usar valores predeterminados
# - Si omitimos 'inicio', comienza desde el principio.
# - Si omitimos 'fin', va hasta el final.
print("\nOmitiendo índices:")
inicio_omitido = texto[:6]  # Equivalente a texto[0:6]
fin_omitido = texto[7:]   # Desde el índice 7 hasta el final
print(f"texto[:6] -> '{inicio_omitido}'")  # Imprime: ¡Pytho
print(f"texto[7:] -> '{fin_omitido}'")     # Imprime: es increíble!

# 3. Slicing con paso: [inicio:fin:paso]
# - 'paso': Indica el incremento entre índices. Puede ser positivo o negativo.
print("\nSlicing con paso:")
cada_dos = texto[::2]  # Toma cada segundo carácter desde el inicio hasta el final
print(f"texto[::2] -> '{cada_dos}'")  # Imprime: ¡yoesicrdbe

# 4. Slicing con índices negativos
# - Los índices negativos cuentan desde el final de la cadena (-1 es el último carácter).
print("\nSlicing con índices negativos:")
ultimos_cinco = texto[-5:]  # Extrae los últimos 5 caracteres
print(f"texto[-5:] -> '{ultimos_cinco}'")  # Imprime: ible!

# 5. Slicing con paso negativo: Invertir una cadena
# - Un paso negativo recorre la cadena en orden inverso.
print("\nSlicing con paso negativo:")
invertida = texto[::-1]  # Invierte toda la cadena
print(f"texto[::-1] -> '{invertida}'")  # Imprime: !elbidércni se nohtyP¡

# 6. Slicing con límites fuera de rango
# - Python maneja índices fuera de rango de forma segura, ajustándolos al inicio o fin.
print("\nSlicing con índices fuera de rango:")
fuera_rango = texto[10:100]  # Intenta extraer desde el índice 10 hasta uno inexistente
print(f"texto[10:100] -> '{fuera_rango}'")  # Imprime: increíble!

# 7. Slicing con cadenas vacías o de longitud cero
# - Si el rango es inválido (inicio >= fin con paso positivo), se obtiene una cadena vacía.
print("\nSlicing con rango inválido:")
vacia = texto[10:10]  # Inicio y fin son iguales
print(f"texto[10:10] -> '{vacia}'")  # Imprime: ''

# 8. Ejemplo práctico: Extraer palabras específicas
# - Supongamos que queremos extraer la palabra "es" de la cadena.
print("\nEjemplo práctico: Extraer palabra 'es':")
palabra_es = texto[7:9]  # Sabemos que "es" está entre los índices 7 y 9
print(f"texto[7:9] -> '{palabra_es}'")  # Imprime: es

# 9. Modificando subcadenas (no directamente, ya que los strings son inmutables)
# - Los strings en Python son inmutables, pero podemos crear una nueva cadena combinando slices.
print("\nModificando una cadena con slicing:")
nueva_cadena = texto[:7] + "fue" + texto[9:]  # Reemplaza "es" por "fue"
print(f"texto[:7] + 'fue' + texto[9:] -> '{nueva_cadena}'")  # Imprime: ¡Python fue increíble!

# 10. Consideraciones avanzadas: Slicing en cadenas Unicode
# - Las cadenas en Python son Unicode, y el slicing respeta los puntos de código.
print("\nSlicing con caracteres Unicode:")
texto_unicode = "こんにちは"  # Hola en japonés
parte_unicode = texto_unicode[0:3]  # Extrae los primeros 3 caracteres
print(f"texto_unicode[0:3] -> '{parte_unicode}'")  # Imprime: こんに

# Nota final:
# - El slicing es una herramienta poderosa y flexible para manipular cadenas.
# - Es importante entender los índices, el paso y cómo Python maneja casos extremos.
# - Practica con diferentes combinaciones de inicio, fin y paso para dominar esta técnica.