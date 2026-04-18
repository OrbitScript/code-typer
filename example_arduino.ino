// Example Arduino LED Blink Program
// Perfect for testing CODE-TYPER

const int LED_PIN = 13;
int delayTime = 1000;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Set LED pin as output
  pinMode(LED_PIN, OUTPUT);
  
  Serial.println("LED Blink Started!");
}

void loop() {
  // Turn LED on
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED ON");
  delay(delayTime);
  
  // Turn LED off
  digitalWrite(LED_PIN, LOW);
  Serial.println("LED OFF");
  delay(delayTime);
}
