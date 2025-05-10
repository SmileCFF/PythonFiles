import pygame

global direction

direction = 1
length = 4

WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
FPS = 60

snake_spawn_time = 0
snake_frequency = 500

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
        self.length2 = 30
        self.width2 = 30
        self.rect = pygame.Rect(self.x2,self.y2,self.length2,self.width2)

    def is_apple_hitting_snake(self,snake):
        for SnakePart in snake:
            if self.rect.colliderect(SnakePart.rect):
                length  += 1
                return True
        return False


def draw_window():
    pygame.draw.rect(WIN,BLACK,pygame.Rect(0,0,WIDTH,HEIGHT))

    for SnakePart in snake:
        pygame.draw.rect(WIN, GREEN,SnakePart.rect)

    
    
def moveSnake(snake, direction, length):
    head = snake[len(snake)-1]
    curr_x = head.rect.x
    curr_y = head.rect.y
    if direction == 1:
        target_x = curr_x
        target_y = curr_y - 30
    if direction == 2:
        target_x = curr_x
        target_y = curr_y + 30
    if direction == 3:
        target_x = curr_x + 30
        target_y = curr_y
    if direction == 4:
        target_x = curr_x - 30
        target_y = curr_y
    
    snake.append(SnakePart(target_x,target_y))
    if len(snake) > length:
        del snake[0]
    
   
snake = [SnakePart(100, 100)]

game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]:
            direction = 1
        if keys_pressed[pygame.K_DOWN]:
            direction = 2
        if keys_pressed[pygame.K_RIGHT]:
            direction = 3
        if keys_pressed[pygame.K_LEFT]:
            direction = 4

    is_apple_hitting_snake(snake)

    if pygame.time.get_ticks() - snake_spawn_time > snake_frequency:
        snake_spawn_time = pygame.time.get_ticks()
        moveSnake(snake, direction, length)        
    
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()
