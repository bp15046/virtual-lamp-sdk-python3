from anif.mqttif import MQTTPublishInterface
import json


class Lamp(MQTTPublishInterface):
    def enable(self);
        self.open("PrototypingEnvironment/Actuator/Lamp")

    def disable(self)
        self.close()

    def on(self):
        self.write(json.dumps({"power":"on"}))

    def off(self):
        self.write(json.dumps({"power":"off"})