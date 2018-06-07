#include <DHT.h>

#define DHTTYPE DHT11
#define DHTPIN 7

DHT dht(DHTPIN, DHTTYPE);


void setup(){

  Serial.begin(115200);
  pinMode(13, OUTPUT);
  digitalWrite(13, 1);
  
}



String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}


float lastTemp;
float lastHumi;
void loop(){
  
  
  
  float tempera = dht.readTemperature();
  float humi = dht.readHumidity();
  int lumi = analogRead(A0)/10;
  float volt = analogRead(A1)*(5.0 / 1023.0);
  
  
  
  if(tempera != -999.00 && humi != -999.00){
    lastTemp = tempera;
    lastHumi = humi;
    Serial.print("SENSORS|");
    Serial.print(tempera);
    Serial.print("|");
    Serial.print(humi);
    Serial.print("|");
    Serial.print(lumi);
    Serial.print("|");
    Serial.print(volt);
    Serial.println("|");
  }else{
  
  
    Serial.print("SENSORS|");
    Serial.print(lastTemp);
    Serial.print("|");
    Serial.print(lastHumi);
    Serial.print("|");
    Serial.print(lumi);
    Serial.print("|");
    Serial.print(volt);
    Serial.println("|");
  }
  delay(100);
}





