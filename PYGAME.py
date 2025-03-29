import pygame
import os


WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

pygame.display.set_caption("Shoot the blocks")
os.chdir("/Users/cff/Documents/Python/")
class SpaceShip():
    def __init__(self,img,rotation,dimension):
        a_surf= pygame.image.load(os.path.join('assets',img))
        self.surface = pygame.transform.rotate(pygame.transform.scale(a_surf,dimension,),rotation)
        self.x = WIDTH/2
        self.y = HEIGHT-100

    def updateX(self,x_diff):
        self.x += x_diff

    def updateY(self,y_diff):
        self.y += y_diff

YELLOW_SPACESHIP = SpaceShip('spaceship_yellow.png',180,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
# rotate this image and scale it using pygame.transform 
#YELLOW_SPACESHIP = 

#define a draw_window function that displays all elements on the screen
def draw_window():
    pygame.draw.rect(WIN,BLACK,pygame.Rect(0,0,WIDTH,HEIGHT))
    WIN.blit(YELLOW_SPACESHIP.surface, (YELLOW_SPACESHIP.x,YELLOW_SPACESHIP.y))
    ASTEROID = pygame.image.load(os.path.join('assets','asteroid.png'))
    WIN.blit(pygame.transform.scale(ASTEROID,(50,50)),(WIDTH/2,HEIGHT/2))
    
    
   
game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    #check for all the events that can occur
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if YELLOW_SPACESHIP.x > VEL:
            YELLOW_SPACESHIP.updateX(0-VEL)
    if keys_pressed[pygame.K_RIGHT]:
        if YELLOW_SPACESHIP.x < WIDTH - SPACESHIP_WIDTH - VEL:
            YELLOW_SPACESHIP.updateX(VEL)
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()
