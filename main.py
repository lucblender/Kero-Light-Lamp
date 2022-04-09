from machine import Pin, Timer
import time
from FireNeopixel import *

MIST_ON = 0
MIST_OFF = 1

mode = False
fan_on_counter = 0
update_mist_counter = 0
up_to = 0
old_up_to = 0

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
    mode = not mode
    
button.irq(debounce, Pin.IRQ_FALLING)

def update_mist_strength():
    global update_mist_counter, up_to, old_up_to
    if update_mist_counter%35 == 0:
        up_to = random.randrange(1,4)
        if old_up_to != up_to:
            turn_off_all()
            turn_on_up_to(up_to)            
            print(up_to)
        old_up_to = up_to
    update_mist_counter += 1

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
    
def fan_clear():
    fan.value(0)
    
def fan_on():
    fan.value(1)

def random_fan_lifecycle():
    global fan_on_counter
    if fan.value() == 1:
        fan_on_counter += 1
        if fan_on_counter > 40:
            print("ici0")
            fan_clear()
            fan_on_counter = 0
        elif fan_on_counter > 10:   
            if random.random()>0.95:  
                print("ici1")              
                fan_clear()
                fan_on_counter = 0
    else:
        if random.random()>0.95:
            fan_on()
        

turn_on_all()
time.sleep(1)
turn_off_all()
clear()

while True:
    if mode == True:
        draw()
        random_fan_lifecycle()
        update_mist_strength()
    else:
        update_mist_counter = 0
        up_to = 0
        old_up_to = 0
        clear()
        fan_clear()
        turn_off_all()

    time.sleep_ms(random.randrange(50,150))

    




