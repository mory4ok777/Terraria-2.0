
import pygame

import	pickle 
from os import path
 
from pygame import mixer 

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TERRARIA2.0")
tile_size = 25
restart_image = pygame.image.load("restart_btn.png")
start_img = pygame.image.load("start_btn.png")
exit_img = pygame.image.load("exit_btn.png")
bg_image = pygame.image.load("OIP (4).png")
bg_image = pygame.transform.scale(bg_image,(800,800))
def draw_grid():
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
main_menu = True

GAme_oVer = 0
class World():
    def __init__(self,data):
        self.tile_list = []
        dirt_img = pygame.image.load("dirt.png")#zemly foto
        oblothko_img = pygame.image.load("oblothko.png")
        row_count = 0
        for row in data:
            col_count = 0 
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect)
                    self.tile_list.append(tile)
                
                if tile == 2:
                    img = pygame.transform.scale(oblothko_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    enemy = Enemy(col_count * tile_size,row_count*tile_size+10)
                    enemy_GROuB.add(enemy)
                if tile == 4:
                    BALAnda = LAVAnda(col_count * tile_size,row_count*tile_size+(tile_size//2))
                    BALAnda_GROuB.add(BALAnda)
                if tile == 5:
                    exit = Exit(col_count*tile_size,row_count*tile_size-(tile_size//2))
                    exit_Groub.add(exit)
                col_count +=1
            row_count += 1

    def draw(self):
        for i in self.tile_list:
            screen.blit(i[0],i[1])
class Player():
    def __init__(self,x,y):
        self.reset(x,y)
    def reset(self,x,y) :
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.dead_image = pygame.image.load("pixil-frame-0 (22).png")
        for num in range(1, 4):
            img_right = pygame.image.load(f'player{num}.png')
            img_right = pygame.transform.scale(img_right, (20, 40))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
       
    def update(self,GAme_oVer):
        dx = 0
        dy = 0
        wolk_kd = 10
        key = pygame.key.get_pressed()
        if GAme_oVer == 0:
            if key[pygame.K_b] and self.jumped == False:
                jump_fx.play()
                self.vel_y = -14
                self.jumped = True
            if key[pygame.K_b] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -=5
                self.counter +=1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx +=5
                self.counter +=1
                self.direction = 1
            if self.counter > wolk_kd:
                self.counter = 0
                self.index +=1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]            
            self.vel_y +=1
            if self.vel_y > 10:
                self.vel_y = 10 
            dy += self.vel_y
            
        
            
            
            
            
            for tile in world.tile_list:
                if tile [1].colliderect(self.rect.x + dx,self.rect.y ,self.width,self.height):
                    dx = 0
                if tile [1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height): 
                    if self.vel_y < 0:
                        dy = tile [1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile [1].top - self.rect.bottom
                        self.vel_y = 0 
            if pygame.sprite.spritecollide(self,enemy_GROuB,False):
                GAme_oVer = -1
                GAme_oVer_fx.play()
            if pygame.sprite.spritecollide(self,BALAnda_GROuB,False):
                GAme_oVer = -1
                GAme_oVer_fx.play()
            if pygame.sprite.spritecollide(self,exit_Groub,False):
                GAme_oVer = 1
            self.rect.x += dx
            self.rect.y += dy
                
        elif GAme_oVer == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -=5
        screen.blit(self.image,self.rect)     
        #pygame.draw.rect(screen,(255,255,255),self.rect,2)
        return GAme_oVer
class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((tile_size,int(tile_size*1.5)),pygame.SRCALPHA)#
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y        

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("normalslitzen.png")    
        self.rect = self.image.get_rect()    
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
class LAVAnda(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        img=pygame.image.load("LAVAnda.png")
        self.image = pygame.transform.scale(img,(tile_size,tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def reset_level(level):
    player.reset(100,screen_height-130)        
    enemy_GROuB.empty()
    BALAnda_GROuB.empty()
    exit_Groub.empty()
    
    if path.exists(f"level{level}_data"):
        pickle_in = open(f"level{level}_data","rb")
        world_data = pickle.load(pickle_in)
    world = World(world_data)
    
    return world    
        
class Button():
    def __init__(self,x,y, image ):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y = y 
        self.clicked = False
    def draw(self):
        action = False 

        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        screen.blit(self.image,self.rect)
        
        return action
                
mixer.init()

pygame.mixer.music.load("digiffects-sound-effects-library-capercaillie-bird-in-forest-with-other-birds-version-1.mp3")
pygame.mixer.music.play(-1,0.0,5000)
jump_fx = pygame.mixer.Sound("3f00da9bdf24c19.mp3")
jump_fx.set_volume(0.5)
GAme_oVer_fx = pygame.mixer.Sound("680efe34665ab92.mp3")
GAme_oVer_fx.set_volume(0.5)           

class platform(pygame.sprite.Sprite):
    def __init__(self,x,y, move_x , move_y ):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("pixil-frame-0 (23).png")
        self.image = pygame.transform.scale(img,(tile_size,tile_size // 2 ))
        self.rect.x = x
        self.rect.y = y
        self.move_counter= 0
        self.move_direction  = 1 
        self.move_x = move_x
        self.move_y = move_y
        
        
    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter +=1
        if abs(self.move_counter)> 50:
            self.move_direction *= -1
            self.move_counter *= -1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,2,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[2,2,0,0,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0],
[2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[5,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],
[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,5],
[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,5],
[1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
level = 1
max_level = 9
enemy_GROuB = pygame.sprite.Group()
BALAnda_GROuB = pygame.sprite.Group()
exit_Groub = pygame.sprite.Group()
#world = World (world_data)
player = Player(50,screen_height-100)  
clock = pygame.time.Clock()
restart_button = Button(screen_width//2-75,screen_height//2,restart_image)
start_button = Button(screen_width//2-350,screen_height//2,start_img)
exit_button = Button(screen_width//2+150,screen_height//2,exit_img)
run = True
if path.exists(f"level{level}_data"):
    pickle_in = open(f"level{level}_data","rb")
    world_data = pickle.load(pickle_in)
world = World(world_data)
while run:
    clock.tick(40)
    screen.blit(bg_image,(0,0))
    if main_menu == True:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu= False 
    else :
        world.draw()
        if GAme_oVer == 0:
            
            enemy_GROuB.update()
        enemy_GROuB.draw(screen )
        BALAnda_GROuB.draw(screen)
        exit_Groub.draw(screen)
        GAme_oVer = player.update(GAme_oVer)
        if GAme_oVer == -1:
            if restart_button.draw():
                world_data = []
                level = 1
                world = reset_level(level)
                GAme_oVer = 0
#       draw_grid()
        if GAme_oVer == 1:
            level+=1
            if level <=max_level:
                world_data=[]
                world =reset_level(level)
                GAme_oVer = 0
            else :
                if restart_button.draw():
                    level=1
                    world_data = []
                    world =reset_level(level)
                    GAme_oVer = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
    