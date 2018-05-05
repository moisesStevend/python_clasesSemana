#include <ESP8266WiFi.h>

#include "DHT.h"

#include <ESP8266HTTPClient.h>

WiFiClient client;

DHT dht2(2,DHT11);

String thingSpeakAddress= "http://api.thingspeak.com/update?";
String writeAPIKey;
String tsfield1Name;
String request_string;

HTTPClient http;

void setup()
{
  Serial.begin(115200);
  WiFi.disconnect();
  delay(3000);
  Serial.println("START");
   WiFi.begin("MOVISTAR_47DE","zFyQS7HLQJ7pRbY9Ujkg");
  while ((!(WiFi.status() == WL_CONNECTED))){
    delay(300);
    Serial.print("..");

  }
  Serial.println("Connected");
  Serial.println("Your IP is");
  Serial.println((WiFi.localIP().toString()));

}


void loop()
{

    if (client.connect("api.thingspeak.com",80)) {
      request_string = thingSpeakAddress;
      request_string += "key=";
      request_string += "G4Z0I22S89VM7QYD";
      request_string += "&";
      request_string += "field1";
      request_string += "=";
      request_string += String(dht2.readTemperature( ));
      request_string += "&";
      request_string += "field2";
      request_string += "=";
      request_string += String(dht2.readHumidity());
      http.begin(request_string);
      http.GET();
      http.end();
    }
    delay(16000);

}
