#include <ESP8266WiFi.h>


const char* ssid = "Airtel_5757";
const char* password = "";

WiFiServer server(80);

// Left Motor pins
#define IN1 D1
#define IN2 D2

// Speed pins, combined ENA ENB in D3 
#define ENAB D3 

// Right Motor pins
#define IN3 D6
#define IN4 D5

// ultrasonic sensor pins
#define TRIG D0
#define ECHO D7

int speedVal = 50;
// String lastCommand = "S";
bool obstacleMode = false;



void setup() {
  Serial.begin(115200);

  // Putting IN1 IN4 High, and IN2 IN3 Low gives forward motion
  pinMode(IN1, OUTPUT); 
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(ENAB, OUTPUT);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("connected!");
  Serial.println((WiFi.localIP())); // local ip assigned by the router
  server.begin();

}

void loop() {

    float distance = getDistance();
    // Serial.println(distance);

    // Obstacle override
    if (distance > 0 && distance <13) {
      obstacleMode = true;

      stop();
      delay(100);

      // avoid obstacle
      left();
      delay(300);

      stop();
      delay(100);

      return; 
    }

    else{
      obstacleMode = false;
    }

    WiFiClient client = server.available();

    if(!client) return;

    String request = client.readStringUntil('\r');
    client.flush();

    if (request.indexOf("/F") != -1) forward();
    else if (request.indexOf("/B") != -1) backward();
    else if (request.indexOf("/L") != -1) left();
    else if (request.indexOf("/R") != -1) right();
    else if (request.indexOf("/S") != -1) stop();
    else if (request.indexOf("/+") != -1) speedVal += 25;
    else if (request.indexOf("/-") != -1) speedVal -= 25;

    speedVal = constrain(speedVal, 0, 1023);
    analogWrite(ENAB, speedVal);

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/plain");
    client.println("");
    client.println("OK");

    delay(1);

    Serial.println("connected!");
    Serial.println((WiFi.localIP()));


}

void forward(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void backward(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void left(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void right(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void stop(){
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);

}

float getDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duration = pulseIn(ECHO, HIGH);
  float distance = duration / 58.0;

  return distance;
}





















