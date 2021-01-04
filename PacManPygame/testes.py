import pygame

pygame.init()
screen = pygame.display.set_mode((800,600), 0)
AMARELO = (255,255,0)
PRETO = (0,0,0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 100
        self.raio = int(self.tamanho/2)
    
    def pintar (self, tela):
        #Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio)

        #Desenho da boca
        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)

        #Desenho do Olho



if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # Pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
