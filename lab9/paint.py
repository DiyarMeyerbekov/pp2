import pygame
import sys
import math

pygame.init()
width, height = 900, 600
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
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 5))

    def check_action(self, event):    # to check was the bottom pressed 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
#Constants
drawing = False
brush_color = black
circle_mode = False  # to stop drawing circle
circle_start = None
circle_radius = 0

rect_mode = False
rect_start = None
rect_width = 0
rect_height = 0
square_mode=False    
square_start=None

right_trian_mode=False
right_trian_start=None

eq_trian_mode=False
eq_trian_start=None

romb_mode=False
romb_start=None
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
    circle_mode = False  #off circle mode
def toggle_square_mode():
    global rect_mode,circle_mode,square_mode
    square_mode=not square_mode
    rect_mode=False
    circle_mode=False
def toggle_right_trian_mode():
    global rect_mode,circle_mode,square_mode,right_trian_mode
    right_trian_mode=not right_trian_mode
    square_mode=False
    rect_mode=False
    circle_mode=False
def toggle_eq_trian_mode():
    global rect_mode,circle_mode,square_mode,right_trian_mode,eq_trian_mode
    eq_trian_mode=not eq_trian_mode
    right_trian_mode=False
    square_mode=False
    rect_mode=False
    circle_mode=False
def toggle_romb_mode():
    global rect_mode,circle_mode,square_mode,right_trian_mode,eq_trian_mode,romb_mode
    romb_mode=not romb_mode
    eq_trian_mode=False
    right_trian_mode=False
    square_mode=False
    rect_mode=False
    circle_mode=False
buttons = [
    Button(0, 10, 50, 30, 'Black', black, set_black),
    Button(60, 10, 50, 30, 'Green', green, set_green),
    Button(120, 10, 50, 30, 'Red', red, set_red),
    Button(180, 10, 50, 30, 'Blue', blue, set_blue),
    Button(240, 10, 50, 30, 'Clear', gray, clear_screen),
    Button(300, 10, 50, 30, 'Exit', gray, exit_app),
    Button(360, 10, 60, 30, 'Circle', gray, toggle_circle_mode),
    Button(430, 10, 70, 30, 'Rectangle', blue, toggle_rect_mode),
    Button(510,10,70,30, 'Square',gray,toggle_square_mode),
    Button(590,10,80,30, 'Right trian.', red,toggle_right_trian_mode),
    Button(680,10,70,30,'eq. trian.',green,toggle_eq_trian_mode),
    Button(780,10,70,30,'Rhombus',black,toggle_romb_mode)
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
# 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:    # in rus когда нажата левая кнопка мыши провереятся какой мод включен
                if circle_mode:
                    circle_start = pygame.mouse.get_pos()
                    circle_radius = 0
                elif rect_mode:
                    rect_start = pygame.mouse.get_pos()
                    rect_width = rect_height = 0
                elif square_mode:
                    square_start=pygame.mouse.get_pos()
                elif right_trian_mode:
                    right_trian_start=pygame.mouse.get_pos()
                elif eq_trian_mode:
                    eq_trian_start=pygame.mouse.get_pos()
                elif romb_mode:
                    romb_start=pygame.mouse.get_pos()
                else:
                    drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:   # in rus когда отпускается левая кнопка мыши рисуется мод
                drawing = False
                if circle_mode and circle_start:
                    pygame.draw.circle(canvas, brush_color, circle_start, circle_radius, 2)
                    circle_start = None
                    circle_radius = 0

                if rect_mode and rect_start:
                    end_x, end_y = pygame.mouse.get_pos()      # in rus  находим 
                    min_x = min(rect_start[0], end_x)   # left top point when it start to draw
                    min_y = min(rect_start[1], end_y)
                    width = abs(rect_start[0] - end_x)
                    height = abs(rect_start[1] - end_y)
                    pygame.draw.rect(canvas, brush_color, (min_x, min_y, width, height), 2)    # 2 - толщина линии
                    rect_start = None

                if square_mode and square_start:
                    end_x, end_y=pygame.mouse.get_pos()
                    min_x = min(square_start[0], end_x)
                    min_y = min(square_start[1], end_y)
                    side=min(abs(square_start[0] - end_x), abs(square_start[1] - end_y))
                    pygame.draw.rect(canvas, brush_color, (min_x, min_y, side, side), 2)
                    square_start = None

                if right_trian_mode and right_trian_start:
                    end_x, end_y = pygame.mouse.get_pos()
                    p1=right_trian_start
                    p2=(end_x,right_trian_start[1])
                    p3=(right_trian_start[0],end_y)
                    pygame.draw.polygon(canvas, brush_color, [p1, p2, p3], 2)
                    right_trian_start=None
                if eq_trian_mode and eq_trian_start:
                    end_x,end_y=pygame.mouse.get_pos()
                    side = abs(end_x - eq_trian_start[0])
                    height = int((math.sqrt(3) / 2) * side)
                    point1 = (eq_trian_start[0], eq_trian_start[1])  
                    point2 = (eq_trian_start[0] + side, eq_trian_start[1])  
                    point3 = (eq_trian_start[0] + side // 2, eq_trian_start[1] - height)  
                    pygame.draw.polygon(canvas, brush_color, [point1, point2, point3], 2)
                    eq_trian_start= None
                if romb_mode and romb_start:
                    end_x,end_y=pygame.mouse.get_pos()
                    width = abs(end_x - romb_start[0])
                    height = abs(end_y - romb_start[1])
                    center_x = romb_start[0] + width // 2
                    center_y = romb_start[1] + height // 2
                    point1 = (center_x, romb_start[1])      
                    point2 = (romb_start[0], center_y)          
                    point3 = (center_x, romb_start[1] + height) 
                    point4 = (romb_start[0] + width, center_y)  
                    pygame.draw.polygon(canvas, brush_color, [point1, point2, point3, point4], 2)
                    romb_start = None

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