
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
bg_image = pygame.image.load("Pica-enhance-20250216194236.png")
vodavERh = pygame.image.load("pixil-frame-0 (8).png")
vadaNis =  pygame.image.load("pixil-frame-0 (9).png")
pesok =  pygame.image.load("pixil-frame-0 (6).png")
oblothkopltfrm =  pygame.image.load("pixil-frame-0 (23).png")
oblothkopltfrmlp =  pygame.image.load("pixil-frame-0 (24).png")
mezduvodje = pygame.image.load("vodaseredina.png")
podzemelje = pygame.image.load("zemly.png")
pesok_s = pygame.image.load("pesoknis.png")
bg_image = pygame.transform.scale(bg_image,(800,800))
GAme_oVer_Image = pygame.image.load("pixil-frame-0 (41).png")
hart_full_image = pygame.image.load("fullhart.png")
hart_kapput_image = pygame.image.load("kapputhart.png")
platformaVVV= pygame.image.load("pixil-frame-0 (26).png")
o1= pygame.image.load("pixil-frame-0 (27).png")
o2= pygame.image.load("pixil-frame-0 (28).png")
o3= pygame.image.load("pixil-frame-0 (29).png")
o6= pygame.image.load("pixil-frame-0 (30).png")
o4= pygame.image.load("pixil-frame-0 (31).png")
o5= pygame.image.load("pixil-frame-0 (43).png")
platvorma_pesok= pygame.image.load("pixil-frame-0 (43).png")
o7= pygame.image.load("pixil-frame-0 (32).png")
o8= pygame.image.load("pixil-frame-0 (33).png")
o9= pygame.image.load("pixil-frame-0 (34).png")
flvb_1= pygame.image.load("pixil-frame-0 (48).png")
flvb_2= pygame.image.load("pixil-frame-0 (49).png")
flvb_3= pygame.image.load("pixil-frame-0 (55).png")
flvb_4= pygame.image.load("pixil-frame-0 (56).png")
os1 = pygame.image.load("os1.png")
os2 = pygame.image.load("os2.png")
os3 = pygame.image.load("os3.png")
os4 = pygame.image.load("os4.png")
derevo1 = pygame.image.load("derevo1.png")
derevo2 = pygame.image.load("derevo2.png")
boss_img = pygame.image.load("Boss.png")
bgi6 = pygame.image.load("bgi6.png")
bla1 = pygame.image.load("bla1.png")
bla2 = pygame.image.load("bla2.png")
bla3 = pygame.image.load("bla3.png")
pethka=  pygame.image.load("pethka.png")
fbol =  pygame.image.load("fbol.png")
slizenpustini =  pygame.image.load("slizenpustini.png")
portha =  pygame.image.load("portha.png")
ads =  pygame.image.load("ads.png")
helikopter = pygame.image.load("helikopter.png")
krisha = pygame.image.load("krisha.png") 
final_sword = pygame.transform.scale(pygame.image.load("vaukrutimeth.png"),(50,50))
has_final_sword = False
lavvovajaplatvormaimenjidjonisilverhanda = pygame.image.load("pixil-frame-0 (58).png")
coleckted_swords = []
lives = 15
current_musick = None

