import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Reflexão de Formas Geométricas")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -300, 300)

# Função para desenhar um triângulo
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(-100, 0)
    glVertex2f(100, 0)
    glVertex2f(0, 150)
    glEnd()

# Função para desenhar um círculo
def draw_circle():
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        theta = 2.0 * math.pi * i / 360  # Ângulo
        x = 50 * math.cos(theta)  # Coordenada X
        y = 50 * math.sin(theta)  # Coordenada Y
        glVertex2f(x, y)
    glEnd()

# Função para desenhar um quadrado
def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

init_ortho()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Desenha o triângulo e aplica a reflexão no eixo X
    glPushMatrix()
    glTranslatef(-200, 0, 0)
    draw_triangle()
    glScalef(1, -1, 1)
    draw_triangle()
    glPopMatrix()

    # Desenha o círculo e aplica a reflexão no eixo Y
    glPushMatrix()
    glTranslatef(0, 0, 0)
    draw_circle()
    glScalef(-1, 1, 1)
    draw_circle()
    glPopMatrix()

    # Desenha o quadrado e aplica a reflexão nos dois eixos
    glPushMatrix()
    glTranslatef(200, 0, 0)
    draw_square()
    glScalef(-1, -1, 1)
    draw_square()
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()