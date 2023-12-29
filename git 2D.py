import pygame

pygame.init()

#creates a way to track time
clock = pygame.time.Clock()
fps = 60

#screen dimensions in pixels
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel


#cause screen to appear with title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cam's RPG")

#def fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define colors
red = (255, 0, 0)
green = (0, 255, 0)


#load images
#background images
background_img = pygame.image.load('2D action/Background/background.png').convert_alpha()

#bottom panel
panel_img = pygame.image.load('2D action/Icons/panel.png')

#load knight
knight = pygame.image.load('2D action/Knight/Idle/0.png')


# define function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))

#define fuction for drawing bottom panel
def draw_bottom_panel():
    screen.blit(panel_img, (0, 400))
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel + 10)

#create function for drawing text

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))



#fighter class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        #load idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'2D action/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #load attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'2D action/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 100
        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]

        #check if enough time has passed
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has ran out, then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def draw(self):
        screen.blit(self.image, self.rect)

knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 5, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 5, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#run game and allow to quit
run = True
while run:

    clock.tick(fps)

    #draw the background
    draw_bg()

    #draw bottom panel
    draw_bottom_panel()

    #draw fighters
    knight.update()
    knight.draw()

    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()