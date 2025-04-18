import pygame 
import sys 
import random 
import psycopg2 

pygame.init() 
 
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 
 
snake_pos = [[100, 50], [90, 50], [80, 50]] 
snake_speed = [10, 0] 
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0} 
food_spawn = True 
score = 0 
level = 1 
speed_increase = 0.1 
food_counter = 0   
score_saved = False 
last_direction = [10, 0]  # начальное направление движения
conn = psycopg2.connect(host="localhost", dbname = "suppliers", user = "postgres", password = "110906", port = 5432)
 
fps = pygame.time.Clock() 
paused = False 
running=True


def get_top_scores(limit=5):
    conn = psycopg2.connect(dbname='suppliers', user='postgres', password='110906', host='localhost', port='5432') 
    cur = conn.cursor()
    cur.execute("SELECT player_name, score, level FROM snake_game_scores ORDER BY score DESC LIMIT %s", (limit,))
    scores = cur.fetchall()
    cur.close()
    conn.close()
    return scores

def ex():
    global running
    running = False

    insert_score(player_name, score, level)

    print(f"\n Game Over! Your score: {score}, Level: {level}")

    print("\n Top 5 scores:")
    top_scores = get_top_scores()
    for i, (name, s, lvl) in enumerate(top_scores, start=1):
        print(f"{i}. {name} - Score: {s}, Level: {lvl}")




def insert_score(name, score, level): 
    conn = psycopg2.connect(dbname='suppliers', user='postgres', password='110906', host='localhost', port='5432') 
    cur = conn.cursor()

    # Проверка существования
    check_query = "SELECT 1 FROM snake_game_scores WHERE player_name = %s AND score = %s AND level = %s"
    cur.execute(check_query, (name, score, level))
    exists = cur.fetchone()

    if not exists:
        insert_query = "INSERT INTO snake_game_scores (player_name, score, level) VALUES (%s, %s, %s)"
        cur.execute(insert_query, (name, score, level))
        conn.commit()

    cur.close()
    conn.close()


 
def get_scores(name): 
    conn = psycopg2.connect(dbname='suppliers', user='postgres', password='110906', host='localhost', port='5432') 
    cur = conn.cursor() 
    query = "SELECT score, level FROM snake_game_scores WHERE player_name = %s ORDER BY score DESC" 
    cur.execute(query, (name,)) 
    results = cur.fetchall() 
    cur.close() 
    conn.close() 
    return results

 
def create_table():
    conn = psycopg2.connect(dbname='suppliers', user='postgres', password='110906', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS snake_game_scores (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100),
            score INTEGER,
            level INTEGER
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table()

player_name = input("Enter your name: ") 
player_name = player_name.encode('utf-8', 'ignore').decode('utf-8') 
scores = get_scores(player_name) 
if scores: 
    print("Your previous scores:") 
    for score, level in scores: 
        print(f"Score: {score}, Level: {level}") 
    sys.exit()   
 
def check_collision(pos): 
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10: 
        return True 
    if pos in snake_pos[1:]: 
        return True 
    return False 
 
def get_random_food(): 
    global food_counter 
    while True: 
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10] 
        if pos not in snake_pos: 
            weight = 2 if food_counter >= 2 else 1 
            food_counter = 0 if weight == 2 else food_counter + 1 
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()} 
 
try: 
    while running ==True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                if not score_saved:
                    insert_score(player_name, score, level)
                    score_saved = True
                ex()

                
            # Внутри игрового цикла, в блоке обработки событий:
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and last_direction != [0, 10]:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and last_direction != [0, -10]:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and last_direction != [10, 0]:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and last_direction != [-10, 0]:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused

 
 
        if not paused:
            snake_pos.insert(0, list(map(lambda x, y: x + y, snake_pos[0], snake_speed)))
            last_direction = snake_speed[:]  # Сохраняем направление

 
            if check_collision(snake_pos[0]):
                if not score_saved:
                    insert_score(player_name, score, level)
                    score_saved = True
                ex()

 
            if snake_pos[0] == food['pos']: 
                score += food['weight'] 
                if score % 3 == 0: 
                    level += 1 
                    fps.tick(10 + level * speed_increase) 
                food_spawn = True 
            else: 
                snake_pos.pop() 
 
            if food_spawn: 
                food = get_random_food() 
                food_spawn = False 
 
            current_time = pygame.time.get_ticks() 
            if current_time - food['spawn_time'] > 10000: 
                food_spawn = True 
 
        screen.fill(BLACK) 
        for pos in snake_pos: 
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)) 
 
        food_color = RED if food['weight'] == 1 else (255, 165, 0) 
        pygame.draw.rect(screen, food_color,
        pygame.Rect(food['pos'][0], food['pos'][1], 10, 10)) 
 
        font = pygame.font.SysFont('arial', 20) 
        score_text = font.render(f"Score: {score} Level: {level}", True, WHITE) 
        screen.blit(score_text, [0, 0]) 
 
        if paused: 
            pause_text = font.render("Paused", True, WHITE) 
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2]) 
 
        pygame.display.flip() 
        fps.tick(10 + level * speed_increase) 
    cur = conn.cursor()
    cur.execute("SELECT * FROM snake_game_scores;")
    rows = cur.fetchall()

    print("\nTop scores:")
    for row in rows:
      print(f"ID: {row[0]}, Name: {row[1]}, Score: {row[2]}, Level: {row[3]}")

    
    dele = input("to clear all data print 'del': ")
    if dele == "del":
        conn = psycopg2.connect(dbname='suppliers', user='postgres', password='110906', host='localhost', port='5432')
        cur = conn.cursor()
        
        cur.execute("DELETE FROM snake_game_scores")  # Удалит все строки
        cur.execute("TRUNCATE TABLE snake_game_scores RESTART IDENTITY") # удалить ID
        conn.commit()
        
        cur.close()
        conn.close()
except SystemExit: 
    pygame.quit()