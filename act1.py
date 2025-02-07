# Add sprite 
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

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding Sprite")

sprite_list=pygame.sprite.Group()

s1=Sprite(color, 50,50)
s1.rect.x=random.randint(0,450)
s1.rect.y=random.randint(0,450)
sprite_list.add(s1)

exit=True
clock=pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False

    sprite_list.update()
    screen.fill(surf_color)
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)  #msec

pygame.quit()
