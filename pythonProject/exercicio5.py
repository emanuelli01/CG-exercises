import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Reflexões")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)  # Coordenadas centradas
    glMatrixMode(GL_MODELVIEW)

init_ortho()

def drawTriangle(vertices):
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def drawCircle(center, radius, num_segments):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(center[0] + x, center[1] + y)
    glEnd()

def drawSquare(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    triangle_vertices = [(0, 100), (-100, -100), (100, -100)]
    drawTriangle(triangle_vertices)


    glPushMatrix()              ## salva a matriz de projeçao atual
    glScalef(1, -1, 1)      ## muda a matriz de projecao para refletir o poligono
    drawTriangle(triangle_vertices)
    glPopMatrix()               ## reestabelece a matriz de projecao


    glColor3f(0.0, 1.0, 0.0)
    drawCircle((200, 0), 50, 100)


    glPushMatrix()
    glScalef(-1, 1, 1)  # Reflexão no eixo Y
    drawCircle((200, 0), 50, 100)
    glPopMatrix()


    glColor3f(0.0, 0.0, 1.0)
    square_vertices = [(-50 + 100, -50 + 100), (50 + 100, -50 + 100), (50 + 100, 50 + 100), (-50 + 100, 50 + 100)]
    drawSquare(square_vertices)
    glPushMatrix()
    glScalef(-1, -1, 1)
    drawSquare(square_vertices)
    glPopMatrix()


    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()