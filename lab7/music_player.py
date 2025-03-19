import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Music player")
songs = [r'maskoff.mp3', r'nights.mp3']
pygame.mixer.music.load(songs[0])
play=False
font = pygame.font.Font(None, 18)
BLACK=(0,0,0)
def next_song():
    global songs,play
    songs=songs[1:]+[songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
    play=True
running=True
while running:
     screen.fill((255, 255, 255))
     t = font.render("previous - press left, play/stop-space, next-rigth", True, BLACK)
     screen.blit(t, (100,300))
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                songs=songs[-1:]+songs[-1:]
                pygame.mixer.music.load(songs[0])
                pygame.mixer.music.play()
            elif event.key==pygame.K_RIGHT:
                next_song()
            elif event.key==pygame.K_SPACE:
                if play:
                    pygame.mixer.music.pause()
                    play=False
                else:
                    pygame.mixer.music.play()
                    play=True
     pygame.display.flip()
pygame.quit()