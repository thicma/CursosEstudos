import pygame
from abc import ABCMeta, abstractmethod
import random

pygame.init()
screen = pygame.display.set_mode((800,600), 0)
size= 600 // 30

fonte = pygame.font.SysFont('arial', 24, True, False)
AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)
LARANJA = (255, 140, 0)
ROSA = (255, 15, 192)
CIANO = (0, 255, 255)
VELOCIDADE = 1
PARADO = 0
ACIMA = 1
ABAIXO = 2
DIREITA = 3
ESQUERDA = 4


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


class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass
    
    @abstractmethod
    def esquina(self, direcoes):
        pass

class Cenario(ElementosJogo):
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.moviveis = []
        self.tamanho = tamanho
        self.pontos = 0
        #estado possiveis 0-Jogando 1-Pausado 2-GameOver 3-Ganhou
        self.estado = 0
        self.vidas = 1
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
        self.soma_total = self.pontos_totais(self.matriz)

    def pontos_totais(self, matriz):
        pontos = 0
        for num_linha, linha in enumerate(matriz):
            for ponto in linha:
                if ponto == 1:
                    pontos +=1
        return(pontos)

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)
    
    def pintar_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        img_pontos = fonte.render(f"Score: {self.pontos}", True, AMARELO)
        vidas_img = fonte.render(f'Vidas: {self.vidas}', True, AMARELO)
        tela.blit(img_pontos, (pontos_x, 50))
        tela.blit(vidas_img,(pontos_x, 100))
    
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
    
    def pintar_texto(self, tela, texto):
        texto_img = fonte.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img, (texto_x, texto_y))

    def pintar(self, tela):
        if self.estado == 0:
            self.pintar_jogando(tela)
        elif self.estado == 1:
            self.pintar_jogando(tela)
            self.pintar_texto_pausado(tela)
        elif self.estado == 2:
            self.pintar_jogando(tela)
            self.pintar_texto_game_over(tela)
        elif self.estado == 3:
            self.pintar_jogando(tela)
            self.pintar_vitoria(tela)

    def pintar_texto_pausado(self, tela):
        self.pintar_texto(tela, 'P A U S A D O')

    def pintar_texto_game_over(self,tela):
        self.pintar_texto(tela, 'G A M E  O V E R')

    def pintar_vitoria(self, tela):
        self.pintar_texto(tela, 'V I T Ó R I A \n JOGAR NOVAMENTE? S - SIM / N-NÃO')

    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)
        


    def calcular_regras(self):
        if self.estado == 0:
            self.calcular_regras_jogando()
        elif self.estado == 1:
            self.calcular_regras_pausado()
        elif self.estado == 2:
            self.calcular_regras_gameover()
        elif self.estado == 3:
            self.calcular_regras_vitoria()
    
    def calcular_regras_vitoria(self):
        pass

            

    
    def calcular_regras_gameover(self):
        pass
    
    def calcular_regras_pausado(self):
        pass

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            linha = int(movivel.linha)
            coluna = int(movivel.coluna)
            linha_intencao = int(movivel.linha_intencao)
            coluna_intencao = int(movivel.coluna_intencao)
            direcoes = self.get_direcoes(linha, coluna)


            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and movivel.linha == self.pacman.linha and movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <= 0:
                    self.estado = 2
                else:
                    self.pacman.linha_intencao = 1
                    self.pacman.coluna_intencao = 1                    
                         
            else:
                if 0 <= coluna_intencao < 28 and 0 <= linha_intencao < 29 and self.matriz[linha_intencao][coluna_intencao] != 2:
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman) and self.matriz[linha][coluna] == 1:
                        self.pontos += 1
                        self.matriz[linha][coluna] = 0
                else:
                    movivel.recusar_movimento(direcoes)
            if self.pontos == self.soma_total:
                self.estado = 3

    def processar_eventos(self, eventos):
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado == 0:
                        self.estado = 1
                    else:
                        self.estado = 0
                if e.key == pygame.K_s:
                    self.estado = 0

                    
    
    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha-1)][int(coluna)] !=2:
            direcoes.append(ACIMA)
        if self.matriz[int(linha+1)][int(coluna)] !=2:
            direcoes.append(ABAIXO)
        if self.matriz[int(linha)][int(coluna - 1)] !=2:
            direcoes.append(ESQUERDA)
        if self.matriz[int(linha)][int(coluna + 1)] !=2:
            direcoes.append(DIREITA)
        return direcoes

