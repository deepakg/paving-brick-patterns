def setup():
    size(840,440)
    background(204)

def draw():
    box_width = 40
    box_height = 20
    for x in range(0,21):
        for y in range(0,21):
            fill(random(140,255))
            if y % 2 == 0:
                x_offset = 0
            else:
                x_offset = -box_width/2
            rect(x*box_width + x_offset, y*box_height, box_width, box_height)
    noLoop()
