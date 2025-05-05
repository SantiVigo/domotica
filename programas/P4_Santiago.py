"""Programa completo.............."""
Autor: Santiago Pereira
Data: 5 de maio 

from microbit import *

pin2.set_analog_period(20)  # Configura a frecuencia do sinal PWM para o servo (20 ms = 50 Hz)

while True:
    if button_a.was_pressed():   # Detecta se se premeu o botón A
        pin2.write_analog(1)     # Valor analóxico moi baixo → xira o servo a 0º

    if button_b.was_pressed():   # Detecta se se premeu o botón B
        pin2.write_analog(180)   # Valor analóxico máis alto → xira o servo a 180º


buscar práctica do botón (en este caso botón B)

from microbit import *

pin2.set_analog_period(20)  # Configura o período PWM para controlar o servo

angulo = 0  # Comeza a 0º
pin2.write_analog(0)  # Servo en posición inicial 0º

while True:
    if button_b.was_pressed():  # Se se preme o botón B
        if angulo == 0:
            angulo = 90         # Se está a 0º, pasa a 90º
        else:
            angulo = 0          # Se está a 90º, volve a 0º
        
        # Conversión aproximada de graos a sinal PWM:
        # write_analog(0) → 0º, write_analog(90) → ~90º
        pin2.write_analog(angulo)
        sleep(500)  # Pequena pausa para evitar rebotes


