from site import venv




venv
import sys
import pygame
from pygame.color import THECOLORS


pygame.init()
screen = pygame.display.set_mode((1200,800))
screen.fill(THECOLORS['antiquewhite'])


image = pygame.image.load("Bin/01.png")
pygame.display.set_caption("MyFirstGame")
screen.blit(image,(20,20))

bg = pygame.image.load ("Bin/04.png")
bg = pygame.transform.scale(bg,(1200,800))
screen.blit(bg,(20,20))


image = pygame.transform.scale(image,(30,32))
x = 5
y = 10

screen.blit(image, (x,y))
r = pygame.Rect(50,50,100,30)
pygame.draw.rect(screen, (255,0,0),r,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()



 