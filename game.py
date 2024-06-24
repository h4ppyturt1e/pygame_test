import sys
import pygame

pygame.init()

pygame.display.set_caption('test gaem')
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # gets all the events that are happening
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60) # forces to 60fps
    
    