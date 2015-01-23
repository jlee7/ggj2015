import pygame

HEIGHT = 1024
WIDTH = 786

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

dude = pygame.image.load("dummy.png")

while True:
	screen.fill(0)
    
    screen.blit(player, (100,100))
    display.flip()

	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    exit(0)
