import pygame                           #importa o módulo game
import random                           #importa o módulo random
from pygame.locals import *             #faz usar o teclado

def on_grid_random():                   #add grid uniforme 10x10px
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10) # divisão por nº inteiro com o uso da barra //

def collision(c1, c2):                  #faz comer a comida
    return abs(c1[0] - c2[0]) < 10 and abs(c1[1] - c2[1]) < 10

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))    #tamanho da tela
pygame.display.set_caption('Cobra do Diego - aprendendo Python')  #nome do jogo

cobra = [(200,200),(210,200),(220,200)] #tamanho do crescimento da cobra
cobra_skin = pygame.Surface((10,10))    #tamanho da cobra
cobra_skin.fill((0,255,0))              #cor da cobra

comida_pos = on_grid_random()           #posição aleatória dentro da tela
comida = pygame.Surface((10,10))
comida.fill((255,0,0))                  #fill = cor do objeto

direcao = LEFT                          #faz andar

clock = pygame.time.Clock()             #velocidade do FPS na tela

comendo = False                         #ato de comer a comida

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_RIGHT:
                direcao = RIGHT
            if event.key == K_LEFT:
                direcao = LEFT

    if collision(cobra[0], comida_pos):     #come e cresce
        comendo = True
        comida_pos = on_grid_random()
        cobra.append((0,0))

    

    for i in range(len(cobra) -1, 0, -1):   #faz andar
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if direcao == UP:                       #faz obedecer as setas direcionais
        cobra[0] = (cobra[0][0], cobra[0][1] -10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] +10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] +10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] -10, cobra[0][1])


    if cobra[0][0] < 0:                    #faz a cobra não desaparece
        cobra[0] = (600, cobra[0][1])
    elif cobra[0][0] >= 600:
        cobra[0] = (0, cobra[0][1])
    elif cobra[0][1] < 0:
        cobra[0] = (cobra[0][0], 600)
    elif cobra[0][1] >= 600:
        cobra[0] = (cobra[0][0], 0)

    screen.fill((0, 0, 0))                  #cor da tela
    screen.blit(comida, comida_pos)         #faz aparecer a comida
    
    for pos in cobra:
        screen.blit(cobra_skin, pos)        #faz aparecer a cobra

    pygame.display.update()