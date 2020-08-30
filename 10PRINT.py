import pygame
import random
WIDTH = 800
HEIGHT = 800
AMT = 40;
BLACK = (0,0,0);
WHITE = (255,255,255);

pygame.init();
screen = pygame.display.set_mode((WIDTH,HEIGHT));
clock = pygame.time.Clock();
x = 0
y = 0	
screen.fill(WHITE);
while True:
	clock.tick(60);
	chance = random.random();
	if chance > 0.69: #////
		pygame.draw.line(screen, BLACK,(x,y+AMT), (x+AMT,y),4)
	else: #\\\\\
		pygame.draw.line(screen, BLACK,(x,y), (x+AMT,y+AMT),4)
	x += AMT
	if x > WIDTH:
		x = 0;
		y += AMT
	if y > HEIGHT:
		break;
	pygame.display.update()
	pygame.event.pump();
