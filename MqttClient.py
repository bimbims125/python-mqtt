from paho.mqtt import client as mqtt
from typing import Union

class MqttClient:
  """"Manages connection to mqtt broker"""

  def __init__(self):
    self.clientId = "pramId"
    self.broker = "localhost"
    self.port = 1883
    self.connect()

  def connect(self):
    """Connect to mqtt clients"""
    client = mqtt.Client(self.clientId)
    client.connect(self.broker, self.port, 60)
    self._client = client

  def pub(self, topic:str, payload:str):
    self.client.publish(topic, payload)

  @property
  def client(self):
    return self._client
