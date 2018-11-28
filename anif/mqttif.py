from anif.anif import AccessNetworkInterface
from paho.mqtt import client as paho_mqtt
import threading
import time


class MQTTInterface(AccessNetworkInterface):
    def __init__(self, addr, port):
        super().__init__(addr, port)
        self._client = paho_mqtt.Client(protocol=paho_mqtt.MQTTv31)

    def _connect(self):
        self._client.connect(host=self._addr, port=self._port, keepalive=0)

    def _disconnect(self):
        self._client.disconnect()


class MQTTPublishInterface(MQTTInterface):
    def _send(self):
        self._client.publish(self._file, self._data, qos=0)

    def _recv(self):
        None


class MQTTSubscribeInterface(MQTTInterface):
    def _on_connect(self, client, userdata, flags, rc):
        self._client.subscribe(self._file, qos=0)

    def _on_message(self, client, userdata, msg):
        self._data = msg.payload
    
    def _connect(self):
        self._client.on_connect = self._on_connect
        self._client.on_message = self._on_message
        super()._connect()
        self._thread = threading.Thread(target=self._client.loop_start())
        self._thread.start()
        time.sleep(1.1) # This is better becouse sensor data is received
                        # at about 1 second intervals

    def _disconnect(self):
        self._client.loop_stop()
        super()._disconnect()

        #TODO: implement thread safe procedure
        
    def _send(self):
        None

    def _recv(self):
        return self._data