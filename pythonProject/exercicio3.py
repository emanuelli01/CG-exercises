import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Transformações de um Triângulo')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-10, 10, -10, 10)

init_ortho()

# Variáveis de transformação
translate_x = 0.0
translate_y = 0.0
scale_factor = 1.0
rotation_angle = 0.0

def draw_triangle(): # Função para desenhar um triângulo retângulo
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)  # Vértice na origem
    glVertex2f(1.0, 0.0)  # Vértice no eixo X
    glVertex2f(0.0, 1.0)  # Vértice no eixo Y
    glEnd()

def apply_transformations(): # Função para aplicar as transformações de rotação, translação e escala
    glTranslatef(translate_x, translate_y, 0.0)
    glScalef(scale_factor, scale_factor, 1.0)
    glRotatef(rotation_angle, 0.0, 0.0, 1.0)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: # Verifica as teclas pressionadas para as rotações
            if event.key == pygame.K_LEFT:
                translate_x -= 0.5
            if event.key == pygame.K_RIGHT:
                translate_x += 0.5
            if event.key == pygame.K_UP:
                translate_y += 0.5
            if event.key == pygame.K_DOWN:
                translate_y -= 0.5
            if event.key == pygame.K_w:
                scale_factor += 0.1
            if event.key == pygame.K_s:
                scale_factor -= 0.1
            if event.key == pygame.K_a:
                rotation_angle += 5
            if event.key == pygame.K_d:
                rotation_angle -= 5

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    apply_transformations()
    draw_triangle()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()