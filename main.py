import network
import time
from umqtt.simple import MQTTClient

# WiFi credentials
SSID = "YOUR_SSID"
PASSWORD = "YOUR_PASSWORD"

# MQTT server details (VPS)
MQTT_BROKER = "YOUR_CLOUD_VPS_IP"
MQTT_PORT = 1883
MQTT_TOPIC_SUBSCRIBE = "esp32/control"
MQTT_TOPIC_PUBLISH = "esp32/sensor"

# Initialize WiFi connection
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("WiFi connected with IP:", wlan.ifconfig()[0])

# Callback when a message is received from the server
def on_message(topic, msg):
    print(f"Received message: {msg} on topic: {topic}")
    if msg == b'Turn LED ON':
        # Control the LED here (example)
        print("Turning LED ON")
    elif msg == b'Turn LED OFF':
        print("Turning LED OFF")

# Initialize and connect to the MQTT broker
def connect_mqtt():
    client = MQTTClient("esp32_client", MQTT_BROKER, port=MQTT_PORT)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)
    print("Connected to MQTT broker and subscribed to topic")
    return client

# Main function
def main():
    connect_wifi()
    mqtt_client = connect_mqtt()

    # Publish sensor data to the server
    while True:
        sensor_data = "OFF"  # Replace with actual sensor data or state
        mqtt_client.publish(MQTT_TOPIC_PUBLISH, sensor_data)
        print(f"Published sensor data: {sensor_data}")

        # Check for messages from the server
        mqtt_client.check_msg()
        time.sleep(5)  # Publish every 5 seconds

# Start the main function
main()
