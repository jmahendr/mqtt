import paho.mqtt.client as mqtt
import serial

#define callback method for CONNACK response from broker
def on_connect(client, userdata,rc):
    print("Connected to broker with rc " +str(rc))
    #now subscribe to topic
    client.subscribe("/com/jmahendr/h1/r1/#")

#define callback method when a publish message is received
def on_message(client, userdata, msg):
    print(msg.topic + " "  + str(msg.payload))
    #if (str(msg.payload) == 'on') :
    #    ser.write('on')
    #if(str(msg.payload) == 'off'):
    #    ser.write('off')
    ser.write(str(msg.payload))
    print(str(msg.payload))


ser = serial.Serial('/dev/ttyACM0', 9600)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.106", 1883, 60)
client.loop_forever()