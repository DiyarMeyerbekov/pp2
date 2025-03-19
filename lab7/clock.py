import pygame
import datetime
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()
#images
clock_img=pygame.image.load('clock.png')
clock_img=pygame.transform.scale(clock_img,(800,600))
second_img=pygame.image.load('sec.png')
second_img=pygame.transform.scale(second_img,(300,850))
min_img=pygame.image.load('min.png')
min_img=pygame.transform.scale(min_img,(40,500))
center_x, center_y = 400,300
running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #time
    now=datetime.datetime.now()
    seconds=now.second
    mins=now.minute

    angle_sec=(60-seconds)*6
    angle_min=(60-mins)*6
    #for sec
    rotated_sec=pygame.transform.rotate(second_img,angle_sec)
    sec_rect=rotated_sec.get_rect(center=(center_x,center_y))
    screen.blit(rotated_sec, sec_rect)
    #for min
    rotated_min=pygame.transform.rotate(min_img,angle_min)
    min_rect=rotated_min.get_rect(center=(center_x,center_y))
    screen.blit(rotated_min,min_rect)
    pygame.display.flip()
    clock.tick(1)
pygame.quit()