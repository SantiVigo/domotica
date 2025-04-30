#include <Servo.h>

Servo miServo;
const int pinServo = 2;      // Pin do servo
const int pinBoton = 8;      // Pin do botón B
int estadoServo = 0;         // 0° ou 90°
bool ultimoEstadoBoton = false;

void setup() {
  miServo.attach(pinServo);
  pinMode(pinBoton, INPUT);
  miServo.write(0);          // Comeza en 0°
}

void loop() {
  bool estadoBoton = digitalRead(pinBoton);

  // Detecta o cambio de estado do botón
  if (estadoBoton && !ultimoEstadoBoton) {
    // Cambia á posición oposta
    if (estadoServo == 0) {
      miServo.write(90);
      estadoServo = 90;
    } else {
      miServo.write(0);
      estadoServo = 0;
    }
    delay(300); // Anti-rebote e evita repeticións
  }

  ultimoEstadoBoton = estadoBoton;
}
