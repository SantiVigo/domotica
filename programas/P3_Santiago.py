from microbit import *

completaMedio = Imagen("55555:55555:55555:55555:55555")

while True:
    if button_a.is_pressed():
       pin1.write_digital(1)
       display.show("A")
       sleep(2000)
       display.clear()
       todos =Image("55555,55555,55555,55555,55555")
       display.show(todos)
       sleep(2000)
       display.clear()
       
  if button_b.is_pressed():
     pin1.write_digital(0)
     display.show("B")
     sleep(2000)
     display.clear()
     esquinas =Image("90009,00000,00000,00000,90009")
     display.show(esquinas)
     sleep(2000)
     display.clear()
