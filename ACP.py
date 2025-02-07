

#ACP-Add sprite

import pygame
import random

surf_color="pink"
color="blue"  
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect()
    def moveRight(self, pixels):
	    self.rect.x += pixels
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    def moveForward(self, speed):
        self.rect.y += speed * speed/10
    def moveBack(self, speed):
        self.rect.y -= speed * speed/10
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding Sprite")

sprite_list=pygame.sprite.Group()

s1=Sprite(color, 50,50)
s1.rect.x=random.randint(0,450)
s1.rect.y=random.randint(0,450)
sprite_list.add(s1)

s2=Sprite("green", 50,50)
s2.rect.x=random.randint(0,450)
s2.rect.y=random.randint(0,450)
sprite_list.add(s2)

exit=True
clock=pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False
    
    keys = pygame.key.get_pressed()
	
    if keys[pygame.K_LEFT]:
        s1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        s1.moveRight(5)
    if keys[pygame.K_DOWN]:
        s1.moveForward(5)
    if keys[pygame.K_UP]:
        s1.moveBack(5)
  
    
    sprite_list.update()
    screen.fill(surf_color)
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)  #msec

pygame.quit()

