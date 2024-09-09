import paho.mqtt.client as mqtt

# MQTT server details
MQTT_BROKER = "YOUR_CLOUD_VPS_IP"  # Use the VPS IP or domain name
MQTT_PORT = 1883
MQTT_TOPIC_SUBSCRIBE = "esp32/sensor"
MQTT_TOPIC_PUBLISH = "esp32/control"

# Callback when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to the broker")
        # Subscribe to the topic once connected
        client.subscribe(MQTT_TOPIC_SUBSCRIBE)
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is received from the ESP32 (MicroPython)
def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")
    # Process the message here
    if msg.topic == MQTT_TOPIC_SUBSCRIBE:
        print("Sensor data received from ESP32:", msg.payload.decode())
        # You can control the ESP32 by publishing back to it
        # Example: turning an LED on/off
        if msg.payload.decode() == "ON":
            client.publish(MQTT_TOPIC_PUBLISH, "Turn LED ON")
        elif msg.payload.decode() == "OFF":
            client.publish(MQTT_TOPIC_PUBLISH, "Turn LED OFF")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Start the loop to process callbacks and handle reconnections
client.loop_forever()
