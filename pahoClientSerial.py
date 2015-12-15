#
#  python client for mosquitto
#  Connects to broker and subscribes to topic
#  Communicates to arduino with pyserial 
#  Arduino command is constructed with topic & payload of message from broker
#  Arduino typically connects as /dev/ttyACM0
#    may need exploration on how to identify arduino device dynamically.
#


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
    logging.debug('serial cmd: ' + serialData)
    ser.write(serialData)


logging.basicConfig(filename='/home/pi/projects/mqtt/log/ffWallClient.log', filemode='w', level=logging.DEBUG, 
format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('Attempting to open serial port with arduino')
ser = serial.Serial('/dev/ttyACM0', 9600)
logging.info('Serial port Open? ' + str(ser.isOpen()))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.106", 1883, 60)
client.loop_forever()
