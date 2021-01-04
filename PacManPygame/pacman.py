import pygame

AMARELO = (255,255,0)
PRETO = (0,0,0)
VELOCIDADE = 1
RAIO = 30
pygame.init()


tela = pygame.display.set_mode((640,480), 0)
movimento_eixo_x = 10
movimento_eixo_y = 30
velocidade_x = VELOCIDADE
velocidade_y = VELOCIDADE
while True:

    #Calcula as regras
    movimento_eixo_x += velocidade_x
    movimento_eixo_y += velocidade_y
    if movimento_eixo_x + RAIO > 640:
        velocidade_x = -VELOCIDADE
    if movimento_eixo_x - RAIO < 0:
        velocidade_x = VELOCIDADE
    if movimento_eixo_y + RAIO > 480:
        velocidade_y = -VELOCIDADE
    if movimento_eixo_y - RAIO < 0:
        velocidade_y = VELOCIDADE




    #Pinta a tela      TELA,  COR    POS OBJ  RAIO ESPESSURA do desenho
    tela.fill(PRETO)
    pygame.draw.circle(tela,AMARELO,(int(movimento_eixo_x),int(movimento_eixo_y)), RAIO, 0)
    pygame.display.update()
    #Captura os eventos do usuario

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()



