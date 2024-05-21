# Importando Bibliotecas
import pygame
import random

# Inicializando O Jogo
pygame.init()  # Start do jogo
pygame.display.set_caption("JOGO SNAKE PYTHON")  # Dá um título para o jogo
largura, altura = 600, 400  # Define as dimensões para a tela do jogo
tela = pygame.display.set_mode((largura, altura))  # Cria a tela com os valores de largura e altura.
relogio = pygame.time.Clock()  # Um relógio para controlar o tempo do jogo

# Cores
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Configurações Da Cobrinha
tamanho_quadrado = 20  # Tamanho dos blocos que compõe a cobrinha
velocidade_jogo = 8  # Velocidade com que o jogo roda (frames por segundo)

# Função Para Gerar Comida
def gerar_comida():  # Gera uma posição aleatória para a comida na tela
    comida_x = (random.randrange(0, largura - tamanho_quadrado) // tamanho_quadrado) * tamanho_quadrado
    comida_y = (random.randrange(0, altura - tamanho_quadrado) // tamanho_quadrado) * tamanho_quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho_bloco, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])  # Desenha a comida

def desenhar_cobra(tamanha, pixels):
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

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"pontos: {pontuacao}", True, branca)
    tela.blit(texto, [1, 1])  # Desenha a pontuação na tela

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    else:
        velocidade_x = 0
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    x = largura / 2  # Posição inicial da cobra (centro da tela)
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1  # Tamanho inicial da cobra
    pixels = []  # Lista de pixels que compõem a cobra
    comida_x, comida_y = gerar_comida()  # Posição inicial da comida

    while not fim_jogo:
        tela.fill(preto)  # Preenche a tela com a cor preta

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Se o jogador fechar a janela
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:  # Se uma tecla for pressionada
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True  # Fim de jogo se a cobra sair da tela

        x += velocidade_x
        y += velocidade_y

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True  # Fim de jogo se a cobra colidir com ela mesma

        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        pygame.display.update()  # Atualiza a tela

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1  # Aumenta o tamanho da cobra
            comida_x, comida_y = gerar_comida()  # Gera nova comida

        relogio.tick(velocidade_jogo)  # Controla a velocidade do jogo

rodar_jogo()  # Inicia o jogo

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Tenta rodar o jogo, captura e imprime qualquer exceção que ocorrer
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para sair...")