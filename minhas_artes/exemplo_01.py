import random

# Lista para guardar os círculos
circulos = []

def setup():
    size(800, 600)
    no_stroke()

def draw():
    background(30)
    
    # Atualizar e desenhar os círculos
    for circulo in circulos[:]:
        circulo['size'] *= 0.95  # Diminuir o tamanho do círculo
        #fill(circulo['color'])
        fill(color(circulo['color'][0],circulo['color'][1],circulo['color'][2]))
        circle(circulo['x'], circulo['y'], circulo['size'])
        
        # Remover o círculo se ele for muito pequeno
        if circulo['size'] < 1:
            circulos.remove(circulo)

def mouse_pressed():
    # Adicionar novos círculos na posição do mouse
    for _ in range(10):  # Gerar 10 círculos
        circulos.append({
            'x': mouse_x,
            'y': mouse_y,
            'size': random.randint(150, 200),
            'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        })
