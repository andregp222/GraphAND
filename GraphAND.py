import pygame as pg

def DrawGraph(data:list):
    # pygame uses (r, g, b) color tuples
    white = (255, 255, 255)
    gray = (125, 125, 125)

    width = 900
    height = 900

    # create the display window
    win = pg.display.set_mode((width, height))
    # optional title bar caption
    pg.display.set_caption("Pygame draw circle and save")
    # default background is black, so make it white
    win.fill(white)
    dataprocessed = []
    i = 0
    maxY = 0
    maxX = 0
    while i < len(data):
        if data[i][0] > maxX:
            maxX = data[i][0]
        if data[i][1] > maxY:
            maxY = data[i][1]

        i+=1

    for d in data:
        dataprocessed.append([(d[0]*800/maxX)+50, (((d[1]*800/maxY)-425)*-1)+425])

    # draw a blue circle
    # center coordinates (x, y)
    pg.draw.line(win, gray, (50,0), (50,900),3)
    pg.draw.line(win, gray, (0,850), (900,850),3)

    pg.font.init()
    my_font = pg.font.SysFont('Comic Sans MS', 40)
    j = 0
    print(dataprocessed)
    while j < len(dataprocessed):
        text_surface = my_font.render(str(data[j][1]), True, (0, 0, 0))
        win.blit(text_surface, (0,dataprocessed[j][1]-20))

        text_surface = my_font.render(str(data[j][0]), True, (0, 0, 0))
        win.blit(text_surface, (dataprocessed[j][0]-60,852))
        
        if j > 0 :
            pg.draw.line(win, (255,0,0),dataprocessed[j-1], dataprocessed[j], 5)
            print(j-1,j)
        j+=1

    # now save the drawing
    # can save as .bmp .tga .png or .jpg
    fname = "graph.png"
    pg.image.save(win, fname)
    print("file" + fname + "ehas been saved")

    pg.display.flip()
    pg.quit()
    pass

DrawGraph([(0,0), (100,100),(500,300),(1000,200)])
