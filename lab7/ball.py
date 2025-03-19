import pygame
pygame.init()
width=600
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Ball")
speed=20
x,y=width // 2,height // 2
rad=25
running=True
while running:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(x,y),rad)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and x-speed>0+rad:
                x-=speed
            elif event.key==pygame.K_RIGHT and x+speed<height-rad:
                x+=speed
            elif event.key==pygame.K_UP and y-speed>0+rad:
                y-=speed
            elif event.key==pygame.K_DOWN and y+speed<width-rad:
                y+=speed
            pygame.display.flip()
pygame.quit()
