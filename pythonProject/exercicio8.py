import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exercicio 8")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

init_ortho()

def drawSquare(x, y, side, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_QUADS)
    glVertex2i(x, y)
    glVertex2i(x + side, y)
    glVertex2i(x + side, y + side)
    glVertex2i(x, y + side)
    glEnd()

x, y = 0, 0
side = 50
espaco = 1
linhas = 5
colunas = 5

colors = [(1, 0, 0),
          (0, 1, 0),
          (0, 0, 1),
          (1, 1, 0),
          (1, 0, 1)]

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for linha in range(linhas):
        for coluna in range(colunas):
            x = linha * (side + espaco)
            y = coluna * (side + espaco)
            color = colors[(linha + coluna) % 5]

            drawSquare(x, y, side, color)


    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()