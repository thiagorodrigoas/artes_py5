elipses = []

def setup():
    size(1584, 396)
    size_rect = 15
    for x in range(width-25, 0, -25):
        if size_rect < 40:
            size_rect += 0.5
        for y in range(height-25, 0, -25):
            elipses.append([0, 0, size_rect, size_rect])


def draw():
    stroke(0)
    i = 0
    cor1 = (23, 177, 245) # azul
    cor2 = (0, 0, 0)#(83, 210, 38)  verde
    
    for j in range(width):
        red_value = remap(j, 0, width, cor2[0], cor1[0])
        green_value = remap(j, 0, width, cor2[1], cor1[1])
        blue_value = remap(j, 0, width, cor2[2], cor1[2])
        stroke(red_value, green_value, blue_value)
        
        line(j,0, j, height)
    count_x = 0
    count_y = 0
    for x in range(width-25, 0, -25):
        for y in range(height-25, 0, -25):
            
            limite = i / 10
            push_matrix()
            
            offset_x = random(-limite, limite) / 5
            offset_y = random(-limite, limite) / 5
            translate(x + offset_x, y + offset_y)
            rotate(radians(random(-limite, limite)))
            
            red_value = remap(x, 0, width,cor1[0], cor2[0] )
            green_value = remap(x, 0, width,cor1[1], cor2[1])
            blue_value = remap(x, 0, width,cor1[2] ,cor2[2])
            
            stroke_value = remap(x, 0, width,255,0)
            stroke(stroke_value, stroke_value, stroke_value)
            fill(red_value, green_value, blue_value)

            
            rect(elipses[count_x+count_y][0], elipses[count_x+count_y][1], elipses[count_x+count_y][2], elipses[count_x+count_y][3] ,random(-5,5))
      
            pop_matrix()
            i += 3
            count_y += 1
        count_x += 0
    text_size(16)
    fill(0, 0, 0)
    text("Desenvolvido com Python!", width/2, height-15)
    text("Desenvolvido com Python!", width/2, height-15)
    no_loop()

    