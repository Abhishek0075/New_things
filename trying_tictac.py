import pygame
pygame.init
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Basics")
vel=5
run=True
while(run==True):
    pygame.display.update()
    pygame.time.delay(50)
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            run=False
    pygame.draw.rect(win,(0,0,255),(0,0,140,140))
    pygame.draw.rect(win,(0,0,255),(180,0,140,140))
    pygame.draw.rect(win,(0,0,255),(360,0,140,140))
    pygame.draw.rect(win,(0,0,255),(0,180,140,140))
    pygame.draw.rect(win,(0,0,255),(180,180,140,140))
    pygame.draw.rect(win,(0,0,255),(360,180,140,140))
    pygame.draw.rect(win,(0,0,255),(0,360,140,140))
    pygame.draw.rect(win,(0,0,255),(180,360,140,140))
    pygame.draw.rect(win,(0,0,255),(360,360,140,140))
    pygame.display.update()
	
pygame.quit()
	
