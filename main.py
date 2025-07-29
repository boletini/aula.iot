from machine import Pin
from utime import sleep

print("Hello, ESP32!")


led = Pin(15,Pin.OUT)

while True:
    led.on()
    print("LED ON!")
    sleep(0.5)
    led.off()
    print("LED OFF!")
    sleep(0.5)