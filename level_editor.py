import pygame
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Налаштування вікна
tile_size = 25
cols = 32
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')

# Завантаження зображень
oblothko_img = pygame.image.load("oblothko.png")
bg_img = pygame.image.load('OIP (4).png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
#dirt_img = pygame.image.load('dirt.png')
grass_img = pygame.image.load('dirt.png')
blob_img = pygame.image.load('normalslitzen.png')
# platform_x_img = pygame.image.load('img/platform_x.png')
# platform_y_img = pygame.image.load('img/platform_y.png')
lava_img = pygame.image.load('LAVAnda.png')
# coin_img = pygame.image.load('img/coin.png')
exit_img =pygame.Surface((tile_size,int(tile_size*1.5)))#
exit_img.fill((255,0,0))

exit_img2 =pygame.Surface((tile_size,int(tile_size*1.5)))#
exit_img2.fill((0,255,0))
save_img = pygame.image.load('save_btn.png')
load_img = pygame.image.load('load_btn.png')
vodavERh = pygame.image.load("pixil-frame-0 (8).png")
vadaNis =  pygame.image.load("pixil-frame-0 (9).png")
pesok =  pygame.image.load("pixil-frame-0 (6).png")
oblothkopltfrm =  pygame.image.load("pixil-frame-0 (25).png")
oblothkopltfrmlp =  pygame.image.load("pixil-frame-0 (24).png")
mezduvodje = pygame.image.load("vodaseredina.png")
podzemelje = pygame.image.load("zemly.png")
pesok_s = pygame.image.load("pesoknis.png")
swords1 = pygame.image.load("sword1.webp")
swords2  = pygame.image.load("sword2.webp")
swords3  = pygame.image.load("sword3.webp")
swords4 = pygame.image.load("sword4.webp")
swords5  =pygame.image.load("sword5.webp")
swords6  =pygame.image.load("sword6.webp")
swords7  =pygame.image.load("sword7.webp")
platformaVVV= pygame.image.load("pixil-frame-0 (26).png")
o1= pygame.image.load("pixil-frame-0 (27).png")
o2= pygame.image.load("pixil-frame-0 (28).png")
o3= pygame.image.load("pixil-frame-0 (29).png")
o6= pygame.image.load("pixil-frame-0 (30).png")
o4= pygame.image.load("pixil-frame-0 (31).png")
o5= pygame.image.load("pixil-frame-0 (43).png")
platvorma_pesok= pygame.image.load("pixil-frame-0 (43).png")
fbol =  pygame.image.load("fbol.png")
o7= pygame.image.load("pixil-frame-0 (32).png")
o8= pygame.image.load("pixil-frame-0 (33).png")
o9= pygame.image.load("pixil-frame-0 (34).png")
flvlb_1= pygame.image.load("pixil-frame-0 (48).png")
flvlb_2= pygame.image.load("pixil-frame-0 (49).png")
flvlb_3= pygame.image.load("pixil-frame-0 (55).png")
flvlb_4= pygame.image.load("pixil-frame-0 (56).png")
os1 = pygame.image.load("os1.png")
os2 = pygame.image.load("os2.png")
os3 = pygame.image.load("os3.png")
os4 = pygame.image.load("os4.png")
derevo1 = pygame.image.load("derevo1.png")
derevo2 = pygame.image.load("derevo2.png")
boss = pygame.image.load("Boss.png")
bla1 = pygame.image.load("bla1.png")
bla2 = pygame.image.load("bla2.png")
bla3 = pygame.image.load("bla3.png")
pethka=  pygame.image.load("pethka.png")
slizenpustini =  pygame.image.load("slizenpustini.png")
portha =  pygame.image.load("portha.png")
ads =  pygame.image.load("ads.png")
helikopter = pygame.image.load("helikopter.png")
krisha = pygame.image.load("krisha.png") 
lavvovajaplatvormaimenjidjonisilverhanda = pygame.image.load("pixil-frame-0 (58).png")
# Глобальні змінні
clicked = False
level = 1
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

# Створення пустої карти
world_data = [[0] * cols for _ in range(cols)]

# Створення меж карти
# for tile in range(cols):
#     world_data[cols - 1][tile] = 2
#     world_data[0][tile] = 1
#     world_data[tile][0] = 1
#     world_data[tile][cols - 1] = 1

# Функція малювання тексту
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Малювання сітки
def draw_grid():
    for c in range(cols + 1):
        pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height - margin))
        pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))

