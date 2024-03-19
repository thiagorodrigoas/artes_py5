def setup():
    global s
    s = load_shape("bot.svg")


def draw():
    background(204)
    shape(s)


def mouse_pressed():
    # move the shape 10 pixels right each time the mouse is pressed
    s.translate(10, 0)