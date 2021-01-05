import pygame
from abc import ABCMeta, abstractmethod

pygame.init()
screen = pygame.display.set_mode((800,600), 0)

fonte = pygame.font.SysFont('arial', 24, True, False)
AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)
VELOCIDADE = 1
PARADO = 0

class ElementosJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass

class Cenario(ElementosJogo):
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]
    
    def pintar_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f"Score: {self.pontos}", True, AMARELO)
        tela.blit(img_pontos, (pontos_x, 50))
    
    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            pos_x = numero_coluna * self.tamanho
            pos_y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (pos_x, pos_y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (pos_x + half, pos_y+half),self.tamanho //10, 0)
    
    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)

    def calcular_regras(self):
        coluna_pac_quer_ir = self.pacman.coluna_intencao
        linha_pac_quer_ir = self.pacman.linha_intencao
        if 0 <= coluna_pac_quer_ir < 28 and 0 <= linha_pac_quer_ir < 29:
            if self.matriz[linha_pac_quer_ir][coluna_pac_quer_ir] !=2:
                self.pacman.aceitar_movimento()
                if self.matriz[linha_pac_quer_ir][coluna_pac_quer_ir] == 1:
                    self.pontos += 1
                    self.matriz[linha_pac_quer_ir][coluna_pac_quer_ir] = 0
    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

class Pacman(ElementosJogo):
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = int(self.tamanho/2)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
    
    def calcular_regras(self):
        self.coluna_intencao += self.velocidade_x
        self.linha_intencao += self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    
    def pintar (self, tela):
        #Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio)

        #Desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        #Desenho do Olho
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)
    
    def processar_eventos(self, eventos):
                #Captura os eventos
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -VELOCIDADE
                    
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = PARADO
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = PARADO
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = PARADO
                elif e.key == pygame.K_UP:
                    self.velocidade_y = PARADO
    def processar_eventos_mouse(self, eventos):
        delay = 30
        for e in eventos:
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x) / delay
                self.linha = (mouse_y - self.centro_y) / delay

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    
class Fantasma(ElementosJogo):
    def __init__(self, cor, tamanho):
        self.coluna = 6.0
        self.linha = 8.0
        self.cor = cor
        self.tamanho = tamanho

    
    def pintar(self, tela):
        fatia = self.tamanho // 8
        pixel_x = int(self.coluna * self.tamanho)
        pixel_y = int(self.linha * self.tamanho)
        contorno = [(pixel_x,  pixel_y + self.tamanho), 
                    (pixel_x + fatia,  pixel_y + fatia * 2),
                    (pixel_x + fatia * 3, pixel_y + fatia // 2),
                    (pixel_x + fatia * 3, pixel_y),
                    (pixel_x + fatia * 5, pixel_y),
                    (pixel_x + fatia * 6, pixel_y + fatia // 2),
                    (pixel_x + fatia * 7, pixel_y + fatia * 2),
                    (pixel_x + self.tamanho, pixel_y + self.tamanho)]
        pygame.draw.polygon(tela, self.cor, contorno, 0)
        olho_raio_externo = fatia
        olho_raio_interno = fatia // 2

        olho_esquerdo_x = int(pixel_x + fatia * 2.5)
        olho_esquerdo_y = int(pixel_y + fatia * 2.5)

        olho_direito_x = int(pixel_x + fatia * 5.5)
        olho_direito_y = int(pixel_y + fatia * 2.5)

        pygame.draw.circle(tela, BRANCO, (olho_esquerdo_x, olho_esquerdo_y), olho_raio_externo, 0)
        pygame.draw.circle(tela, PRETO, (olho_esquerdo_x, olho_esquerdo_y), olho_raio_interno, 0)

        pygame.draw.circle(tela, BRANCO, (olho_direito_x, olho_direito_y), olho_raio_externo, 0)
        pygame.draw.circle(tela, PRETO, (olho_direito_x, olho_direito_y), olho_raio_interno, 0)
    def calcular_regras(self):
        pass

    def processar_eventos(self, eventos):
        pass


if __name__ == "__main__":
    size= 600 // 30
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)
    blink = Fantasma(VERMELHO, size)
    # blink = Fantasma(size)
    # blink = Fantasma(size)
    # blink = Fantasma(size)


    while True:
        #Calcular as regras
        pacman.calcular_regras()
        cenario.calcular_regras()
        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        blink.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)
        
        #Captura os eventos
        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)