import pygame

pygame.init()

scr_width = 500
scr_height = 500
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Ping Pong")
# создаём таймер
clock = pygame.time.Clock()

FPS = 50

screen.fill((20, 180, 255))



class GameSprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, 
                                (self.rect.width, self.rect.height))     
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, x, y, w, h, image, speed_x, speed_y):
        super().__init__(x, y, w, h, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    def move(self):
        #мяч движется в зависимости от скорости
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # если касается верхней границы, скорость по вертикали меняет знак
        if self.rect.y >= scr_height - self.rect.height:
            self.speed_y *= (-1)
        # если касается нижней границы, скорость по вертикали меняет знак
        if self.rect.y <= 0:
            self.speed_y *= (-1)

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed, key_up, key_down):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.key_down = key_down
        self.key_up = key_up
    
    def move(self):
        if pygame.key.get_pressed()[self.key_up]:
           self.rect.y -= self.speed
        if pygame.key.get_pressed()[self.key_down]:
           self.rect.y += self.speed

game = True
while game:




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()
    clock.tick(FPS)
