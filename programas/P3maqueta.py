"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time

# --- Inicio del programa principal ---
print("El sistema está listo. Pulsa la tecla 'A' y Enter para activar el LED y el RINGTONE.")
print("Pulsa Ctrl+C en cualquier momento para salir.")

while True:
    # Simulamos la lectura del botón. En un sistema real, esto sería la lectura de un pin digital.
    accion_usuario = input("\nEsperando la pulsación del botón A... (Introduce 'A' y pulsa Enter): ").strip().upper()

    # Verificamos si el usuario "pulsó" el botón A
    if accion_usuario == 'A':
        print("Botón A pulsado. ¡Activando!")

        # Simula el encendido del LED
        print("LED: ENCENDIDO")

        # Simula la reproducción del sonido RINGTONE
        print("Sonido: RINGTONE reproduciéndose...")

        # Esperamos 5 segundos
        time.sleep(5)

        # Simula el apagado del LED
        print("LED: APAGADO")
        print("Sonido: RINGTONE terminado.")
        print("Proceso completado. Esperando una nueva pulsación del botón A.")

    else:
        print("Entrada no reconocida. Por favor, pulsa solo 'A'.")

    # Pequeña pausa antes de volver a pedir la entrada para evitar bucles muy rápidos
    time.sleep(0.5)

# --- Manejo de la salida del programa ---
    try:
        # Esto es un truco para que el bucle siga pidiendo entrada,
        # pero permite que Ctrl+C lo detenga limpiamente.
        pass
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break

# --- Fin del programa principal ---
print("¡Hasta pronto!")
