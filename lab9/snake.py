import pygame
import random
import time
pygame.init()
# Window 
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
RED = (255, 0, 0)  
BLUE = (135, 206, 235) 
GOLD = (255, 215, 0)  
BLACK = (0, 0, 0)  
# Dictionary mapping food weights to colors
food_colors = {1: RED, 2: BLUE, 3: GOLD}

# Snake settings
snake_pos = [100, 100]  
snake_body = [[100, 100], [80, 100], [60, 100]]
snake_direction = "RIGHT" 
change_to = snake_direction  
speed = 10  
game_score = 0 
Running = True
dot = 0  # for level progression

food_list = []  
def spawn_food():
 #Generates a new food item at a random position with a random weight.
    while True:
        x = random.randrange(0, WIDTH // 10) * 10
        y = random.randrange(0, HEIGHT // 10) * 10
        weight = random.choice([1, 2, 3])  # Random weight
        spawn_time = time.time()  # to remenber when food append
        new_food = [x, y, weight,spawn_time]  

        if new_food[:2] not in [food[:2] for food in food_list] and new_food[:2] not in snake_body:
            return new_food


def update_food():
    current_time = time.time()
    food_list[:] = [food for food in food_list if not (food[2] == 3 and current_time - food[3] > 100)] # after 100 sec gold disapiaring
#always 4 food 
    while len(food_list) < 4:
        food_list.append(spawn_food())


# Create initial food items
for _ in range(4):
    food_list.append(spawn_food())


while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False  # Exit game
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"

    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Insert the new position at the head of the snake
    snake_body.insert(0, list(snake_pos))

    # Check if the snake eats food
    for food in food_list[:]:  
        if snake_pos[:2] == food[:2]:  # Check if snake's head touches food
            game_score += food[2]  
            food_list.remove(food)  # Remove eaten food
            break
    else:
        snake_body.pop()  # Remove the tail if no food is eaten

    update_food() 

    # increase speed every 4 points
    if game_score % 4 == 0 and game_score != 0:
        if dot == 1:
            dot = 0
            speed+=5
    else:
        dot = 1

    screen.fill(BLACK) 

    # walls
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        Running = False  # Game over

    # Draw the snake
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))

    # Draw the food
    for food in food_list:
        pygame.draw.rect(screen, food_colors[food[2]], pygame.Rect(food[0], food[1], 10, 10))

    # Display the score and level
    game_score_text = font.render(f"Score: {game_score}", True, WHITE)
    screen.blit(game_score_text, (20, 20))
    game_level_text = font.render(f"Level: {game_score // 4}", True, WHITE)
    screen.blit(game_level_text, (400, 20))

    pygame.display.update()
    clock.tick(speed)  # Control game speed

# Game over screen
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()