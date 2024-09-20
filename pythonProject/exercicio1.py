import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 800
screen_height = 600
points = []

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL dos dudu')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

init_ortho()

def drawPoint(x, y, size):          ## FUNÇÃO PARA EXIBIR O PONTO
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def drawLine(point1, point2):      ## FUNÇÃO PARA EXIBIR A LINHA
    glBegin(GL_LINES)
    glVertex2i(point1[0], point1[1])    ## POINT1 E 2 USADO COMO PARÂMETRO PARA RECEBER A LOCALIZACAO
    glVertex2i(point2[0], point2[1])    ## ALOCADA NA LISTA POINTS
    glEnd()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                    ## condição para registrar a posicao do clique quando o usuario pressionar o botao do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos            ##obtem as coordenadas do clique
            y = screen_height - y       ### Inverte Y para corresponder ao sistema de coordenadas do OpenGL
            points.append((x, y))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1, 5, 0)
    ## LOOP PARA ACESSAR A LOCALIZAÇÃO ONDE O USUARIO CLICOU
    for point in points:          
        drawPoint(point[0], point[1], 15)     

    if len(points) >= 2:
        drawLine(points[0], points[1])    

    pygame.display.flip()
    pygame.time.wait(100)
    
pygame.quit()
