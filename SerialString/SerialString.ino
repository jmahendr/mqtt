/** Arduino client to control 12channel relayboard
    based on serial commands
   
   **/ 
   
int L1 = 2;
int L2 = 3;
int L3 = 4;

int F1 = 5;
int F2 = 6;

int WS1 = 7;
int WS2 = 8;

String msg = "";
String dev = "";
String cmd = "";

void setup() {
  Serial.begin(9600);
  for (int i = 2; i <=13; i++)
    pinMode(i, OUTPUT);
    
  for(int i = 2; i <=13; i++)
  {
    digitalWrite(i, HIGH);
    delay(250);
    digitalWrite(i,LOW);
  }  
}

void loop() {
  while(Serial.available()>0)
  {
    msg = Serial.readString();
    int dlim = msg.indexOf('|');
    dev = msg.substring(0, dlim);
    cmd = msg.substring(dlim+1);
    Serial.print(dev);
    Serial.print(" - ");
    Serial.println(cmd);
    
    if(dev == "L1") 
    {
      if(cmd == "on")
        digitalWrite(L1, HIGH);
      else
        digitalWrite(L1, LOW);
    }//end of L1
    
    if(dev == "L2") 
    {
      if(cmd == "on")
        digitalWrite(L2, HIGH);
      else
        digitalWrite(L2, LOW);
    }//end of L2
    if(dev == "L3") 
    {
      if(cmd == "on")
        digitalWrite(L3, HIGH);
      else
        digitalWrite(L3, LOW);
    }//end of L3
    
    
    if(dev == "F1") 
    {
      if(cmd == "on")
        digitalWrite(F1, HIGH);
      else
        digitalWrite(F1, LOW);
    }//end of F1
    if(dev == "F2") 
    {
      if(cmd == "on")
        digitalWrite(F2, HIGH);
      else
        digitalWrite(F2, LOW);
    }//end of F1
    
    
    if(dev == "WS1") 
    {
      if(cmd == "on")
        digitalWrite(WS1, HIGH);
      else
        digitalWrite(WS1, LOW);
    }//end of WS1
    if(dev == "WS2") 
    {
      if(cmd == "on")
        digitalWrite(WS2, HIGH);
      else
        digitalWrite(WS2, LOW);
    }//end of WS2
    
  }//end of while
}//end of loop
