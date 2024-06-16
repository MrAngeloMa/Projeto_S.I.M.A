# Estrutura.py

import pygame
from MapaT import *
from BotPlayerT import *

# Definindo o player
player = Player(50, 480, 20)

# Densidade Demográfica - quanitdade de pessoas na sala
def DDemo(Largura, Altura, Dist):
    NMax = ((Largura* Altura)//(Dist*2))//375 # Número máximo de pessoas
    if NMax == 0:
        NMax = 1
    return(NMax)

# Define valores: largura e altura da sala, distanciamento, quantidade de pessoas
def Valores(): # 1m = 16p
    largura = int(input("Informe o comprimento da sala em metro: "))*16
    while largura < 90 or largura > 560:
        largura = int(input("Insira um valor entre 9m e 56m: "))*16

    altura = int(input("Informe a largura da sala em metro: "))*16
    while altura < 150 or altura > 350:
        altura = int(input("Insira um valor entre 15m e 35m: "))*16

    Dist = float(input("Informe o distânciamento desejado em metro: "))*16
    while Dist < 5 or Dist > 25:
        Dist = int(input("Insira um valor entre 0,5m e 2,5m: "))*16

    NMax = DDemo(largura, altura, Dist)
    
    NBot = int(input("Informe o número de pessoas dentro da sala: "))
    while NBot > NMax or NBot < 1:
        NBot = int(input(f"Deve-se conter pelo menos uma pessoa e no máximo {NMax} : "))

    return[largura, altura, NBot, Dist, NMax]

# Cria Salas e Bots (Mudou as posições)
def CriaMapa(player):
    modo = int(input("Utilizar salas prontas? (Sim = 1/Não = 0) "))
    TBots = []
    TMapas = []
    TSalas = []
    ##

    if modo == 0:
        NMapa = int(input("Informe o número de salas: "))
        for n in range(1, NMapa+1):
            xcorredor = 25
            ycorredor = 410
            if n == 1 and NMapa > 1:
                mapa = Mapa(50, 50, n)
                largura, altura, NBot, Dist, NMax  = Valores()
                salax = 700 - (largura/2)
                salay = ycorredor - altura - 15
                sala = Sala(salax, salay, largura, altura)
                sala.nmax = NMax
                mapa.addSala(sala)

                corredor = Corredor(xcorredor, ycorredor, 1150, 150)
                mapa.addCorredor(corredor)
                corredor.addPorta(Porta(1150, 0, 25, 150, 2))
                ListaB = ListaBot(NBot, Dist, sala)
                player.dist = Dist
                TBots.append(ListaB)
                TMapas.append(mapa)
                TSalas.append(sala)

            elif n == 1 and NMapa == 1:
                mapa = Mapa(50, 50, n)
                largura, altura, NBot, Dist, NMax  = Valores()
                salax = 700 - (largura/2)
                salay = ycorredor - altura - 15
                sala = Sala(salax, salay, largura, altura)
                sala.nmax = NMax
                mapa.addSala(sala)

                corredor = Corredor(xcorredor, ycorredor, 1150, 150)
                mapa.addCorredor(corredor)
                ListaB = ListaBot(NBot, Dist, sala)
                player.dist = Dist
                TBots.append(ListaB)
                TMapas.append(mapa)
                TSalas.append(sala)
                
            elif n > 1 and n < NMapa and NMapa != 1:
                mapa = Mapa(1200 - player.x, 600 - player.y, n)
                largura, altura, NBot, Dist, NMax  = Valores()
                salax = 700 - (largura/2)
                salay = ycorredor - altura - 15
                sala = Sala(salax, salay, largura, altura)
                sala.nmax = NMax
                mapa.addSala(sala)

                corredor = Corredor(xcorredor, ycorredor, 1150, 150)
                mapa.addCorredor(corredor)
                corredor.addPorta(Porta(-25, 0, 25, 150, n - 1))
                corredor.addPorta(Porta(1150, 0, 25, 150, n + 1))
                ListaB = ListaBot(NBot, Dist, sala)
                player.dist = Dist
                TBots.append(ListaB)
                TMapas.append(mapa)
                TSalas.append(sala)
                
            elif n == NMapa:
                mapa = Mapa(1200 - player.x, 600 - player.y, n)
                largura, altura, NBot, Dist, NMax  = Valores()
                salax = 700 - (largura/2)
                salay = ycorredor - altura - 15
                sala = Sala(salax, salay, largura, altura)
                sala.nmax = NMax
                mapa.addSala(sala)

                corredor = Corredor(xcorredor, ycorredor, 1150, 150)
                mapa.addCorredor(corredor)
                corredor.addPorta(Porta(-25, 0, 25, 150, n - 1))
                ListaB = ListaBot(NBot, Dist, sala)
                player.dist = Dist
                TBots.append(ListaB)
                TMapas.append(mapa)
                TSalas.append(sala)
            
    elif modo == 1:
        player.dist = 15
        mapa_1 = Mapa(50, 50, 1)                              # Cria mapa 1
        sala_1_mapa_1 = Sala(250, 45, 900, 350)               # Cria Sala 1 
        mapa_1.addSala(sala_1_mapa_1)                         # Add Sala 1 no mapa 1
        sala_1_mapa_1.nmax = 15

        corredor_1_mapa_1 = Corredor(25, 410, 1150, 150)      # Cria corredor 1
        mapa_1.addCorredor(corredor_1_mapa_1)                 # Add corredor 1 no mapa 1

        corredor_1_mapa_1.addPorta(Porta(1150, 0, 25, 150, 2)) # Add Porta para o mapa 2 no mapa 1

        #############################

        mapa_2 = Mapa(1200 - player.x, 600 - player.y, 2)
        corredor_1_mapa_2 = Corredor(25, 410, 1150, 150)
        corredor_1_mapa_2.addPorta(Porta(-25, 0, 25, 150, 1))
        corredor_1_mapa_2.addPorta(Porta(1150, 0, 25, 150, 3))

        mapa_2.addCorredor(corredor_1_mapa_2)
        sala_1_mapa_2 = Sala(250, 45, 600, 350)
        mapa_2.addSala(sala_1_mapa_2)
        sala_1_mapa_2.nmax = 15

        #############################

        mapa_3 = Mapa(1000 - player.x, 600 - player.y, 3)
        corredor_1_mapa_3 = Corredor(25, 410, 1150, 150)
        corredor_1_mapa_3.addPorta(Porta(-25, 0, 25, 150, 2))

        mapa_3.addCorredor(corredor_1_mapa_3)
        sala_1_mapa_3 = Sala(250, 45, 750, 350)
        sala_1_mapa_3.nmax = 15
        mapa_3.addSala(sala_1_mapa_3)

        ##############   Listas   #############

        ListaB1 = ListaBot(15, 15, sala_1_mapa_1)
        ListaB2 = ListaBot(10, 15, sala_1_mapa_2)
        ListaB3 = ListaBot(4, 15, sala_1_mapa_3)

        TBots = [ListaB1, ListaB2, ListaB3]                    # Lista com todas as listas de bots
        TMapas = [mapa_1, mapa_2, mapa_3]                      # Lista com todos os mapas
        TSalas = [sala_1_mapa_1, sala_1_mapa_2, sala_1_mapa_3] # Lista com todos as salas
    
    return[TBots, TMapas, TSalas]

# Executa a estrutura do programa com os valores estabelecidos
def Estrutura(TMapas, TBots, TSalas, player):
    class SIMA():
        def __init__(self, screenSize = (1200, 600), fps=60, title='S.I.M.A', icon=None):
            
            self.SimaRunning = True
            self.screenSize = screenSize
            self.title = title
            self.icon = icon
            self.fps = fps
            
            self.initSima()

            self.mapa_atual = TMapas[0]
            self.bot_atual = TBots[0]
            self.sala_atual = TSalas[0]
            
        def initSima(self):
            # Define a Tela, fonte e "relógio" da simulação
            self.screen = pygame.display.set_mode(self.screenSize)

            pygame.display.set_caption(self.title)

            if(self.icon != None):
                pygame.display.set_icon(self.icon)
            
            pygame.font.init()

            self.start = False

            self.SimaClock = pygame.time.Clock()
            self.SimaFont = pygame.font.SysFont('Arial', 25)

        def SimaMain(self):
            # Limpa/ atualiza a tela, marca o tempo e realiza as etapas da simulação
            while self.SimaRunning:
                self.deltaTime = self.SimaClock.tick(self.fps)

                for event in pygame.event.get():
                    self.SimaEvent(event)
                self.SimaUpdate()
                self.SimaRender()

                pygame.display.update()

            pygame.display.quit()   

        def SimaEvent(self, event):     
            # Verifica se o "QUIT" ou "ESC" foram precionados, se sim, fecha a simulação
            if(event.type == pygame.QUIT):
                self.SimaRunning = False
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.SimaRunning = False

        def SimaUpdate(self):
            # Retorna a tecla precionada
            keys = pygame.key.get_pressed()
            
            # Muda o Mapa atual
            self.mapa_atual, self.bot_atual, self.sala_atual = MudaMapa(player, self.mapa_atual, self.bot_atual, self.sala_atual, TMapas, TBots, TSalas)

            # Nº de pessoas na sala
            self.NP = NPessoas(self.bot_atual, player, self.sala_atual)

            # Atualiza os Bots que estão na tela
            Atualiza(self.bot_atual, self.sala_atual, self.deltaTime, player, keys, self.screen)

        def SimaRender(self):
            # Limpa a Tela
            self.screen.fill((70,130,180))

            # Desenha o mapa atual com suas salas e corredores
            DesenhaMapa(self.mapa_atual, self.screen)

            # Porta Fake
            pygame.draw.rect(self.screen, (210, 180, 140) ,(((self.sala_atual.x + (self.sala_atual.largura/2)))-75, 395, 150, 15))

            # Desenha os bots atuais
            DesenhaBots(self.bot_atual, self.screen)
                
            # Desenhando personagem
            pygame.draw.circle(self.screen, player.color, (player.x, player.y), player.raio)

            # Mostra o nº de pessoas na sala
            N = self.SimaFont.render(f'Nº de pessoas na sala: {self.NP}', True, (255, 255, 255))
            self.screen.blit(N, (10, 5))

            # Mostra o nº máximo de Bots na Sala
            NM = self.SimaFont.render(f'Nº máximo de pessoas na sala: {int((self.sala_atual).nmax)}', True, (255, 255, 255))
            self.screen.blit(NM, (880, 5))

    Simulação = SIMA()
    return(Simulação.SimaMain())
