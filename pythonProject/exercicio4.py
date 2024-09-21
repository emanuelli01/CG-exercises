import pygame
from OpenGL.raw.GL.NV.path_rendering import GL_SQUARE_NV
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

def drawSquare(vertices):               ## funcao para exibir o quadrado baseado nos vertices
    glBegin(GL_QUADS)
    for vertex in vertices:             ## percorre todos os vertices, capturando x e y
        glVertex2f(vertex[0], vertex[1])
    glEnd()

x, y = 0, 0                     ## define a posicao do quadrado
side_length = 100     ## definido o tamanho dos lados do quadrado, desta forma fica mais facil de alocar as coordenadas
move_speed = 10

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()         ## funcao para alocar a tecla pressionada
    if keys[K_UP] or keys[K_w]:
        y += move_speed
    if keys[K_DOWN] or keys[K_s]:
        y -= move_speed
    if keys[K_LEFT] or keys[K_a]:
        x -= move_speed
    if keys[K_RIGHT] or keys[K_d]:
        x += move_speed

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    vertexSquare = [(x, y),         ## posicao inicial
                    (x + side_length, y),     ## no vertice 2, a coordenada de x recebe + 100 pixels
                    (x + side_length, y + side_length),
                    (x, y + side_length)]

    drawSquare(vertexSquare)

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()