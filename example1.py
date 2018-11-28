from vlamp.vlamp import Lamp
import time


lamp = Lamp("172.29.156.35", 1883)
lamp.enable()

lamp.on()
time.sleep(3)
lamp.off()

lamp.disable()