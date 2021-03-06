# Start of my pygame
import pygame
import random
import os

WIDTH= 800
HEIGHT = 600
FPS = 30

# define colors 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0, 0, 255)

# set up assests folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    # sprite for Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'Image_cardgame.png' )).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5


    #def update(self):
        # self.rect.x += 5
        # self.rect.y += self.y_speed
        # if self.rect.bottom > HEIGHT - 200:
        #     self.y_speed = -5
        # if self.rect.top < 200:
        #     self.y_speed = 5
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0
            
   
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cards Against Moms")
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Georgia', 30)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
lefttextsurface = myfont.render('Hello world', False, (0, 255, 255))
answers = ['img/Img1.png', 'img/Img2.png','img/Img3.png', 'img/Img4.png']
righttextsurface = myfont.render('Chastity Kick Ass', False, (255, 0, 255))
questions = ['img/cover1.png', 'img/Qimg1.png', 'img/Qimg2.png', 'img/Qimg3.png', 'img/Qimg4.png']


#Game Loop
running = True
while running:
    # Keep to loop running at right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            #textsurface = myfont.render('Cards Against Moms', False, (255, 255, 255))
            number = (random.randint(0, 3))
            if pygame.mouse.get_pos()[0] > 150 and pygame.mouse.get_pos()[0] < 350 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 450:
                lefttextsurface = pygame.image.load(answers[number]).convert_alpha()
                #lefttextsurface = myfont.render( answers[number], False, (0, 255, 0))
            elif pygame.mouse.get_pos()[0] > 450 and pygame.mouse.get_pos()[0] < 650 and pygame.mouse.get_pos()[1] > 150 and pygame.mouse.get_pos()[1] < 450:
                righttextsurface = pygame.image.load(questions[number]).convert_alpha()
            

            
    # Update
    all_sprites.update()
    # Draw/render
    screen.fill(BLACK)
    pygame.draw.rect(screen, [255, 255, 255], [150, 150, 200, 300], 0)
    screen.blit(lefttextsurface, (150, 150))
    screen.blit(righttextsurface, (450, 150))
    pygame.draw.rect(screen, [255, 255, 255 ], [450, 150, 200, 300 ], 5)
   #all_sprites.draw(screen)
    # *after* drawing everthing, flip the display
    pygame.display.flip()



pygame.quit()
