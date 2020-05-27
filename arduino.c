#include <ArduinoJson.h>
#include <Servo.h>
int koridorPin = 2;
int wcPin = 3;
int oda1Pin = 4;
int oda2Pin = 5;
int salonPin = 6;
int LDRPin1 = A0;
int LDRValue1 = 0;
int LDRPin2 = A1;
int LDRValue2 = 0;
int sicaklik = 0;
float analoggerilim = 0;
int sicaklikpin = A2;
unsigned long currentTime = 0; 
unsigned long sensorReadTime = 0;
Servo koridor_kapi;
Servo oda_1pencere;
Servo oda_2pencere;
Servo salon_pencere;

void setup() {
Serial.begin(9600);
Serial.setTimeout(30);
pinMode(koridorPin,OUTPUT);
pinMode(wcPin,OUTPUT);
pinMode(oda1Pin,OUTPUT);
pinMode(oda2Pin,OUTPUT);
pinMode(salonPin,OUTPUT);
koridor_kapi.attach(7);
oda_1pencere.attach(8);
oda_2pencere.attach(9);
salon_pencere.attach(10);

}

void loop() {
 // currentTime= millis();
  if(Serial.available() > 0){
          String newval = Serial.readString();
          sensorReading();
          StaticJsonBuffer<750> jsonBuffer;
          JsonObject& root = jsonBuffer.parseObject(newval);
          int pos = 0;
            String firstname  = root["firstname"];
            String lastname = root["lastname"];
            String switchval = root["switchval"];
            String switchtype = root["switchtype"];
            byte seekbarval = root["seekbarval"];
            String seekbartype = root["seekbartype"];
            String togglebuttontype = root["togglebuttontype"];
            boolean togglebuttonval = root["togglebuttonval"];

            if(switchval == "true"){
              if(switchtype == "switch1" && seekbartype == "Led1") analogWrite(koridorPin, seekbarval);
              if(switchtype == "switch2" && seekbartype == "Led2") analogWrite(wcPin, seekbarval);
              if(switchtype == "switch3" && seekbartype == "Led3") analogWrite(oda1Pin, seekbarval);
              if(switchtype == "switch4" && seekbartype == "Led4") analogWrite(oda2Pin, seekbarval);
              if(switchtype == "switch5" && seekbartype == "Led5") analogWrite(salonPin, seekbarval);
              }
            if(switchval == "false"){
              if(switchtype == "switch1")digitalWrite(koridorPin, LOW);
              if(switchtype == "switch2")digitalWrite(wcPin, LOW);
              if(switchtype == "switch3")digitalWrite(oda1Pin, LOW);
              if(switchtype == "switch4")digitalWrite(oda2Pin, LOW);
              if(switchtype == "switch5")digitalWrite(salonPin, LOW);
              }
             if(togglebuttonval == true){
              if(togglebuttontype == "toggleButton1"){
                koridor_kapi.write(40);delay(10); }
             if(togglebuttontype == "toggleButton2"){
                oda_1pencere.write(40);delay(10); }
             if(togglebuttontype == "toggleButton3"){
                oda_2pencere.write(40);delay(10); }
             if(togglebuttontype == "toggleButton4"){
                salon_pencere.write(40);delay(10); }
             }

             if(togglebuttonval == false){
              if(togglebuttontype == "toggleButton1"){
                 koridor_kapi.write(130);delay(10);}
              if(togglebuttontype == "toggleButton2"){
                 oda_1pencere.write(130);delay(10);}
              if(togglebuttontype == "toggleButton3"){
                 oda_2pencere.write(130);delay(10);}
              if(togglebuttontype == "toggleButton4"){
                 salon_pencere.write(130);delay(10);}
             }
        
    }
    //if(currentTime - sensorReadTime > 2000){
    //       sensorReadTime = currentTime;
    //       sensorReading();
    //     }

}
void sensorReading(){
      
            
           LDRValue1 = analogRead(LDRPin1);
           delay(10);
           LDRValue2 = analogRead(LDRPin2);
           delay(10);
           analoggerilim = analogRead(sicaklikpin);
           sicaklik = (analoggerilim/1023)*500;
           String jsonString = "{\"LDRValue1\":\"";
           jsonString += LDRValue1;
           jsonString += "\",\"LDRValue2\":\"";
           jsonString += LDRValue2;
           jsonString += "\",\"sicaklik\":\"";
           jsonString += sicaklik;
           jsonString += "\"}";
           Serial.print(jsonString);


}
