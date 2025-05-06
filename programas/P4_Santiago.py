"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira Briceño
Data: 30/04/2025"""

from microbit import *
import neopixel

# Definir o número de LEDs e o pin ao que están conectados
num_leds = 5  # Número de LEDs
pin = pin0  # Pin ao que están conectados os LEDs

# Crear o obxecto NeoPixel
leds = neopixel.NeoPixel(pin, num_leds)

# Función para cambiar a cor dos LEDs
def change_color(red, green, blue):
    for i in range(num_leds):
        leds[i] = (red, green, blue)
    leds.show()

# Bucle principal
while True:
    # Cor azul
    for value in range(0, 256, 5):  # Aumentar de 5 en 5 ata 255
        change_color(0, 0, value)  # Cor azul
        sleep(50)  # Esperar 50 milisegundos
    
    # Cor vermella
    for value in range(0, 256, 5):  # Aumentar de 5 en 5 ata 255
        change_color(value, 0, 0)  # Cor vermella
        sleep(50)  # Esperar 50 milisegundos
    
    # Cor verde
    for value in range(0, 256, 5):  # Aumentar de 5 en 5 ata 255
        change_color(0, value, 0)  # Cor verde
        sleep(50)  # Esperar 50 milisegundos
