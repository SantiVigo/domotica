"""Programa completo da fila 1 para a maqueta domótica.
Autores: Santiago Pereira Briceño
Data: 30/04/2025"""

#include <Servo.h>               // [1] Inclúe a libraría Servo para controlar o servomotor

Servo servoMotor;               // [2] Crea un obxecto Servo chamado 'servoMotor'

const int botonB = 8;           // [3] Define o pin 8 como o pin onde está conectado o botón
int angulo = 0;                 // [4] Variable que garda o ángulo actual do servo
bool estadoAnterior = HIGH;    // [5] Variable para detectar cambios de estado no botón

void setup() {
  servoMotor.attach(2);         // [6] Conecta o servo ao pin analóxico 2
  pinMode(botonB, INPUT_PULLUP); // [7] Configura o botón como entrada con resistencia interna
  servoMotor.write(0);          // [8] Establece o servo ao comezo en 0º
}

void loop() {
  bool estadoActual = digitalRead(botonB); // [9] Le o estado actual do botón

  // [10] Comproba se o botón foi premido (pasou de non premido a premido)
  if (estadoAnterior == HIGH && estadoActual == LOW) {
    
    angulo += 10;               // [11] Aumenta o ángulo en 10º

    if (angulo > 90) {          // [12] Se pasa de 90º, volve a 0º
      angulo = 0;
    }

    servoMotor.write(angulo);  // [13] Manda o novo ángulo ao servo
    delay(300);                // [14] Engade unha pausa para evitar lectura múltiple do mesmo toque
  }

  estadoAnterior = estadoActual; // [15] Actualiza o estado anterior para a próxima lectura
}
