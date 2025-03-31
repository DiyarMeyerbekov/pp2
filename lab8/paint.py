import pygame
import sys
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint')
#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

canvas = pygame.Surface((width, height))
canvas.fill(white)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
#Constants
drawing = False
brush_color = black
circle_mode = False
circle_start = None
circle_radius = 0

rect_mode = False
rect_start = None
rect_width = 0
rect_height = 0
#functions for buttons
def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def clear_screen():
    canvas.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

def toggle_circle_mode():
    global circle_mode, rect_mode
    circle_mode = not circle_mode
    rect_mode = False 

def toggle_rect_mode():
    global rect_mode, circle_mode
    rect_mode = not rect_mode
    circle_mode = False  

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(160, 10, 60, 30, 'Red', red, set_red),
    Button(230, 10, 60, 30, 'Blue', blue, set_blue),
    Button(300, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(390, 10, 60, 30, 'Exit', gray, exit_app),
    Button(460, 10, 80, 30, 'Circle', gray, toggle_circle_mode),
    Button(560, 10, 100, 30, 'Rectangle', blue, toggle_rect_mode)
]

while True:
    screen.fill(white)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for button in buttons:
            button.check_action(event)
#активаци режима рисования 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode:
                    circle_start = pygame.mouse.get_pos()
                    circle_radius = 0
                elif rect_mode:
                    rect_start = pygame.mouse.get_pos()
                    rect_width = rect_height = 0
                else:
                    drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if circle_mode and circle_start:
                    pygame.draw.circle(canvas, brush_color, circle_start, circle_radius, 2)
                    circle_start = None
                    circle_radius = 0
                if rect_mode and rect_start:
                    end_x, end_y = pygame.mouse.get_pos()
                    min_x = min(rect_start[0], end_x)
                    min_y = min(rect_start[1], end_y)
                    width = abs(rect_start[0] - end_x)
                    height = abs(rect_start[1] - end_y)
                    pygame.draw.rect(canvas, brush_color, (min_x, min_y, width, height), 2)
                    rect_start = None

        if event.type == pygame.MOUSEMOTION:
            if circle_mode and circle_start:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                circle_radius = int(math.dist(circle_start, (mouse_x, mouse_y)))
            if rect_mode and rect_start:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                rect_width = abs(rect_start[0] - mouse_x)
                rect_height = abs(rect_start[1] - mouse_y)
            # Drawing the circle on the position where mouse were clicked

    if drawing and not circle_mode and not rect_mode:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:
            pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y), 5)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