class Pacman(ElementosJogo, Movivel):
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
        self.abertura = 0
        self.velocidade_abertura = 1
    
    def calcular_regras(self):
        self.coluna_intencao += self.velocidade_x
        self.linha_intencao += self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

    
    def pintar (self, tela):
        #Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio)

        self.abertura += self.velocidade_abertura

        if self.abertura > self.raio:
            self.velocidade_abertura = -1
        if self.abertura <= 0:
            self.velocidade_abertura = 1

        #Desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.abertura)
        labio_inferior = (self.centro_x + self.raio, self.centro_y + self.abertura)
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

    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna 
    
    def esquina(self, direcoes):
        pass

    
class Fantasma(ElementosJogo, Movivel):
    def __init__(self, cor, tamanho):
        self.coluna = 15.0
        self.linha = 13.0
        self.cor = cor
        self.velocidade = 1
        self.direcao = ABAIXO
        self.tamanho = tamanho
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna

    
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
        if self.direcao == ACIMA:
            self.linha_intencao -= self.velocidade
        elif self.direcao == ABAIXO:
            self.linha_intencao += self.velocidade
        elif self.direcao == ESQUERDA:
            self.coluna_intencao -= self.velocidade
        elif self.direcao == DIREITA:
            self.coluna_intencao += self.velocidade

    def mudar_direcao(self, direcoes_possiveis):
        self.direcao = random.choice(direcoes_possiveis)
    
    def esquina(self,direcoes):
        self.mudar_direcao(direcoes)

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    
    def recusar_movimento(self, direcoes_possiveis):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes_possiveis)

    def processar_eventos(self, eventos):
        pass

class Jogando:
    def __init__(self):
        self.iniciar(size)

    def iniciar(self, size):
        self.pacman = Pacman(size)
        self.blink = Fantasma(VERMELHO, size)
        self.inky = Fantasma(CIANO, size)
        self.clayde = Fantasma(LARANJA, size)
        self.pinky = Fantasma(ROSA, size)
        self.cenario = Cenario(size, self.pacman)
        self.cenario.adicionar_movivel(self.pacman)
        self.cenario.adicionar_movivel(self.blink)
        self.cenario.adicionar_movivel(self.inky)
        self.cenario.adicionar_movivel(self.clayde)
        self.cenario.adicionar_movivel(self.pinky)

        while True:
            #Calcular as regras
            self.pacman.calcular_regras()
            self.cenario.calcular_regras()
            self.blink.calcular_regras()
            self.inky.calcular_regras()
            self.clayde.calcular_regras()
            self.pinky.calcular_regras()
            # Pintar a tela
            screen.fill(PRETO)
            self.cenario.pintar(screen)
            self.pacman.pintar(screen)
            self.blink.pintar(screen)
            self.inky.pintar(screen)
            self.clayde.pintar(screen)
            self.pinky.pintar(screen)
            pygame.display.update()
            pygame.time.delay(100)
            
            #Captura os eventos
            eventos = pygame.event.get()
            self.pacman.processar_eventos(eventos)
            self.cenario.processar_eventos(eventos)

if __name__ == "__main__":
    jogando = Jogando()
    # pacman = Pacman(size)
    # blink = Fantasma(VERMELHO, size)
    # inky = Fantasma(CIANO, size)
    # clayde = Fantasma(LARANJA, size)
    # pinky = Fantasma(ROSA, size)
    # cenario = Cenario(size, pacman)
    # cenario.adicionar_movivel(pacman)
    # cenario.adicionar_movivel(blink)
    # cenario.adicionar_movivel(inky)
    # cenario.adicionar_movivel(clayde)
    # cenario.adicionar_movivel(pinky)



    # while True:
    #     #Calcular as regras
    #     pacman.calcular_regras()
    #     cenario.calcular_regras()
    #     blink.calcular_regras()
    #     inky.calcular_regras()
    #     clayde.calcular_regras()
    #     pinky.calcular_regras()
    #     # Pintar a tela
    #     screen.fill(PRETO)
    #     cenario.pintar(screen)
    #     pacman.pintar(screen)
    #     blink.pintar(screen)
    #     inky.pintar(screen)
    #     clayde.pintar(screen)
    #     pinky.pintar(screen)
    #     pygame.display.update()
    #     pygame.time.delay(100)
        
    #     #Captura os eventos
    #     eventos = pygame.event.get()
    # pacman.processar_eventos(eventos)
    for e in eventos:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_s:
                jogando.iniciar()
            elif e.key == pygame.K_s:
                exit()
    #     cenario.processar_eventos(eventos)