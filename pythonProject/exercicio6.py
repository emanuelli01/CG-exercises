import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

screen_size = (800, 600)
pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Ex6")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

init_ortho()

def drawSquare(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

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

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glColor3f(1.0, 0.5, 1)
    squareVertex = [(300, 150), (300, 300), (450, 300), (450, 150)]
    drawSquare(squareVertex)

    glColor3f(1.0, 0.5, 0.5)
    triangleVertex = [(375, 400), (300, 300), (450, 300)]
    drawTriangle(triangleVertex)

    glColor3f(0.5, 0.5, 0.2)
    squareVertex2 = [(370, 150), (370, 200), (420, 200), (420, 150)]
    drawSquare(squareVertex2)

    glColor3f(0.0, 1.0, 0.0)
    drawCircle((350, 250), 20, 100)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()