import paho.mqtt.client as mqtt
from PySide6.QtCore import QObject, Signal

class MQTTClient(QObject):
    connected = Signal()
    disconnected = Signal()
    message_received = Signal(str, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
    
    def connect_to_broker(self, host, port):
        self.client.connect(host, port)
        self.client.loop_start()
    
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected.emit()
        else:
            self.disconnected.emit()
    
    def on_disconnect(self, client, userdata, rc):
        self.disconnected.emit()
    
    def on_message(self, client, userdata, msg):
        self.message_received.emit(msg.topic, msg.payload.decode())
    
    def subscribe(self, topic):
        self.client.subscribe(topic)
    
    def publish(self, topic, message):
        self.client.publish(topic, message)
