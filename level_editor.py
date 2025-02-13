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
sun_img = pygame.image.load('img/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('img/sky.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
dirt_img = pygame.image.load('img/dirt.png')
grass_img = pygame.image.load('img/grass.png')
blob_img = pygame.image.load('img/blob.png')
platform_x_img = pygame.image.load('img/platform_x.png')
platform_y_img = pygame.image.load('img/platform_y.png')
lava_img = pygame.image.load('img/lava.png')
coin_img = pygame.image.load('img/coin.png')
exit_img = pygame.image.load('img/exit.png')
save_img = pygame.image.load('img/save_btn.png')
load_img = pygame.image.load('img/load_btn.png')

# Глобальні змінні
clicked = False
level = 1
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

# Створення пустої карти
world_data = [[0] * cols for _ in range(cols)]

# Створення меж карти
for tile in range(cols):
    world_data[cols - 1][tile] = 2
    world_data[0][tile] = 1
    world_data[tile][0] = 1
    world_data[tile][cols - 1] = 1

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
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                elif world_data[row][col] == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                elif world_data[row][col] == 3:
                    img = pygame.transform.scale(blob_img, (tile_size, int(tile_size * 0.75)))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size * 0.25)))
                    continue
                elif world_data[row][col] == 4:
                    img = pygame.transform.scale(platform_x_img, (tile_size, tile_size // 2))
                elif world_data[row][col] == 5:
                    img = pygame.transform.scale(platform_y_img, (tile_size, tile_size // 2))
                elif world_data[row][col] == 6:
                    img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
                    continue
                elif world_data[row][col] == 7:
                    img = pygame.transform.scale(coin_img, (tile_size // 2, tile_size // 2))
                    screen.blit(img, (col * tile_size + (tile_size // 4), row * tile_size + (tile_size // 4)))
                    continue
                elif world_data[row][col] == 8:
                    img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
                    screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
                    continue
                if img:
                    screen.blit(img, (col * tile_size, row * tile_size))

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
    screen.blit(sun_img, (tile_size * 2, tile_size * 2))

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
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
            pos = pygame.mouse.get_pos()
            x, y = pos[0] // tile_size, pos[1] // tile_size
            if x < cols and y < cols:
                if pygame.mouse.get_pressed()[0]:
                    world_data[y][x] = (world_data[y][x] + 1) % 9
                elif pygame.mouse.get_pressed()[2]:
                    world_data[y][x] = (world_data[y][x] - 1) % 9
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            elif event.key == pygame.K_DOWN and level > 1:
                level -= 1

    pygame.display.update()

pygame.quit()
