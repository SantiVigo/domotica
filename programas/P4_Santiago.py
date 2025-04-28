from microbit import *

pin6.set_analog_period(20)   #servo conectado ao pin6
while True:
    pin6.write_analog(180)     #o servo xira a 180º ao enviar un valor analóxico de 180
    sleep(1000) #esperamos 1s
    pin6.write_analog(1)
    sleep(1000)
