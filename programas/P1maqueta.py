"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time
from machine import Pin
import neopixel

# Configuración del pin del ventilador (relé)
ventilador_pin = Pin(2, Pin.OUT)  # Cambia por el pin correcto de tu placa
ventilador_pin.value(0)  # Ventilador apagado inicialmente

# Configuración del LED Neopixel
np_pin = Pin(4, Pin.OUT)  # Cambia por el pin correcto donde está el Neopixel
np = neopixel.NeoPixel(np_pin, 1)

# Simulamos la lectura de temperatura con un valor fijo que puedes modificar para probar
temperatura = 23.0  # Cambia este valor para probar distintas temperaturas

while True:
    # Actualizar estado según temperatura
    if temperatura > 24:
        # LED rojo
        np[0] = (255, 0, 0)
        np.write()
        # Activar ventilador
        ventilador_pin.value(1)
    else:
        # LED verde
        np[0] = (0, 255, 0)
        np.write()
        # Apagar ventilador
        ventilador_pin.value(0)

    # Mostrar estado para debug por consola
    print("Temperatura:", temperatura)
    if ventilador_pin.value() == 1:
        print("Ventilador activado, LED rojo")
    else:
        print("Ventilador apagado, LED verde")

    time.sleep(5)

    # Actualiza temperatura variable aquí para probar cambios o añádelo lectura real de sensor
    # temperatura = leer_sensor()

