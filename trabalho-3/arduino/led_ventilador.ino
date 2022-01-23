char serial;

int ventilador = 12;
int led = 8;

void setup() {
  pinMode(ventilador, OUTPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  serial = Serial.read();
  if(serial == 'a'){
    digitalWrite(ventilador, HIGH);
  }
  if(serial == 's'){
    digitalWrite(ventilador, LOW);
  }
  if(serial == 'n'){
    digitalWrite(led, HIGH);
  }
  if(serial == 'm'){
    digitalWrite(led, LOW);
  }
}
