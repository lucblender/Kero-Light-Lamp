from machine import Pin, Timer
import time
from FireNeopixel import *

MIST_ON = 0
MIST_OFF = 1

mode = 0

led = Pin(25, Pin.OUT)
fan = Pin(22, Pin.OUT)
mist_0 = Pin(11, Pin.OUT)
mist_1 = Pin(12, Pin.OUT)
mist_2 = Pin(13, Pin.OUT)
button = Pin(18, Pin.IN, Pin.PULL_UP)

fan.value(0)

timer = Timer()

mists = [mist_0, mist_1, mist_2]

mode_number = len(mists)+1

def debounce(pin):
    timer.init(mode=Timer.ONE_SHOT, period=500, callback=button_listener)


def button_listener(pin):
    print("button_listener")    
    global mode
    mode = (mode+1)%mode_number
    turn_on_up_to(mode)
    
button.irq(debounce, Pin.IRQ_FALLING)


def turn_on_up_to(index):
    if index == 0:        
        turn_off_all()
    
    for i in range(0, index):
        blink_led()
        mists[i].value(MIST_ON)

def turn_on_all():
    for mist in mists:
        mist.value(MIST_ON)
        
def turn_off_all():
    for mist in mists:
        mist.value(MIST_OFF)
        
def turn_on_index(index):
    mists[index].value(MIST_ON)
    
def turn_off_index(index):
    mists[index].value(MIST_OFF)
    
def sequence_turn_on():
    for i in range(0,4):
        turn_on_index(i)
        time.sleep(1)
        
def blink_led():    
    led.value(1)
    time.sleep(0.05)
    led.value(0)
    time.sleep(0.05)

def random_fan_lifecycle():
    if random.random()>0.95:
        fan.value(not fan.value())
def fan_clear():
    fan.value(0)
    
turn_off_all()
clear()

while True:
    if mode != 0:
        draw()
        random_fan_lifecycle()  
    else:
        clear()
        fan_clear()
        
         
        
    time.sleep_ms(random.randrange(50,150))

    




