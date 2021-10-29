import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# ----------------
# zip() function
# ----------------
name = ['asa', 'afa', 'dna', 'slm', 'ahm']
age = [40, 30, 14, 12, 9]
initials = ['js', 'python', 'html', 'word', 'css']

displ = zip(name, age, initials)
for i in displ:
    print(i)