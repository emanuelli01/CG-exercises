import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Triângulosss")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

init_ortho()

def drawTriangle(vertices, tipo):       ## desenha os triangulos baseados no valor dos vertices e no tipo desejado
    if tipo == 1:
        glBegin(GL_TRIANGLES)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

    elif tipo == 2:
        glBegin(GL_LINE_LOOP)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

    elif tipo == 3:
        glPointSize(10)
        glBegin(GL_POINTS)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

    elif tipo == 4:
        glBegin(GL_TRIANGLES)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        glBegin(GL_LINE_LOOP)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

        glPointSize(10)
        glBegin(GL_POINTS)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()

tipo = 1

done = False
while not done:                     ## loop padrão pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:     ## condição para captar a tecla pressionada
            if event.key == pygame.K_1:
                tipo = 1
            elif event.key == pygame.K_2:
                tipo = 2
            elif event.key == pygame.K_3:
                tipo = 3
            elif event.key == pygame.K_4:
                tipo = 4

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.2, 0.3)
    triangle1_vertex = [(300, 200), (400, 200), (350, 300)]
    triangle2_vertex = [(500, 400), (600, 400), (550, 500)]
    drawTriangle(triangle1_vertex, tipo)
    drawTriangle(triangle2_vertex, tipo)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()