# Малювання світу
def draw_world():
    for row in range(cols):
        for col in range(cols):
            if world_data[row][col] > 0:
                img = None
                if world_data[row][col] == 1:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 2:
                    img = pygame.transform.scale(oblothko_img, (tile_size, tile_size))   
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 3:
                    img = pygame.transform.scale(blob_img, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                    continue
                elif world_data[row][col] == 12:
                     img = pygame.transform.scale(oblothkopltfrm, (tile_size, tile_size // 2))
                     screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 13:
                     img = pygame.transform.scale(oblothkopltfrmlp, (tile_size, tile_size // 2))
                     screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 4:
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
                    continue
                # elif world_data[row][col] == 7:
                #     img = pygame.transform.scale(coin_img, (tile_size // 2, tile_size // 2))
                #     screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
                #     continue
                elif world_data[row][col] == 5:
                    img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
                    screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
                    continue
                elif world_data[row][col] == 6:
                    img = pygame.transform.scale(vodavERh, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 7:
                    img = pygame.transform.scale(vadaNis, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 8:
                    img = pygame.transform.scale(pesok, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 9:
                    img = pygame.transform.scale(mezduvodje, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))            
                elif world_data[row][col] == 10:
                    img = pygame.transform.scale(podzemelje, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 11:
                    img = pygame.transform.scale(pesok_s, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 14:
                    img = pygame.transform.scale( swords1, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 15:
                    img = pygame.transform.scale(swords2, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 16:
                    img = pygame.transform.scale(swords3, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 17:
                    img = pygame.transform.scale(swords4, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 18:
                    img = pygame.transform.scale(swords5, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 19:
                    img = pygame.transform.scale(swords6, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 53:
                    img = pygame.transform.scale(swords7, (tile_size, tile_size))    
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 20:
                    img = pygame.transform.scale(o1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 21:
                    img = pygame.transform.scale(o2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 22:
                    img = pygame.transform.scale(o3, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 23:
                    img = pygame.transform.scale(o4, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 24:
                    img = pygame.transform.scale(o5, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 25:
                    img = pygame.transform.scale(o6, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 26:
                    img = pygame.transform.scale(o7, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 27:
                    img = pygame.transform.scale(o8, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 28:
                    img = pygame.transform.scale(o9, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 29:
                    img = pygame.transform.scale(flvlb_1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 30:
                    img = pygame.transform.scale(flvlb_2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 31:
                    img = pygame.transform.scale(flvlb_3, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 32:
                    img = pygame.transform.scale(flvlb_4, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 33:#1
                    img = pygame.transform.scale(os1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 34:#1
                    img = pygame.transform.scale(os2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 35:#1
                    img = pygame.transform.scale(os3, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 36:#1
                    img = pygame.transform.scale(os4, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 37:#1
                    img = pygame.transform.scale(derevo1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 38:#1
                    img = pygame.transform.scale(derevo2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))                    
                elif world_data[row][col] == 40:
                    img = pygame.transform.scale(boss, (tile_size*5, tile_size*5))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 41:
                    img = pygame.transform.scale(bla1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 42:
                    img = pygame.transform.scale(bla2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 43:
                    img = pygame.transform.scale(bla3, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 44:
                    img = pygame.transform.scale(pethka, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 45:
                    img = pygame.transform.scale(exit_img2, (tile_size, int(tile_size * 1.5)))
                    screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
                elif world_data[row][col] == 46:
                    img = pygame.transform.scale(fbol, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size)) 
                elif world_data[row][col] == 47:
                    img = pygame.transform.scale(lavvovajaplatvormaimenjidjonisilverhanda, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 48:
                    img = pygame.transform.scale(slizenpustini, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                elif world_data[row][col] == 49:
                    img = pygame.transform.scale(ads, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                elif world_data[row][col] == 50:
                    img = pygame.transform.scale(portha, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                elif world_data[row][col] == 51:
                    img = pygame.transform.scale(krisha, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                elif world_data[row][col] == 52:
                    img = pygame.transform.scale(helikopter, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                    
                continue             
    
                                
                                
                                                
                
                
                                                                                                                                                                               
                       
                
# Клас кнопки
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Створення кнопок
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

# Основний цикл гри
run = True
while run:
    clock.tick(fps)
    screen.fill(green)
    screen.blit(bg_img, (0, 0))
    #screen.blit(sun_img, (tile_size * 2, tile_size * 2))

    if save_button.draw():
        with open(f'level{level}_data', 'wb') as pickle_out:
            pickle.dump(world_data, pickle_out)

    if load_button.draw():
        if path.exists(f'level{level}_data'):
            with open(f'level{level}_data', 'rb') as pickle_in:
                world_data = pickle.load(pickle_in)

    draw_grid()
    draw_world()

    draw_text(f'Level: {level}', font, white, tile_size, screen_height - 60)
    draw_text('Press UP or DOWN to change level', font, white, tile_size, screen_height - 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEWHEEL:
     
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // tile_size, pos[1] // tile_size
            if x < cols and y < cols:
                if event.y == 1:
                    world_data[y][x] +=1
                    if world_data[y][x]> 54:
                        world_data[y][x] = 0
                elif event.y == -1:
                    world_data[y][x] -=1
                    if world_data[y][x]<0:
                        world_data[y][x] = 54
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    pygame.display.update()

pygame.quit()
