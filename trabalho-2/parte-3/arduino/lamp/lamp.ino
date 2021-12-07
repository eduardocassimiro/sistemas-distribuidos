char serial;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  serial = Serial.read();
  if(serial == 'l'){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  if(serial == 'd'){
    digitalWrite(LED_BUILTIN, LOW);
  }
}
