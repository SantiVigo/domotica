"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

# Importar módulos necesarios para micro:bit (simulados)
# from microbit import display, Image, sleep # En un entorno real de micro:bit
# import neopixel # En un entorno real para Neopixel
# import music # En un entorno real para música
# import pin # En un entorno real para leer el PIR y controlar LEDs

print("Iniciando programa de seguridad para micro:bit...")
print("Simulación: introduce 'presencia' si el PIR detecta algo, o 'nada' si no.")

# Configuración inicial (simulada)
# NEOPixel_PIN = pin.P0 # Pin para Neopixels
# NEOPixel_COUNT = 8 # Número de Neopixels
# np = neopixel.NeoPixel(NEOPixel_PIN, NEOPixel_COUNT) # Objeto Neopixel real
# WHITE_LED_PIN = pin.P1 # Pin para LED blanco
# PIR_SENSOR_PIN = pin.P2 # Pin para el sensor PIR

# Bucle principal del programa
while True:
    # Simulación de la lectura del sensor PIR
    # En una micro:bit real, sería algo como 'pir_value = PIR_SENSOR_PIN.read_digital()'
    deteccion_pir_str = input("\n¿El sensor PIR detecta presencia? (escribe 'presencia' o 'nada'): ").strip().lower()

    if deteccion_pir_str == "presencia":
        print("\n¡PRESENCIA DETECTADA!")

        # 1. Micro:bit emite el sonido "Ringtone" dos veces
        print("Sonido: 'Ringtone' sonando (1/2)")
        # music.play(music.RINGTONE) # Código real
        time.sleep(1) # Simulación de la duración del sonido
        print("Sonido: 'Ringtone' sonando (2/2)")
        # music.play(music.RINGTONE) # Código real
        time.sleep(1) # Simulación

        # 2. LEDs Neopixel parpadean en rojo cinco veces, en períodos de 500 ms
        for i in range(5):
            print(f"Neopixel: ROJO (parpadeo {i+1}/5)")
            # np.fill((255, 0, 0)) # Neopixel real a rojo
            # np.show() # Actualizar Neopixel real
            time.sleep(0.5) # Espera 500 ms (0.5 segundos)

            print("Neopixel: APAGADO")
            # np.fill((0, 0, 0)) # Neopixel real a apagado
            # np.show() # Actualizar Neopixel real
            time.sleep(0.5) # Espera 500 ms

        # 3. El LED blanco parpadea también 5 veces en períodos de 500 ms
        for i in range(5):
            print(f"LED Blanco: ENCENDIDO (parpadeo {i+1}/5)")
            # WHITE_LED_PIN.write_digital(1) # LED blanco real a encendido
            time.sleep(0.5) # Espera 500 ms

            print("LED Blanco: APAGADO")
            # WHITE_LED_PIN.write_digital(0) # LED blanco real a apagado
            time.sleep(0.5) # Espera 500 ms

        # 4. En la matriz aparece la cara enfadada durante 5 veces en períodos de 500 ms
        for i in range(5):
            print(f"Matriz de LEDs: CARA ENFADADA (parpadeo {i+1}/5)")
            # display.show(Image.ANGRY) # Matriz real
            time.sleep(0.5) # Espera 500 ms

            print("Matriz de LEDs: APAGADA")
            # display.clear() # Matriz real
            time.sleep(0.5) # Espera 500 ms

        print("\nSecuencia de alerta terminada.")

    elif deteccion_pir_str == "nada":
        print("\nSensor PIR: Sin presencia.")
        print("Matriz de LEDs: MOSTRANDO CASA")
        # display.show(Image.HOUSE) # Código real para la matriz de LEDs
        # np.fill((0, 0, 0)) # Asegurarse que Neopixel estén apagados
        # np.show()
        # WHITE_LED_PIN.write_digital(0) # Asegurarse que LED blanco esté apagado
        time.sleep(1) # Espera un poco antes de la siguiente comprobación

    else:
        print("Entrada no válida. Por favor, escribe 'presencia' o 'nada'.")

    # Pequeña pausa para evitar que el bucle se ejecute demasiado rápido
    time.sleep(0.5)

    # Permite salir del bucle si el usuario presiona Ctrl+C
    try:
        pass
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break
