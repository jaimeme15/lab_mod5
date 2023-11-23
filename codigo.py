import time

# Iniciar el temporizador
start_time = time.time()

# Bucle del 1 al 100,000
for number in range(1, 100001):
    # Realizar alguna operación (en este caso, no se está haciendo nada)

# Calcular el tiempo transcurrido
elapsed_time = time.time() - start_time

# Imprimir el tiempo total transcurrido
print(f"Elapsed Time: {elapsed_time:.2f} seconds")
