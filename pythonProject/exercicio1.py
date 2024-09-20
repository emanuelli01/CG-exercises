import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL da Galera junto com Python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 700, 0, 480)

done = False
init_ortho()

def draw_point(x, y):
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glEnd()

def draw_quads(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

print("Informe as coordenadas do primeiro ponto da linha:")
x1 = int(input("X1: ")) #100
y1 = int(input("Y1: ")) #100

print("Informe as coordenadas do segundo ponto da linha:")
x2 = int(input("X2: ")) #500
y2 = int(input("Y2: ")) #400

square_size = 100
square_x = 350
square_y = 240

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_point(231, 151)
    draw_line(x1, y1, x2, y2)
    draw_quads(300, 450, 400, 450, 400, 350, 300, 350)
    draw_triangle(200, 400, 250, 300, 150, 300)

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()