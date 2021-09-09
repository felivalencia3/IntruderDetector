# IntruderDetector

A Raspberry Pi is a very cheap, small, credit card sized, fully functioning computer, it’s used for controlling sensors and electrical currents through code.

So I decided to use the Raspberry Pi and the sensors I had to make a simple, yet useful intruder detector. To make the simplest possible intruder detector you need an infrared sensor, such as the HC-SR501 (which is the one I used in my project)

This small device works by first adjusting itself to the base infrared heat signature in the room and then looking for any changes in the infrared signature. It’s constantly sending a signal to the Raspberry Pi, if no movement is detected the signal will be stable and low, but whenever something warm passes in front of the detector, the signal will spike:

Through the GPIO pins, the raspberry pi is able to read this signal and run an event whenever a spike happens. It’s also important to note that the hotter the object that passed in front is, the higher the signal spike will be. I set my sensor to only recognize objects over 30ºC, so that it only goes off when a person or animal passes it front.

An infrared sensor would be enough for a simple intruder detector, but I wanted to take it a step further and so I decided to also use a tilt sensor.

It works by using a tiny ball of mercury that moves back and forth with gravity. If the sensor is pointing downwards, the ball will roll down and disconnect the circuit, if it tilts upwards it will reconnect the circuit and send a signal.
My plan was to use this as a second layer of protection, the first layer would notify me if a person walked in front of the sensor and the second layer would notify me (more urgently) if that person moved or tampered with the detector.

