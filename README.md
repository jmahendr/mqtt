# mqtt 
This projects is made of two parts i) Python client for Mosquitto broker and ii) arduino sketch for controlling relay board.

The python client will subscribe to a known topic, and construct a message to be sent to arduino via serial.

Arduino sketch will read serial data and swith its digital pins to HIGH or LOW, in turn controlling a realy.
