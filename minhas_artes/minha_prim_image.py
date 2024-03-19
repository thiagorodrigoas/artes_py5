# Lista para armazenar a posição e a velocidade de cada gota
gotas = []

# Número de gotas na chuva
numero_de_gotas = 500

def setup():
    size(640, 360)
    background(230, 230, 250)
    # Inicializa as gotas em posições e velocidades aleatórias
    for _ in range(numero_de_gotas):
        gotas.append([random(width), random(height), random(4, 50)])

def draw():
    background(230, 230, 250)
    
    # Desenha cada gota
    for gota in gotas:
        stroke(43, 43, 43)
        #stroke_weight(2)
        x, y, velocidade = gota
        line(x, y, x, y + 10)
        
        # Atualiza a posição da gota
        gota[1] += velocidade
        
        # Reseta a gota para o topo se ela sair do fundo da tela
        if gota[1] > height:
            gota[1] = random(-200, -100)
            gota[2] = random(4, 10)
