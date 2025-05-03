import pygame

global direction

direction = 1

WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
FPS = 60

snake_spawn_time = 0
snake_frequency = 1000

class SnakePart ():
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        self.length = 40
        self.width = 40
        self.rect = pygame.Rect(self.x,self.y,self.length,self.width)

class Apple ():
    def __init__ (self,x2,y2):
        self.x2 = x2
        self.y2 = y2
        self.color = RED
        self.radius = 8


def draw_window():
    pygame.draw.rect(WIN,BLACK,pygame.Rect(0,0,WIDTH,HEIGHT))

    for SnakePart in snake:
        pygame.draw.rect(WIN, GREEN,SnakePart.rect)

    if pygame.time.get_ticks() - snake_spawn_time > snake_frequency:
        snake_spawn_time = pygame.time.get_ticks()
        moveSnake()

def moveSnake(snake):
    head = snake[len(snake)-1]
    curr_x = head.rect.x
    curr_y = head.rect.y
    if direction == 1:
        target_x = curr_x
        target_y = curr_y - 100
    if direction == 2:
        target_x = curr_x
        target_y = curr_y + 100
    if direction == 3:
        target_x = curr_x + 100
        target_y = curr_y
    if direction == 4:
        target_x = curr_x - 100
        target_y = curr_y
    
    snake.append(SnakePart(target_x,target_y))
    
   
snake = [SnakePart(100, 100)]

game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False
    
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()
