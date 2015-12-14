#
#  python client for mosquitto
#  connects to broker and subscribes to topic
#  communicates to arduino with serial py 
#  arduino command is constructed with topic & payload of message from broker


import paho.mqtt.client as mqtt
import serial
import logging


#define callback method for CONNACK response from broker
def on_connect(client, userdata,rc):
    logging.info('Connected to broker with rc ' +str(rc))
    #now subscribe to topic
    client.subscribe("/com/jmahendr/h1/ff/#")

#define callback method when a publish message is received
def on_message(client, userdata, msg):
    logging.info('msg recvd: ' + msg.topic + " "  + str(msg.payload))
    topic = str(msg.topic)
    serialData = topic[topic.rindex('/')+1:] + "|" + str(msg.payload)
    logging.debug(serialData)
    ser.write(serialData)


logging.basicConfig(filename='/home/pi/projects/mqtt/log/ffWallClient.log', filemode='w', level=logging.DEBUG, 
format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info('Attempting to open serial port with arduino')
ser = serial.Serial('/dev/ttyACM0', 9600)
logging.info('Serial port opeing status ' + str(ser.isOpen()))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.106", 1883, 60)
client.loop_forever()
