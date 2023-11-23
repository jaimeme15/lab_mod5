# Abrir un archivo en modo de escritura
with open('numeros.txt', 'w') as archivo:
    # Escribir los números del 1 al 100,000 en el archivo
    for numero in range(1, 100001):
        archivo.write(str(numero) + '\n')

print("Archivo creado exitosamente.")
