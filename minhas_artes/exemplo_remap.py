def setup():
    size(200, 200)
    no_stroke()


def draw():
    background(204)
    x1 = remap(mouse_x, 0, width, 50, 150)
    ellipse(x1, 75, 50, 50)
    x2 = remap(mouse_x, 0, width, 0, 200)
    ellipse(x2, 125, 50, 50)