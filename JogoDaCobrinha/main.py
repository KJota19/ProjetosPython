#Importando Bibliotecas
import pygame
import random

#Inicializando O Jogo
pygame.init()#Start do jogo
pygame.display.set_caption("JOGO SNAKE PYTHON")# Dá um titulo para o jogo
largura, altura = 600 , 400# Define as dimensões para a tela do jogo
tela=pygame.display.set_mode((600,400))# Cria a tela com os valores de largura e altura.
relogio=pygame.time.Clock()# Um relógio para controlar o tempo do jogo

#Cores
preto=(0,0,0)
branca=(255,255,255)
vermelha=(255,0,0)
verde=(0,255,0)
#Cores que serão usadas no jogo, definidas por combinações de vermelho, verde e azul(RGB)
#Parametros da cobrinha.

#Configurações Da Cobrinha
tamanho_quadrado=20#Tamanho dos blocos que compõe a cobrinha
velocidade_jogo=8#Velocidade com que o jogo roda(frames por segundo)

#Função Para Gerar Comida
def gerar_comida():#Gera uma posição aleatória para a comida na tela.
    comida_x = (random.randrange(0,largura-tamanho_quadrado) // 20)*20#Gera um número aletório entre 0 e 600 - 20...divide esse valor por 20 para caber na tela sem ocupar dois quadrados...como por exemplo um número quebrado faria...e multiplica por 20 para preencher totalmente esse quadrado com 20x20.
    comida_y = (random.randrange(0,altura-tamanho_quadrado) // 20)*20#Gera um número aletório entre 0 e 600 - 20...divide esse valor por 20 para caber na tela sem ocupar dois quadrados...como por exemplo um número quebrado faria...e multiplica por 20 para preencher totalmente esse quadrado com 20x20.
    return comida_x,comida_y

def desenhar_comida(tamanho_bloco,comida_x,comida_y):
    pygame.draw.rect(tela,vermelha,[comida_x,comida_y,tamanho_bloco,tamanho_bloco])#Gera na tela, um quadrado...vermelho...tanto na posição x quanto y(largura e altura)com um tamanho de 20x20

def desenhar_cobra(tamanha,pixels):
    for i, pixel in enumerate(pixels):
        if i == len(pixels) - 1:
            pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanha, tamanha])
            # Desenha os olhos
            eye_size = tamanha // 5
            eye_offset = tamanha // 3
            eye_y = pixel[1] + tamanha // 4
            eye1_x = pixel[0] + eye_offset
            eye2_x = pixel[0] + tamanha - eye_offset - eye_size

            pygame.draw.circle(tela, branca, (eye1_x, eye_y), eye_size)
            pygame.draw.circle(tela, branca, (eye2_x, eye_y), eye_size)

            pupil_size = eye_size // 2
            pupil_offset = pupil_size // 2
            pupil1_x = eye1_x + pupil_offset
            pupil2_x = eye2_x + pupil_offset
            pupil_y = eye_y + pupil_offset
            pygame.draw.circle(tela, preto, (pupil1_x, pupil_y), pupil_size)
            pygame.draw.circle(tela, preto, (pupil2_x, pupil_y), pupil_size)
        else:
            pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanha, tamanha])
        
    #for pixel in pixels:
        #pygame.draw.rect(tela,verde,[pixel[0],pixel[1],tamanha,tamanha])#Gera na tela...no pixel 0 e 1 uma qudrado de 20x20 verde

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica",35)
    texto = fonte.render(f"pontos: {pontuacao}",True, branca)
    tela.blit(texto, [1, 1])
    #Gera um titulo para pontuação e coloca a pontuação

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x=0
        velocidade_y=tamanho_quadrado
    if tecla == pygame.K_UP:
        velocidade_x=0
        velocidade_y=-tamanho_quadrado
    if tecla == pygame.K_RIGHT:
        velocidade_x=tamanho_quadrado
        velocidade_y=0
    if tecla == pygame.K_LEFT:
        velocidade_x=-tamanho_quadrado
        velocidade_y=0
    return velocidade_x,velocidade_y
    #Gera as regras das teclas...cima,baixo,direita,esquerda...(se for para cima  é - tamanho quadrado...ou seja anda 20 de velocidade)

def rodar_jogo():
    fim_jogo=False
    x=largura/2 
    #Largura em cima e largura em baixo ... 300 para cada lado
    y=altura/2
    #Cima e baixo na esquerda e direita...200 para cada lado

    velocidade_x = 0
    #Quanto que a cobra vai andar para cima,baixo,esquerda,direita...
    velocidade_y = 0 

    tamanho_cobra=1#Tamanho inicial da cobra
    pixels=[]#Lista vazia de pixels verdes da cobra
    comida_x,comida_y=gerar_comida()#Função de cordenadas de comida
    
    while not fim_jogo:#Enquanto fim de jogo não for true
        tela.fill(preto)#Mostra fundo da tela do jogo


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:#Se apertar para sair
                fim_jogo=True#Ele quita
            elif evento.type == pygame.KEYDOWN:#Se for qualquer tecla...
                velocidade_x,velocidade_y = selecionar_velocidade(evento.key)# a velocidade tanto no x quanto y vai atualizar de acordo com a regra acima...
        #desenhar_comida

        desenhar_comida(tamanho_quadrado,comida_x,comida_y)# Feito isso...mostra a comida...com tamanho,cor e dimensão
        
        if x < 0 or x >= largura or y < 0 or y>= altura:
            fim_jogo=True
            #Se x e y for menor ou maior que a tela, o jogo fecha
        x += velocidade_x#Aqui atualiza com a velocidade do jogo...que na verdade é o comando do teclado
        y += velocidade_y#Aqui atualiza com a velocidade do jogo...que na verdade é o comando do teclado
        
        #Desenhar_cobra
        pixels.append([x,y])#Adiciona a dimensão da cobra a pixels conforme x e y atualizados...
        if len(pixels)>tamanho_cobra:#Se pixels(20x20) for maior que 1...
            del pixels[0]#Deleta um quadrado...


        #Se a cobra bateu no prórprio corpo
        for pixel in pixels[:-1]:#Olha para o quadrado anterior...
            if pixel == [x, y]:#Se for igual...
                 fim_jogo = True#Jogo fecha
        
        desenhar_cobra(tamanho_quadrado, pixels)#Essa sempre vem primeiro antes das condições
        #Desenha_pontos
        desenhar_pontuacao(tamanho_cobra -1)#Essa sempre vem primeiro antes das condições


        pygame.display.update()#Atualização da tela
        
        
        #Criar nova comida
        if x == comida_x and y == comida_y:#Se x e y for igual ao tamanho da comida x e y 
            tamanho_cobra +=1#tamaho da cobra aumenta
            comida_x,comida_y=gerar_comida()#E gera uma nova comida
        
        relogio.tick(velocidade_jogo)#Relógio do jogo vai de acordo com a velocidade do jogo

rodar_jogo()#Função para rodar o jogo
        