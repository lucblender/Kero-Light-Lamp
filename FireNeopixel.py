from neopixel import Neopixel
import time
import random

CNT  = 12

pixels = Neopixel(CNT, 0, 28, "BRG")

fire_color = (80, 20, 0)
off_color = (0, 0, 0)

def constrain(in_num, min_num, max_num):
    if in_num < min_num:
        return min_num
    if in_num > max_num:
        return max_num
    return in_num

def clear():
    pixels.fill((0,0,0))
    pixels.show()

def draw():
    for i in range(0, CNT):
        add_color(i, fire_color)
        r = int(random.random()*80)
        diff_color = (r, r/1.7, r/2)
        substract_color(i, diff_color)     
    pixels.show()

def add_color(position, color):
    blended_color = blend(pixels.pixels[position], color)
    pixels.set_pixel(position, blended_color)
    

def substract_color(position, color):
    sub_color = substract(pixels.pixels[position], color)
    pixels.set_pixel(position, sub_color)
  
def blend(color1, color2):
    b1 = (color1 >> 16) & 0xFF
    r1 = (color1 >> 8) & 0xFF
    g1 = (color1 >> 0) & 0xFF
    
    r2 = color2[0]
    g2 = color2[1]
    b2 = color2[2]
    
    return (constrain(r1+r2, 0, 255),constrain(g1+g2, 0, 255),constrain(b1+b2, 0, 255))
  
def substract(color1, color2):
    b1 = (color1 >> 16) & 0xFF
    r1 = (color1 >> 8) & 0xFF
    g1 = (color1 >> 0) & 0xFF
    
    r2 = color2[0]
    g2 = color2[1]
    b2 = color2[2]    
    
    return (constrain(r1-r2, 0, 255),constrain(g1-g2, 0, 255),constrain(b1-b2, 0, 255))

