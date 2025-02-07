#random color cube
import pygame
import random
pygame.init()

color_changeEvent = pygame.USEREVENT + 1

magenta = pygame.Color('magenta')
brown = pygame.Color('brown')
blue = pygame.Color('blue')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__() #call parent class (Sprite) constructor
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])] #x,y speed

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]  # reverse direction 
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(color_changeEvent))

    def change_color(self):
        self.image.fill(random.choice([magenta, brown, blue]))


sprit_lst = pygame.sprite.Group()
s1 = Sprite(blue, 40, 40)
s1.rect.x = random.randint(0, 480)
s1.rect.y = random.randint(0, 480)
sprit_lst.add(s1)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing cube")
screen.fill("pink")
exit = False
clock = pygame.time.Clock()

while not exit:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
    elif event.type == color_changeEvent:
      s1.change_color()


  sprit_lst.update()
  screen.fill("pink")
  sprit_lst.draw(screen)
  pygame.display.flip()
  clock.tick(240)  # Limit the frame rate to 240 fps

pygame.quit()
