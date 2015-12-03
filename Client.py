#https://eclipse.org/paho/clients/python/
## Source
## http://git.eclipse.org/c/paho/org.eclipse.paho.mqtt.python.git/
## 
## Download
## The Python client can be downloaded and installed from PyPI using the pip tool:
## 
## pip install paho-mqtt
## Building from source
## The project can be installed from the repository as well. To do this:
## 
## git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git
## cd org.eclipse.paho.mqtt.python.git
## python setup.py install
## The final step may need to be run with sudo if you are using Linux or similar system.
## 
## Documentation
## Full client documentation is available here.
## https://eclipse.org/paho/clients/python/docs/


import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("com/jmahendr/a")
    client.subscribe("com/jmahendr/b")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic == 'com/jmahendr/b'):client.publish("com/jmahendr/a", str(msg.payload), 0, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect("iot.eclipse.org", 1883, 60)
client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()