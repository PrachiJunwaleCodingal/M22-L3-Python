#custom event

import pygame
import random
  
SColor = "pink"
color = "blue"

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        self.image.fill(SColor)
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
  
pygame.init()

sprit_lst = pygame.sprite.Group()

s1 = Sprite(color, 50,50)
s1.rect.x = random.randint(0,480)
s1.rect.y = random.randint(0,480)
sprit_lst.add(s1)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Custom events")
screen.fill(SColor)

Ncolor = "green"
bgColor = SColor
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)
exit = True
clock = pygame.time.Clock()

while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		if event.type == CHANGE_COLOR:
			if bgColor == Ncolor:
				screen.fill(Ncolor)
				bgColor = SColor
			elif bgColor == SColor:
				screen.fill(SColor)
				bgColor = Ncolor
  
	sprit_lst.update()
	sprit_lst.draw(screen)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
