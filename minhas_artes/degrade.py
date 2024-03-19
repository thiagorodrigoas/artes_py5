def setup():
    size(400, 400)
    no_loop()  # Evita a execução repetida de draw()

def draw():
    background(255)  # Define o fundo como branco
    draw_gradient_square(width / 2 - 50, height / 2 - 50, 100, 100)

def draw_gradient_square(x, y, w, h):
    for i in range(w):
        # Interpolação da cor verde do escuro para o claro da direita para a esquerda
        green_value = remap(i, 0, w, 0, 255)
        fill(0, green_value, 0)  # Define a cor de preenchimento
        no_stroke()  # Remove a borda das formas desenhadas
        rect(x + i, y, 100, h)  # Desenha retângulos finos para criar o degradê

run_sketch()
