"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira Briceño
Data: 30/04/2025
"""

from microbit import *
import neopixel  # Libraría para controlar LEDs Neopixel

led_np = neopixel.NeoPixel(pin9, 1)  # 1 LED conectado ao pin 9

# Función para aumentar progresivamente a intensidade dunha cor
def subir_cor(r, g, b):
    for valor in range(0, 256, 5):  # Desde 0 ata 255, de 5 en 5
        led_np[0] = (r(valor), g(valor), b(valor))  # Establece a cor actual
        led_np.show()  # Actualiza o LED
        sleep(50)  # Agarda 50 ms entre cambios

# Aumenta azul
subir_cor(lambda v: 0, lambda v: 0, lambda v: v)

# Aumenta vermello
subir_cor(lambda v: v, lambda v: 0, lambda v: 0)

# Aumenta verde
subir_cor(lambda v: 0, lambda v: v, lambda v: 0)

# Volve a azul
subir_cor(lambda v: 0, lambda v: 0, lambda v: v)
