import pygame
pygame.init
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Basics")
x,y=450,450
run=True
while(run==True):
	pygame.time.delay(50)
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			run=False
	pygame.draw.rect(win,(0,0,255),(x,y,70,70))
	pygame.display.update()
	
pygame.quit()
	
