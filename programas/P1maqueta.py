"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time

# Este bucle infinito simula el funcionamiento continuo del sistema
while True:
    try:
        # Simulamos la lectura de la temperatura.
        # En un sistema real, aquí leerías un sensor de temperatura (ej. DHT11/22).
        temperatura_str = input("Introduce la temperatura actual en grados Celsius: ")
        temperatura = float(temperatura_str)

        print(f"\nTemperatura actual: {temperatura}°C")

        # Condición para temperatura alta (superior a 24º)
        if temperatura > 24:
            print("Temperatura superior a 24°C.")
            print("LED Neopixel: ROJO")
            print("Ventilador: ENCENDIDO (Relé ACTIVADO)")
            # Aquí iría el código real para:
            # 1. Configurar los Neopixel en rojo.
            # 2. Activar el relé para encender el ventilador.
        # Condición para temperatura baja (24º o inferior)
        else:
            print("Temperatura 24°C o inferior.")
            print("LED Neopixel: VERDE")
            print("Ventilador: APAGADO (Relé DESACTIVADO)")
            # Aquí iría el código real para:
            # 1. Configurar los Neopixel en verde.
            # 2. Desactivar el relé para apagar el ventilador.

        print("-" * 30) # Separador para mejor legibilidad
        time.sleep(2)  # Pequeña pausa antes de la siguiente lectura simulada

    except ValueError:
        print("Entrada inválida. Por favor, introduce un número para la temperatura.")
        print("-" * 30)
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break # Sale del bucle infinito si el usuario presiona Ctrl+C
