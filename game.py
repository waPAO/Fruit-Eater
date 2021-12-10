import pygame
from pygame import image
from random import randint

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'imgs/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()  

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.y > 500: 
            self.reset()

    def reset(self):
        self.x = randint(50, 400)
        self.y = -64

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'imgs/player.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 100

    def right(self):
        self.dx += 100

    def up(self):
        self.dy -= 100

    def down(self):
        self.dy += 100

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32


apple = Apple()
player= Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
        
    
    screen.fill((255, 255, 255))

    apple.move()
    apple.render(screen)

    player.move()
    player.render(screen)

    pygame.display.flip()
    clock.tick(30)

