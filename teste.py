import pygame
import os

pygame.init()

# Ecrã
screen_width = 1920
screen_height = 1020

pygame.display.set_caption('MindUp Education')
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Caminhos de ficheiros
caminho_base = os.path.dirname(__file__)
carregamento_caminho = os.path.join(caminho_base, "imagens", "Tela_carregamento.png")
inicial_caminho = os.path.join(caminho_base, "imagens", "Tela_inicial.png")

# Carregamento de ficheiros
tela_carregamento = pygame.image.load(carregamento_caminho)
tela_inicial = pygame.image.load(inicial_caminho)
carregamento = pygame.transform.smoothscale(tela_carregamento, (screen_width, screen_height))
inicial = pygame.transform.smoothscale(tela_inicial, (screen_width, screen_height))

running = True

# Variáveis para controlar o tempo e o ecrã atual
estado_atual = "carregamento"
tempo_inicio = pygame.time.get_ticks()  # Guarda o momento exato em que o jogo arranca

while running:
    # Gestão de eventos (fecha a janela se clicares no X)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Verificar se já passaram 5 segundos (5000 milissegundos)
    tempo_atual = pygame.time.get_ticks()
    if estado_atual == "carregamento" and tempo_atual - tempo_inicio >= 5000:
        estado_atual = "inicial"  # Muda para o ecrã inicial após 5 segundos

    # Limpar o ecrã
    screen.fill((30, 16, 53))

    # Desenhar a imagem correta dependendo do estado atual
    if estado_atual == "carregamento":
        screen.blit(carregamento, (0, 0))
    else:
        screen.blit(inicial, (0, 0))

    # Atualizar o ecrã (sem congelar!)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()