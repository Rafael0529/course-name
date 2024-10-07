import os

# Obtener las variables de entorno definidas en el workflow
nombre = os.getenv('USERNAME', 'Usuario')
lenguaje = os.getenv('LANGUAGE', 'Python')

# Imprimir el saludo personalizado
print(f"Hola {nombre}, tu lenguaje favorito es {lenguaje}!")
