import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    triangleVertex = [(300, 200),
                      (400, 200),
                      (350, 300)]
    rVertex = triangleVertex
    for x in rVertex:
        x[0] *= -1

    drawTriangle(rVertex)
    drawTriangle(triangleVertex)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()