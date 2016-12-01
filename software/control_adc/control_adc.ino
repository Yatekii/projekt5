#include <Wire.h>

const byte I2C_ADDRESS = 0b1100000;
const byte WRITE_DAC_REGISTER = 0x00;
const byte WRITE_MEMORY = 0x40;
const byte BUFFERED_VREF = 0x18;
const byte UNBUFFERED_VREF = 0x10;
const byte GAIN_PIN = 0;
const byte HILO_PIN = 22;

void setPin(byte pin, byte level){
  digitalWrite(pin, level);
}

void sendI2C(byte value){
  Wire.beginTransmission(I2C_ADDRESS);
  Wire.write(WRITE_MEMORY | UNBUFFERED_VREF);
  //Wire.write(WRITE_DAC_REGISTER);
  Wire.write(value);
  Wire.write(0x00); // This byte is just padding
  Wire.endTransmission();  
}

void readGAIN(){
  int val = analogRead(GAIN_PIN);
  Serial.print("DAC has ");
  Serial.print((float)(val * 3.3) / (1 << 10));
  Serial.print("V.\n");
}

void setHILO(byte level){
  setPin(HILO_PIN, level);
}

void setup() {
  Serial.begin(9600);
  Serial.println(WRITE_MEMORY | UNBUFFERED_VREF, BIN);
  Wire.begin();
  pinMode(HILO_PIN, OUTPUT);

  // Set DAC Voltage
  sendI2C(127);
  setHILO(LOW);
  readGAIN();
}

void loop() {
  
}
