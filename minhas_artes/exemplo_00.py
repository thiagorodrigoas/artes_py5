import pandas as pd

class Particle:
    pass    
    
    
def setup():
    size(400, 400)
    rect_mode(CENTER)


def draw():
    square(mouse_x, mouse_y, 40)


def mouse_clicked():
    fill(random_int(255), random_int(255), random_int(255))


#run_sketch()