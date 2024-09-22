import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

init_ortho()

def drawTriangle(vertices):
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def drawSquare(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

def drawLine(vertices):
    glBegin(GL_LINES)
    for vertex in vertices:
        glVertex2i(vertex[0], vertex[1])
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

    glColor3f(0, 0, 1)          ## CHAO
    chao = [(0, 0), (0, 70), (800, 70), (800, 0)]
    drawSquare(chao)

    glColor(255, 255, 0)                ## SOL
    drawCircle((150, 500), 50, 100)

    glColor3f(1, 1, 1)
    drawCircle((400, 130), 75, 100) ##CORPO
    drawCircle((400, 250), 50,100)  ##CORPO 2
    drawCircle((400, 330), 35, 100) ##CABECA

    glColor3f(0.5, 0.25, 0)
    drawLine([(350, 250), (300, 230)])  ##BRACO ESQUERDO
    drawLine([(450, 250), (500, 270)])

    glColor3f(0, 0, 0)
    drawSquare([(390, 340), (390, 345), (395, 345), (395, 340)])   ##OLHO ESQUERDO
    drawSquare([(410, 340), (410, 345), (415, 345), (415, 340)])   ## DIREITO

    glColor3f(0, 0, 0)
    drawCircle((400, 240), 5, 20)       ##BOTOES
    drawCircle((400, 210), 5, 20)
    drawCircle((400, 180), 5, 20)

    glColor3f(1, 0.5, 0)
    drawTriangle([(400, 330), (400, 320), (430, 325)])  ##NARIZ

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()