#include <Wire.h>

byte value = 127;
byte address = 0b1100000;
byte WRITE_DAC_REGISTER = 0x00;

void setup() {
  Wire.begin(); // join i2c bus
  Wire.beginTransmission(address);
  Wire.write(WRITE_DAC_REGISTER);
  Wire.write(value);
  Wire.endTransmission();
}

void loop() {
  
}
