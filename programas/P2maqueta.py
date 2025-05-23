"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira 
Data: 30/04/2025
"""

import time

# Simulación sencilla de hora actual (0-23)
hora = 20  # Cambia este valor para probar diferente momentos del día

while True:
    if 6 <= hora < 18:
        # Día - LED apagado
        led_blanco = False
        print("Es de día, LED blanco apagado.")
    else:
        # Noche - LED encendido
        led_blanco = True
        print("Es de noche, LED blanco encendido.")

    time.sleep(5)

    # Para simular cambio de hora (incrementar cada iteración)
    hora += 1
    if hora >= 24:
        hora = 0
