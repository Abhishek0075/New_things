import pygame
pygame.init
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Basics")

run=True
while(run==True):
	pygame.time.delay(100)
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			run=False
pygame.quit()
	