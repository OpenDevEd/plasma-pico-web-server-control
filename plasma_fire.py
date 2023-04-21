import plasma
from plasma import plasma_stick
import time
from random import random, uniform
import plasma_config

"""
A basic fire effect.
"""

async def fire():    # Set how many LEDs you have
    NUM_LEDS = 50

    # WS2812 / NeoPixel™ LEDs
    led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

    # Start updating the LED strip
    led_strip.start()
    #k=0
    while True and plasma_config.state != 0:
    #while True:
        # fire effect! Random red/orange hue, full saturation, random brightness
        for i in range(NUM_LEDS):
            try:
                led_strip.set_hsv(i, uniform(0.0, 50 / 360), 1.0, random())
            except:
                print("led_strip error")
        time.sleep(0.5)
        #k=k+1
        #print("Fire"+str(k))
        
    print("done with fire")    

#config.state=1
#fire()