# Bots&Player.py
import pygame
import numpy as np
import random as rd
import ColisaoT as C

FPS = 60

Angle = (np.pi / 4)

def Randc():                                 # Randomiza uma Cor
    return rd.uniform(0, 255)

#### Classes ####

class BOT:                                   # Cria as características da classe Bot 
    def __init__(self, x, y, velocidade_i, distanciamento, id):
        self.raio = 15
        self.dist = distanciamento

        self.x = x
        self.y = y

        self.velocidade_i = velocidade_i
        self.v_x = 0
        self.v_y = 0
        self.lv_x = self.v_x
        self.lv_y = self.v_y

        self.color = (Randc(), Randc(), Randc())
        self.color_o = self.color
        self.color_a = (255, 0, 0)

        self.collider = C.GCollider()
        self.collider.swap = True
        self.id = id

        self.dir = 1
        if(rd.uniform(0, 1) >= 0.5):
            self.dir = -1

        # randomiza o ângulo
        randAngle = rd.uniform(-Angle, Angle)

        # randomiza velocidade
        self.randVelocidade = rd.uniform(self.velocidade_i/1.2, self.velocidade_i*1.2)
        self.v_x = self.dir * self.randVelocidade * np.cos(randAngle)
        self.v_y = self.randVelocidade * np.sin(randAngle)

class Player:                                # Cria as características da classe Player
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.raio = r

        self.color = (Randc(), Randc(), Randc())
        self.color_o = self.color
        self.color_a = (255, 0, 0)
        self.id = 0

        self.collider = C.GCollider()
        self.collider.swap = False
        self.dist = 0

        self.last_x = 0 
        self.last_y = 0
        self.dir_x = 0
        self.dir_y = 0

#### Funções Bots #####

def ListaBot(n, dist, local):                # Cria uma lista de [n] Bots com um distanciamento de [dist] em um determinado [local]
    lista = []
    for i in range(n):
        Bot = BOT( rd.randint(local.x + 25, local.x - 25 + local.largura), rd.randint(local.y + 25, local.y - 25 + local.altura), (1 / FPS) * 3, dist, i+1)
        if len(lista) >= 1:   
            for Bot2 in lista:
                if Bot != Bot2:                                                       
                    D = np.sqrt((Bot.x - Bot2.x)**2 +(Bot.y - Bot2.y)**2)
                    while D <= ((2 * Bot.raio) + (2* Bot.dist)): # Enquanto a colisão ocorrer, muda o x e y
                        Bot.x = rd.randint(local.x + 25, local.x - 25 + local.largura)
                        Bot.y = rd.randint(local.y + 25, local.y - 25 + local.altura)
                        D = np.sqrt((Bot.x - Bot2.x)**2 +(Bot.y - Bot2.y)**2)                                            
            lista.append(Bot)
        else:
            lista.append(Bot)
    return lista

def ListaAlerta(ListaBots):                  # Cria uma lista de Rects dos Bots de [ListaBots] para alerta
    ListaDist = []
    for Bot in ListaBots:
        b = pygame.Rect(((Bot.x - Bot.raio) - Bot.dist, (Bot.y - Bot.raio) - Bot.dist, (2*Bot.dist) + 2*Bot.raio, (2*Bot.dist) + 2*Bot.raio))
        ListaDist.append(b)
    return ListaDist

def AlertaB(ListaBots, ListaA):              # Verifica o Distanciamento dos Bots de [ListaBots] e aciona o  Alerta
    for Rect in ListaA:                                                               
        colisao = Rect.collidelist(ListaA)                                                     # Verifica se a colisão ocorreu e retorna o indíce do objeto colidido
        Bot1 = ListaBots[ListaA.index(Rect)]                                                   # ListaB[ListaD.index(Rect)] acha o objeto oqual o Rect corresponde
        Bot2 = ListaBots[colisao]                                                                 # ListaB[colisao] acha qual foi o objeto colidido
        if Rect != ListaA[colisao]:                                                            # Se os Rects pertencerem a objetos diferentes
            if colisao != -1:                                                                     # Se ocorrer colisão
                Bot1.color = Bot1.color_a                                                         # Muda para a cor de alerta
                Bot2.color = Bot2.color_a                                                    
        else:
            Bot1.color = Bot1.color_o                                                             # Volta para a cor original
            Bot2.color = Bot2.color_o

def DesenhaBots(ListaBots, screen):          # Desenha [ListaBots] em uma tela [screen]
    for Bot in ListaBots:
        pygame.draw.circle(screen, Bot.color, (Bot.x, Bot.y ), Bot.raio)

def MovLimite(local, ListaBots, time):       # Define o limite do movimento [ListaBots] em certo [local] com base em um certo [tempo]
    for Bot in ListaBots:                                 
        Bot.x += (Bot.v_x) * time                         # Movimento Bot
        Bot.y += (Bot.v_y) * time

        if(Bot.y < local.y + Bot.raio):                   # Colisão superior
            Bot.y = local.y + Bot.raio
            Bot.v_y = (-1)*Bot.v_y

        if(Bot.y > (local.y + local.altura) - Bot.raio):  # Colisão inferior
            Bot.y = (local.y + local.altura) - Bot.raio
            Bot.v_y = (-1)*Bot.v_y

        if(Bot.x < local.x + Bot.raio):                   # Colisão lateral (Esquerda)
            Bot.x = local.x + Bot.raio
            Bot.v_x = (-1)*Bot.v_x

        if(Bot.x > (local.x + local.largura) - Bot.raio): # Colisão lateral (Direita)
            Bot.x = (local.x + local.largura) - Bot.raio
            Bot.v_x = (-1)*Bot.v_x

