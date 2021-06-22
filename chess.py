import pygame
pygame.init()

res = (600, 600)
base = pygame.display.set_mode(res)

rows = []
for i in range(9):
    coord = res[0]//8 * i
    rows.append(coord)

columns = []
for i in range(9):
    coord = res[1]//8 * i
    columns.append(coord)

black = (80,80,80)
white = (255,255,255)
run = True

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False 

        def row_type_1(z):
            for i in range(0,8,2):
                pygame.draw.rect(base, white, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))
            for i in range(1,8,2):
                pygame.draw.rect(base, black, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))               

        def row_type_2(z):
            for i in range(0,8,2):
                pygame.draw.rect(base, black, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))               
            for i in range(1,8,2):
                pygame.draw.rect(base, white, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))
       
        for i in range(0, 8, 2):
            row_type_1(i)
        for i in range(1, 8, 2):
            row_type_2(i)

        pawn = pygame.image.load('assets/c_pawn.png')
        pawn = pygame.transform.smoothscale(pawn, (50, 50))

        for i in range(8):
            base.blit(pawn,(rows[i],columns[1]))

        pygame.display.update()

pygame.quit()