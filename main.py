from MqttClient import MqttClient

client = MqttClient()

client.pub("message", "hallo")