def draw_grid():
    for line in range(0, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
main_menu = True

GAme_oVer = 0
class World():
    def __init__(self,data):
        self.tile_list = []
        self.boss = None 
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
                    tile =(img,img_rect,1)
                    self.tile_list.append(tile)
                
                if tile == 2:
                    img = pygame.transform.scale(oblothko_img,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,2)
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
                if tile == 6:
                    img = pygame.transform.scale(vodavERh,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,6)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(vadaNis,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,7)
                    self.tile_list.append(tile)
                if tile == 8:
                    img = pygame.transform.scale(pesok,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,8)
                    self.tile_list.append(tile)
                if tile == 9:
                    img = pygame.transform.scale(mezduvodje,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,9)
                    self.tile_list.append(tile)
                if tile == 10:
                    img = pygame.transform.scale(podzemelje,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,10)
                    self.tile_list.append(tile)
                if tile == 11:
                    img = pygame.transform.scale(pesok_s,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,11)
                    self.tile_list.append(tile)
                if tile == 12:
                    platform = Platform(col_count*tile_size,row_count*tile_size,0,1)
                    platform_Grup.add(platform)
                if tile == 13:
                    platform = Platform(col_count*tile_size,row_count*tile_size,1,0)
                    platform_Grup.add(platform)
                if tile == 14 and 1 not in [s.sword_number for s in coleckted_swords]: 
                    sword = Sword(col_count*tile_size,row_count*tile_size,1)
                    sword_Group.add(sword)
                if tile == 15 and 2 not in [s.sword_number for s in coleckted_swords]:  
                    sword = Sword(col_count*tile_size,row_count*tile_size,2)
                    sword_Group.add(sword)
                if tile == 16 and 3 not in [s.sword_number for s in coleckted_swords]: 
                    sword = Sword(col_count*tile_size,row_count*tile_size,3)
                    sword_Group.add(sword)
                if tile == 17 and 4 not in [s.sword_number for s in coleckted_swords]: 
                    sword = Sword(col_count*tile_size,row_count*tile_size,4)
                    sword_Group.add(sword)                                                    
                if tile == 18 and 5 not in [s.sword_number for s in coleckted_swords]:  
                    sword = Sword(col_count*tile_size,row_count*tile_size,5)
                    sword_Group.add(sword)                                                    
                if tile == 19 and 6 not in [s.sword_number for s in coleckted_swords]:  
                    sword = Sword(col_count*tile_size,row_count*tile_size,6)
                    sword_Group.add(sword)      
                if tile == 53 and 7 not in [s.sword_number for s in coleckted_swords]:  
                    sword = Sword(col_count*tile_size,row_count*tile_size,7)
                    sword_Group.add(sword)                                               
                if tile == 20:
                    img = pygame.transform.scale(o1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,20)
                    self.tile_list.append(tile)
                if tile == 21:
                    img = pygame.transform.scale(o2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,21)
                    self.tile_list.append(tile)
                if tile == 22:
                    img = pygame.transform.scale(o3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,22)
                    self.tile_list.append(tile)
                if tile == 23:
                    img = pygame.transform.scale(o4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,23)
                    self.tile_list.append(tile)
                if tile == 24:
                    img = pygame.transform.scale(o5,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,24)
                    self.tile_list.append(tile)
                if tile == 25:
                    img = pygame.transform.scale(o6,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,25)
                    self.tile_list.append(tile)
                if tile == 26:
                    img = pygame.transform.scale(o7,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,26)
                    self.tile_list.append(tile)
                if tile == 27:
                    img = pygame.transform.scale(o8,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,27)
                    self.tile_list.append(tile)
                if tile == 28:
                    img = pygame.transform.scale(o9,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,28)
                    self.tile_list.append(tile)
                if tile == 29:
                    img = pygame.transform.scale(flvb_1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,29)
                    self.tile_list.append(tile)
                if tile == 30:
                    img = pygame.transform.scale(flvb_2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,30)
                    self.tile_list.append(tile)
                if tile == 31:
                    img = pygame.transform.scale(flvb_3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,31)
                    self.tile_list.append(tile)
                if tile == 32:
                    img = pygame.transform.scale(flvb_4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,32)
                    self.tile_list.append(tile)              
                if tile == 33:
                    img = pygame.transform.scale(os1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,33)
                    self.tile_list.append(tile)
                if tile == 34:
                    img = pygame.transform.scale(os2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,34)
                    self.tile_list.append(tile)
                if tile == 35:
                    img = pygame.transform.scale(os3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,35)
                    self.tile_list.append(tile)
                if tile == 36:
                    img = pygame.transform.scale(os4,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,36)
                    self.tile_list.append(tile)
                if tile == 37:
                    img = pygame.transform.scale(derevo1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,37)
                    self.tile_list.append(tile)
                if tile == 38:
                    img = pygame.transform.scale(derevo2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,38)
                    self.tile_list.append(tile)
                if tile ==40:
                    self.boss = Bosyra(col_count*tile_size,row_count*tile_size)
                    boss_group.add(self.boss)
                if tile == 41:
                    img = pygame.transform.scale(bla1,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,41)
                    self.tile_list.append(tile)
                if tile == 42:
                    img = pygame.transform.scale(bla2,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,42)
                    self.tile_list.append(tile)
                if tile == 43:
                    img = pygame.transform.scale(bla3,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,43)
                    self.tile_list.append(tile)
                if tile == 44:
                    img = pygame.transform.scale(pethka,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,44)
                    self.tile_list.append(tile)
                if tile == 45:
                    exit2 = Exit2(col_count*tile_size,row_count*tile_size-(tile_size//2))
                    exit_Groub2.add(exit2)
                if tile == 46:
                    img = pygame.transform.scale(fbol,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,46)
                    self.tile_list.append(tile)
                if tile == 47:
                    platforml = LavaPlatform(col_count*tile_size,row_count*tile_size,1,0)
                    platform_Grup.add(platforml)
                if tile == 48:
                   enemy = Enemy_1(col_count * tile_size,row_count*tile_size+10)
                   enemy_GROuB2.add(enemy)               
                if tile == 49:
                   enemy = Enemy_2(col_count * tile_size,row_count*tile_size+10)
                   enemy_GROuB3.add(enemy)
                if tile == 50:
                   enemy = Enemy_3(col_count * tile_size,row_count*tile_size+10)
                   enemy_GROuB4.add(enemy)                
                if tile == 51:
                    img = pygame.transform.scale(krisha,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,8)
                    self.tile_list.append(tile)
                if tile == 52:
                    img = pygame.transform.scale(helikopter,(tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile =(img,img_rect,8)
                    self.tile_list.append(tile)

                col_count +=1
            row_count+=1
    def draw(self):
        for i in self.tile_list:
            screen.blit(i[0],i[1])
           
class Atackkristalom_black:
    def __init__(self,x,y):
        self.images= []
        for i in range(1,14):
            img = pygame.image.load(f"KTH{i}.png")
            img = pygame.transform.scale(img,(75,100))
            self.images.append(img)
        self.damage = 2
        self.index =0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True
        self.animation_speed = 2
        self.current_frame = 0
        self.lifetime = 200
    def update(self):    
        if self.active:
            self.current_frame +=1
            if self.current_frame >= self.animation_speed:
                self.current_frame = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = len(self.images) -1 
                self.image = self.images[self.index]     
    def draw(self,screen):
        if self.active:
            screen.blit(self.image,self.rect)



class Supersnositheluronasonnyerixon993:
    def __init__(self,x,y):
        self.images= []
        for i in range(1,23):
            img = pygame.image.load(f"sa{i}.png")
            #img = pygame.transform.scale(img,(75,100))
            self.images.append(img)
        self.damage = 3
        self.index =0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True
        self.animation_speed = 2
        self.current_frame = 0
        self.lifetime = 200
    def update(self):    
        if self.active:
            self.current_frame +=1
            if self.current_frame >= self.animation_speed:
                self.current_frame = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = len(self.images) -1 
                self.image = self.images[self.index]     
    def draw(self,screen):
        if self.active:
            screen.blit(self.image,self.rect)
class Atackkristalom_blackR:
    def __init__(self,x,y):
        self.images= []
        for i in range(1,14):
            img = pygame.image.load(f"KTH{i}.png")
            img = pygame.transform.flip(img,1,1)
            self.images.append(img)
            
        self.index =0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 2
        self.active = True
        self.animation_speed = 2
        self.current_frame = 0
        self.lifetime = 200
    def update(self):    
        if self.active:
            self.current_frame +=1
            if self.current_frame >= self.animation_speed:
                self.current_frame = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = len(self.images) -1 
                self.image = self.images[self.index]  
    def draw(self,screen):
        if self.active:
            screen.blit(self.image,self.rect)
class Atackkristalom_y:
    def __init__(self,x,y):
        self.images= []
        for i in range(1,12):
            img = pygame.image.load(f"ky{i}.png")
            self.images.append(img)    
        self.index =0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 2
        self.active = True
        self.animation_speed = 2
        self.current_frame = 0
        self.lifetime = 200
    def update(self):    
        if self.active:
            self.current_frame +=1
            if self.current_frame >= self.animation_speed:
                self.current_frame = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = len(self.images) -1 
                self.image = self.images[self.index]  
    def draw(self,screen):
        if self.active:
            screen.blit(self.image,self.rect)
class lutajaatakaviolrthjivoistreloi:
    def __init__(self,x,y):
        self.images= []
        for i in range(1,38):
            img = pygame.image.load(f"as{i}.png")
            self.images.append(img)    
        self.index =0 
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 2
        self.active = True
        self.animation_speed = 2
        self.current_frame = 0
        self.lifetime = 300
    def update(self):    
        if self.active:
            self.current_frame +=1
            if self.current_frame >= self.animation_speed:
                self.current_frame = 0
                self.index +=1
                if self.index >= len(self.images):
                    self.index = len(self.images) -1 
                self.image = self.images[self.index]  
    def draw(self,screen):
        if self.active:
            screen.blit(self.image,self.rect)


            
class Bosyra(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boss_img,(125,125))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y=y
        self.helth = 80
        self.atackcd = 400
        self.atackastreloicd = 0
        self.cristals =[]
        self.attacikng = False
        self.current_attack_type = 0
        self.attack_switch_timer = 0
        self.attack_switch_delay = 500
        
    def take_damage(self,damage):
        self.helth -= damage 
        if self.helth <= 0:
            self.kill()
    def check_player_height(self,player):
        return player.rect.y <= 525
    def atack(self):
        if self.atackcd <=0 and not self.attacikng:
            self.attacikng = True
            self.attack_duration = 300
            if self.current_attack_type == 0:
                cristal5 = Atackkristalom_y(188,636)
                cristal6 = Atackkristalom_y(388,636)
                cristal7 = Atackkristalom_y(725,606)
                cristal5.lifetime = 200   
                cristal6.lifetime = 200   
                cristal7.lifetime = 200   
                self.cristals.append(cristal5)
                self.cristals.append(cristal6)
                self.cristals.append(cristal7)
                self.current_attack_type = 1
                self.attack_switch_timer = self.attack_switch_delay
            elif self.current_attack_type == 1:
                	
                cristal = Atackkristalom_black(88,636)
                cristal2 = Atackkristalom_blackR(563,600)
                cristal3 = Atackkristalom_black(288,636)
                cristal4 = Atackkristalom_black(488,636)

                cristal.lifetime = 200   
                cristal2.lifetime = 200
                cristal3.lifetime = 200
                cristal4.lifetime = 200
                self.cristals.append(cristal)
                self.cristals.append(cristal2)
                self.cristals.append(cristal3)
                self.cristals.append(cristal4)
                
                self.current_attack_type = 2
                self.attack_switch_timer = self.attack_switch_delay
            else:
                cristal8 = Supersnositheluronasonnyerixon993(79 ,669)
                cristal8.lifetime = 200
                self.cristals.append(cristal8)
                self.current_attack_type = 0
                self.attack_switch_timer = self.attack_switch_delay         
            self.atackcd = 400       
    def lyutayastrela(self):
            cristal9 = lutajaatakaviolrthjivoistreloi(200,275)
            cristal10 = lutajaatakaviolrthjivoistreloi(565,330)
            cristal11 = lutajaatakaviolrthjivoistreloi(370,125)
            cristal12 = lutajaatakaviolrthjivoistreloi(620,330)
            self.cristals.append(cristal9)
            self.cristals.append(cristal10)
            self.cristals.append(cristal11)
            self.cristals.append(cristal12)
            cristal9.lifetime = 200
            cristal10.lifetime = 200
            cristal11.lifetime = 200 
            self.current_attack_type = 0
            self.attack_switch_timer = self.attack_switch_delay
            
            self.atackastreloicd = 200
    def update(self,player):
        self.atackcd-=1
        self.atackastreloicd -=1

        if self.check_player_height(player) and self.atackastreloicd <=0:
            self.lyutayastrela()

        if self.attack_switch_timer > 0 :
            self.attack_switch_timer -=1


        if self.attacikng:
            self.attack_duration -=1
            if self.attack_duration <= 0:
                self.attacikng = False
        self.atack()
        for i in self.cristals[:]:
            i.update()
            i.lifetime -=1
            if i.lifetime <= 0 or not i.active:
                self.cristals.remove(i)
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        for i in self.cristals:
            i.draw(screen)

class Player():
    def __init__(self,x,y):
        self.reset(x,y)

    def reset(self,x,y) :
        self.invisible= False
        self.invisibletomer = 0
        self.attaking = False
        self.cdattaking = 0
        self.images_right = []
        self.images_left = []
        self.Atack_Right = []
        self.Atack_left = []
        self.index = 0
        self.atack_index = 0
        self.counter = 0
        self.dead_image = pygame.image.load("pixil-frame-0 (22).png")
        for num in range(1, 4):
            img_right = pygame.image.load(f'player{num}.png')
            img_right = pygame.transform.scale(img_right, (20, 40))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        for i in range(1,6):
            Atack_Right = pygame.image.load(f"PLAYERFINALLVL{i}.png")
            Atack_Right = pygame.transform.scale(Atack_Right,(40,44))
            Atack_left = pygame.transform.flip(Atack_Right,True,False)
            self.Atack_Right.append(Atack_Right)
            self.Atack_left.append(Atack_left)
            
            
            
            
            
            
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
    def update(self,GAme_oVer):
        dx = 0
        dy = 0
        wolk_kd = 10
        global has_final_sword
        global world 
        global level
        global lives 
        global coleckted_swords
        
        
        
        key = pygame.key.get_pressed()
        if GAme_oVer == 0:
            if self.invisible:
                self.invisibletomer -=1
                if self.invisibletomer <=0:
                    self.invisible= False
                
                
                
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_fx.play()
                self.vel_y = -14
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_a]:
                dx -=5
                self.counter +=1
                self.direction = -1
            if key[pygame.K_d]:
                dx +=5
                self.counter +=1
                self.direction = 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if not self.attaking and self.cdattaking <= 0:
                        self.attaking = True
                        self.cdattaking = 20
                        self.index = 0
            if self.attaking:
                self.atack_index +=1
                if self.atack_index >= len(self.Atack_Right):
                    self.attaking = False    
                    self.atack_index = 0
                else:
                    attack_rect = pygame.Rect(
                        self.rect.x + (self.direction * tile_size),
                        self.rect.y,
                        tile_size+5,
                        tile_size+12   
                    )
                    pygame.draw.rect(screen,(255,0,0),attack_rect,2)

                    for enemy in enemy_GROuB:
                        if attack_rect.colliderect(enemy.rect):
                            if has_final_sword:
                                enemy.take_damage(1)
                            else:
                                enemy.take_damage(0.5)
                                
                    for enemy in enemy_GROuB2:
                        if attack_rect.colliderect(enemy.rect):
                            if has_final_sword:
                                enemy.take_damage(1)
                            else:
                                enemy.take_damage(0.5)
                                
                    for enemy in enemy_GROuB3:
                        if attack_rect.colliderect(enemy.rect):
                            if has_final_sword:
                                enemy.take_damage(1)
                            else:
                                enemy.take_damage(0.5)
                                
                    for enemy in enemy_GROuB4:
                        if attack_rect.colliderect(enemy.rect):
                            if has_final_sword:
                                enemy.take_damage(1)
                            else:
                                enemy.take_damage(0.5)
                                
                    for enemy in boss_group:
                        if attack_rect.colliderect(enemy.rect):
                            if has_final_sword:
                                enemy.take_damage(1)
                            else:
                                enemy.take_damage(0.5)
                    
            if self.cdattaking > 0:
                self.cdattaking -=1
                



            if self.counter > wolk_kd:
                self.counter = 0
                self.index +=1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]          
            if self.attaking and self.direction == 1:
                self.image = self.Atack_Right[self.atack_index]
                
            elif self.attaking and self.direction == -1:
                self.image = self.Atack_left[self.atack_index]
                
            
            
            self.vel_y +=1
            if self.vel_y > 10:
                self.vel_y = 10 
            dy += self.vel_y
            
        
            

            self.in_air = True
            for tile in world.tile_list:
                tile_img,tile_rect,tile_type = tile
                if tile_type == 44 and len(coleckted_swords) >= 7 and not has_final_sword:
                    coleckted_swords.clear()
                    final_swordd = Sword(0,0,8)
                    coleckted_swords.append(final_swordd)
                    has_final_sword = True
            for tile in world.tile_list:
                tile_img,tile_rect,tile_type = tile
                if tile_type in [37,38]:
                    continue
                    
                if tile [1].colliderect(self.rect.x + dx,self.rect.y ,self.width,self.height):
                    dx = 0
                if tile [1].colliderect(self.rect.x,self.rect.y + dy,self.width,self.height): 
                    if self.vel_y < 0:
                        dy = tile [1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile [1].top - self.rect.bottom
                        self.vel_y = 0 
                        self.in_air = False
            sword_coleckted = pygame.sprite.spritecollide(self,sword_Group,True)
            for sword in sword_coleckted:
                coleckted_swords.append(sword)
            
            
            if (pygame.sprite.spritecollide(self, enemy_GROuB , False) or 
                pygame.sprite.spritecollide(self, enemy_GROuB2, False) or 
                pygame.sprite.spritecollide(self, enemy_GROuB3, False) or 
                pygame.sprite.spritecollide(self, enemy_GROuB4, False)) and not self.invisible:
                lives -=1 
                self.invisible = True
                self.invisibletomer = 20
                if lives <= 0:
                    GAme_oVer = -1
                    GAme_oVer_fx.play()
            if pygame.sprite.spritecollide(self,BALAnda_GROuB,False)and not self.invisible:
                lives -=1 
                self.invisible = True
                self.invisibletomer = 20
                if lives <= 0:
                    GAme_oVer = -1
                    GAme_oVer_fx.play()

            for exit in exit_Groub2:
                if self.rect.colliderect(exit.rect):
                    level = 6
                    world_data = []
                    world = reset_level(level)
                    GAme_oVer = 0
                    break
            for exit in exit_Groub:
                if self.rect.colliderect(exit.rect):
                    if exit.rect.x < screen_width //2:
                        level-=1 
                        if level < 1:
                            level = 1
                    else:
                        level +=1
                        if level > max_level:
                            level = max_level
                    world_data = []
                    world = reset_level(level)
                    GAme_oVer = 0
                    break 
                                
           #for platform in platform

            for platform in platform_Grup:
                if platform.rect.colliderect(self.rect.x +dx,self.rect.y , self.width,self.height):
                    dx = 0
                if platform.rect.colliderect(self.rect.x,self.rect.y +dy,self.width,self.height):
                    if abs((self.rect.top + dy)-platform.rect.bottom)< 20:
                        self.vel_y = 0
                        dy = platform.rect.bottom -self.rect.top 
                    elif abs((self.rect.bottom + dy)-platform.rect.top)< 20:
                        self.rect.bottom = platform.rect.top -1
                        self.in_air = False
                        dy = 0
                    if platform.move_x !=0:
                        self.rect.x += platform.move_direction       

            self.rect.x += dx
            self.rect.y += dy
                
        elif GAme_oVer == -1:
            pygame.mixer.music.stop()
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

class Exit2(pygame.sprite.Sprite):
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
        self.health = 2
    def take_damage(self,damage):
        self.health -= damage 
        if self.health <= 0:
            self.kill()
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
class Enemy_1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("slizenpustini.png")    
        self.rect = self.image.get_rect()    
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.health = 2
    def take_damage(self,damage):
        self.health -= damage 
        if self.health <= 0:
            self.kill()
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
class Enemy_2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ads.png")    
        self.rect = self.image.get_rect()    
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.health = 2
    def take_damage(self,damage):
        self.health -= damage 
        if self.health <= 0:
            self.kill()
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Enemy_3(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("portha.png")    
        self.rect = self.image.get_rect()    
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.health = 2
    def take_damage(self,damage):
        self.health -= damage 
        if self.health <= 0:
            self.kill()
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

    pygame.mixer.music.stop()
    if level in lvl_musuk:
        pygame.mixer.music.load(lvl_musuk[level])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    else:
        pygame.mixer.music.load("Mlvl1.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
    player.reset(100,screen_height-130)        
    enemy_GROuB.empty()
    enemy_GROuB2.empty()
    enemy_GROuB3.empty()
    enemy_GROuB4.empty()
    BALAnda_GROuB.empty()
    exit_Groub.empty()
    platform_Grup.empty()
    boss_group.empty()

    sword_Group.empty()
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
jump_fx = pygame.mixer.Sound("3f00da9bdf24c19.mp3")
jump_fx.set_volume(0.5)
GAme_oVer_fx = pygame.mixer.Sound("680efe34665ab92.mp3")
GAme_oVer_fx.set_volume(0.5)           

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y, move_x , move_y ):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("pixil-frame-0 (23).png")
        self.image = pygame.transform.scale(img,(tile_size,tile_size // 2 ))
        self.rect= self.image.get_rect()
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
class LavaPlatform(pygame.sprite.Sprite):
    def __init__(self,x,y, move_x , move_y ):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("pixil-frame-0 (58).png")
        self.image = pygame.transform.scale(img,(tile_size,tile_size // 2 ))
        self.rect= self.image.get_rect()
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
class Sword(pygame.sprite.Sprite):           
    def __init__(self,x,y,sword_number):
        pygame.sprite.Sprite.__init__(self)
        if sword_number == 8:
            self.image = pygame.image.load("vaukrutimeth.png")
        else:
            self.image = pygame.image.load(f"sword{sword_number}.webp")
        self.image = pygame.transform.scale(self.image,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y) 
        self.sword_number = sword_number     

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
lvl_musuk = {
    1:"Mlvl1.mp3",
    2:"Mlvl2.mp3",
    3:"Mlvl3.mp3",
    4:"Mlvl3.mp3",
    5:"Mlvl3.mp3",
    6:"tac.mp3",
    7:"MlvlF.mp3"
}           
           
bglvl1 = pygame.image.load("OIP (4).png")
bglvl2 = pygame.image.load("bglvl2.png")
bglvl3 = pygame.image.load("lvlkakoito.png")
bglvl4 = pygame.image.load("3f.png")
bglvl5 = pygame.image.load("4f.png")
bglvl6 = pygame.image.load("bgi6.png")
bglvl7= pygame.image.load("pixil-frame-0 (47).png")
bgimages = {
    1:pygame.transform.scale(bglvl1,(screen_width,screen_height)),
    2:pygame.transform.scale(bglvl2,(screen_width,screen_height)),
    3:pygame.transform.scale(bglvl3,(screen_width,screen_height)),
    4:pygame.transform.scale(bglvl4,(screen_width,screen_height)),
    5:pygame.transform.scale(bglvl5,(screen_width,screen_height)),
    6:pygame.transform.scale(bglvl6,(screen_width,screen_height)),
    7:pygame.transform.scale(bglvl7,(screen_width,screen_height)),
}      

def draw_lives():
    for i in range(lives):
        screen.blit(hart_full_image,(600+i*(tile_size//2+5),25))
def draw_swords():
    if has_final_sword :
        screen.blit(final_sword,(10,10))
    else:
        for i,swords in enumerate(coleckted_swords):
            x = (10+i*(tile_size+5))
            y = 10 
            screen.blit(swords.image,(x,y))



level = 1
max_level = 10
enemy_GROuB = pygame.sprite.Group()
enemy_GROuB2 = pygame.sprite.Group()
enemy_GROuB3 = pygame.sprite.Group()
enemy_GROuB4 = pygame.sprite.Group()
BALAnda_GROuB = pygame.sprite.Group()
exit_Groub = pygame.sprite.Group()
exit_Groub2 = pygame.sprite.Group()
platform_Grup = pygame.sprite.Group()
sword_Group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
#world = World (world_data)
player = Player(100,screen_height-130)  
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
    curimage = bgimages.get(level,bg_image)
    screen.blit(curimage,(0,0))
    if main_menu == True:
        screen.blit(bg_image,(0,0))
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu= False 
            if level in lvl_musuk:
                pygame.mixer.music.load(lvl_musuk[level])
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.2)
    else :
        world.draw()
        if GAme_oVer == 0:
            
            enemy_GROuB.update()
            enemy_GROuB2.update()
            enemy_GROuB3.update()
            enemy_GROuB4.update()
            platform_Grup.update()
            sword_Group.update()
            boss_group.update(player)
        for boss in boss_group:
            boss.update(player)
            boss.draw(screen)
            if  player.rect.colliderect(boss.rect):
                    if not player.invisible:
                        lives-=1
                        player.invisible = True
                        player.invisibletomer = 20
                        if lives <= 0:
                            GAme_oVer = -1
                            GAme_oVer_fx.play()
            for crystal in boss.cristals:
                if crystal.active and player.rect.colliderect(crystal.rect):
                    if not player.invisible:
                        lives-=crystal.damage
                        player.invisible = True
                        player.invisibletomer = 20
                        if lives <= 0:
                            GAme_oVer = -1
                            GAme_oVer_fx.play() 
                         
        if world.boss is not None:
            boss_group.draw(screen)

        enemy_GROuB.draw(screen )
        enemy_GROuB2.draw(screen )
        enemy_GROuB3.draw(screen )
        enemy_GROuB4.draw(screen )
        BALAnda_GROuB.draw(screen)
        exit_Groub.draw(screen)
        exit_Groub2.draw(screen)
     
        platform_Grup.draw(screen)
        sword_Group.draw(screen)
        draw_swords()
        draw_lives()
        GAme_oVer = player.update(GAme_oVer)  
        if GAme_oVer  == -1:
            pygame.mixer.music.stop()
            if lives > 0:
                lives -=1
                world_data=[]
                world = reset_level(level)
                GAme_oVer = 0
            else:
                screen.blit(GAme_oVer_Image,(344,250))
                if restart_button.draw():
                    level = 1
                    lives = 5
                    world_data = []
                    world = reset_level(level) 
                    GAme_oVer = 0
                    score = 0
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
                    coleckted_swords = []
                    world =reset_level(level)
                    GAme_oVer = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    
    