#### Funções Player + Bots ####

def AlertaP(player, ListaBots, ListaA):      # Verifica o Distanciamento do Bot de [ListaBots] com o player e aciona o  Alerta
    rectPlayer = pygame.Rect(((player.x - player.raio) - 8, (player.y - player.raio) - 8, player.raio*2 + 16, player.raio*2 + 16))                                                             
    colisao = rectPlayer.collidelist(ListaA)                                                      # Verifica se a colisão ocorreu e retorna o indíce do objeto colidido                                                  # ListaB[ListaD.index(Rect)] acha o objeto oqual o Rect corresponde
    Bot = ListaBots[colisao]                                                                      # ListaB[colisao] acha qual foi o objeto colidido                                                         # Se os Rects pertencerem a objetos diferentes
    if colisao != -1:                                                                             # Se ocorrer colisão
        player.color = player.color_a                                                             # Muda para a cor de alerta
        Bot.color = Bot.color_a                                                    
    else:
        player.color = player.color_o                                                             # Volta para a cor original
        Bot.color = Bot.color_o

def NPessoas(ListaBots, player, sala_atual): # Conta nº de pessoas (Bot + player) na [sala_atual]
    RectSala = pygame.Rect(((sala_atual.x, sala_atual.y, sala_atual.largura, sala_atual.altura)))
    
    if RectSala.collidepoint(player.x, player.y):
        N = len(ListaBots) + 1
    else:
        N = len(ListaBots)
    return N

def MovePlayer(player, keys, time, screen):  # Movimenta o Player por meio de WASD e salva sua direção

    # Calcula a direção de movimento
    player.dir_x = 0
    player.dir_y = 0

    if keys[pygame.K_d]:    
        player.dir_x += 1
                
    if keys[pygame.K_a]:    
        player.dir_x -= 1
                
    if keys[pygame.K_w]:
        player.dir_y -= 1
                
    if keys[pygame.K_s]:
        player.dir_y += 1

    if(player.dir_x != 0 and player.dir_y != 0):            # Normaliza o vetor direção
            tmp_normal = np.sqrt(np.power(player.dir_x, 2) + np.power(player.dir_y, 2))

            player.dir_x = player.dir_x / tmp_normal
            player.dir_y = player.dir_y / tmp_normal

    ####  Colisão por pixel  ####
    
    color = screen.get_at((             # Fornece a cor do pixel a frente do player
                                int(player.x + player.dir_x * player.raio*1.2),
                                int(player.y + player.dir_y * player.raio*1.2)
                            ))
    if(color != (70,130,180)):          # Se a cor do pixel for a proibida, o Player não se move
        if keys[pygame.K_d]:
            player.x += time*0.3
                
        if keys[pygame.K_a]:
            player.x -= time*0.3
                
        if keys[pygame.K_w]:
            player.y -= time*0.3
                
        if keys[pygame.K_s]:
            player.y += time*0.3

    #### Colisão por posição (Análise)  ####

def Atualiza(ListaBots, local, time, player, keys, screen): # Realiza todas as atualizações de [ListaBots] em um determinado [local] com base em um certo [time]                
    ListaD = ListaAlerta(ListaBots) # Alterar
    ListaGeral = ListaBots + [player]

    AlertaB(ListaBots, ListaD) # Certo
    AlertaP(player, ListaBots, ListaD) # Certo
    C.Colisao(ListaGeral) # Certo

    MovLimite(local, ListaBots, time) # Certo
    MovePlayer(player, keys, time, screen) # Certo


"""  Funções que não são mais utilizadas:


def ColisaoP(ListaBots, player): # Verifica a colisão dos Bots de [ListaBots] com o [player] !!!ARRUMAR!!!
    for Bot in ListaBots:
        D = np.sqrt((Bot.x - player.x)**2 +(Bot.y - player.y)**2)
        Limite = ((2 * Bot.raio) + (2* Bot.dist))
        if  D <= Limite:             
            dir = Bot.dir                                                    
            if dir == -1:
                Bot.velocidade_x = -Bot.velocidade_x
                Bot.velocidade_y = -Bot.velocidade_y
                dir = - dir                                  
            elif dir == 1:
                Bot.velocidade_x = -Bot.velocidade_x
                Bot.velocidade_y = -Bot.velocidade_y
                dir = - dir

def MudaDir(Bot1, Bot2, dir): # (Revisar) Muda as direções do [Bot1] e do [Bot2] 
        Bot1.lv_x = Bot1.velocidade_x
        Bot1.lv_y = Bot1.velocidade_y

        Bot2.lv_x = Bot2.velocidade_x
        Bot2.lv_y = Bot2.velocidade_y

        Bot1.velocidade_x = Bot2.lv_x
        Bot1.velocidade_y = Bot2.lv_y

        Bot2.velocidade_x = Bot1.lv_x
        Bot2.velocidade_y = Bot1.lv_y
                 
        dir = -dir 

def ListaRect(ListaBots): # Cria uma lista de Rects dos Bots de [ListaBots] para colisão
    listaRect = []
    for Bot in ListaBots:
        b = pygame.Rect(((Bot.x - Bot.raio) - (Bot.dist/2), (Bot.y - Bot.raio) - (Bot.dist/2) , 2*Bot.raio + (Bot.dist/2)*2 ,  2*Bot.raio + (Bot.dist/2)*2 ))
        listaRect.append(b)
    return listaRect
"""