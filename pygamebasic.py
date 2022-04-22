import pygame
pygame.init
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Basics")
x,y=250,250
vel=5
run=True
while(run==True):
	pygame.draw.rect(win,(255,0,0),(100,20,70,70))
	pygame.display.update()
	pygame.time.delay(50)
	for event in pygame.event.get():
		if(event.type==pygame.QUIT):
			run=False
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		pygame.draw.rect(win,(255,0,0),(x,y,70,70))
		x -= vel
	if keys[pygame.K_RIGHT]:
		x += vel
	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel
	win.fill((255,255,255))
	pygame.draw.rect(win,(0,0,255),(x,y,70,70))
	pygame.display.update()
	
pygame.quit()
	
