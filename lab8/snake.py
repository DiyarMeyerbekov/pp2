import pygame,sys
import random
pygame.init()
height=500
width=500
cell_size=10
score=0
speed=10
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
font = pygame.font.Font(None,30) 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

snake_pos=[100,100]
snake_body=[[100,100],[80,100],[60,100]]
direction='RIGHT'
change_to=direction
clock=pygame.time.Clock()
running=True
dot=0
#food append
food_list = [[random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10] for _ in range(4)]
def spawn_food():
    while True:
        new_food = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height// 10)) * 10]
        if new_food not in snake_body:
            return new_food
food_spawn = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to='UP'
            if event.key==pygame.K_DOWN:
                change_to='DOWN'
            if event.key==pygame.K_RIGHT:
                change_to='RIGHT'
            if event.key==pygame.K_LEFT:
                change_to='LEFT'
# Move snake based on direction
    direction=change_to
    if change_to=='UP':
        snake_pos[1]-=cell_size
    elif change_to=='DOWN':
        snake_pos[1]+=cell_size
    elif change_to=='RIGHT':
        snake_pos[0]+=cell_size
    elif change_to=='LEFT':
        snake_pos[0]-=cell_size
# Check for collision with walls
    if snake_pos[0]<0 or snake_pos[0]>=width:
        running=False
    elif snake_pos[1]<0  or snake_pos[1]>=height:
        running=False
  
    snake_body.insert(0,list(snake_pos))
# Check if food is eaten
    if snake_pos in food_list:
        score += 1
        food_list.remove(snake_pos)
        food_list.append(spawn_food())
    else:
        snake_body.pop()

    if not food_spawn:
        food_list = [[random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10] for _ in range(4)]
    food_spawn = True
    if score %4 == 0 and score !=0:
        if dot ==1:
            WHITE =(random.randint(0, 200), random.randint(0, 200), random.randint(0, 255))
            dot = 0
            speed+=5
    else:
        dot=1
    screen.fill(BLACK)
    # drawing snake and food
    for block in snake_body:
        pygame.draw.rect(screen,GREEN,pygame.Rect(block[0],block[1],cell_size,cell_size))
    for food in food_list:
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))

    score_text = font.render(f"Your score: {score}",True,'white')
    screen.blit(score_text,(20,20))
    game_level_text = font.render(f"Level: {int(score/4)}",True,'white')
    screen.blit(game_level_text,(400,20))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
