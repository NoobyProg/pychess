import pygame
import sys
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

black = (00,00,00)
white = (255,255,255)
run = True

pawn = pygame.image.load('assets/c_pawn.png')
pawn = pygame.transform.smoothscale(pawn, (50, 50))

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_pawns = pygame.sprite.Group()
pawn_1 = Player(pawn, rows[1], columns[1])
all_pawns.add(pawn_1)

while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False 

        def row_type_1(z):
            for i in range(0,8,2):
                pygame.draw.rect(base, white, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))
                pygame.draw.rect(base, black, pygame.Rect((rows[i+1],columns[z]), (res[0]//8,res[1]//8)))               

        def row_type_2(z):
            for i in range(0,8,2):
                pygame.draw.rect(base, black, pygame.Rect((rows[i],columns[z]), (res[0]//8,res[1]//8)))               
                pygame.draw.rect(base, white, pygame.Rect((rows[i+1],columns[z]), (res[0]//8,res[1]//8)))
       
        for i in range(0, 8, 2):
            row_type_1(i)
            row_type_2(i+1)
        
        all_pawns.draw(base)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_pawns if s.rect.collidepoint(pos)]
            if clicked_sprites:
                p_col = columns.index(clicked_sprites[0].rect.y)
                if p_col < 7:
                    clicked_sprites[0].rect.y = columns[p_col + 1]                    

        pygame.display.update()

pygame.quit()
sys.exit()