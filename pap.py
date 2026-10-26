import pygame
import os


pygame.init()
pygame.mixer.init()

# Ecrã
screen_width = 1540
screen_height = 800


pygame.display.set_caption('MindUp Education')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Caminhos de ficheiros
caminho_base = os.path.dirname(__file__)
carregamento_caminho = os.path.join(caminho_base, "imagens", "Tela_carregamento.png")
inicial_caminho = os.path.join(caminho_base, "imagens", "Tela_inicial.png")
principal_caminho = os.path.join(caminho_base, "imagens", "Tela_principal.png")
click_botao = os.path

# Carregamento de ficheiros
tela_carregamento = pygame.image.load(carregamento_caminho)
tela_inicial = pygame.image.load(inicial_caminho)
tela_principal = pygame.image.load(principal_caminho)
carregamento = pygame.transform.smoothscale(tela_carregamento, (screen_width, screen_height))
inicial = pygame.transform.smoothscale(tela_inicial, (screen_width, screen_height))
principal = pygame.transform.smoothscale(tela_principal, (screen_width, screen_height))

escala_x = 1540 / 1920
escala_y = 800 / 1080

botao_jogar = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 100)
botao_voltar = pygame.Rect(29*escala_x, 18*escala_y, 117*escala_x, 65*escala_y)
botao_opcoes = pygame.Rect(457*escala_x, 472*escala_y, 367*escala_x, 99*escala_y)

running = True

# Variáveis para controlar o tempo e o ecrã atual
estado_atual = "carregamento"
tempo_inicio = pygame.time.get_ticks()  # Guarda o momento exato em que o jogo arranca

while running:
    # Gestão de eventos (fecha a janela se clicares no X)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
            # Só verifica o clique se já estivermos no ecrã inicial!
                if estado_atual == "inicial" and botao_jogar.collidepoint(evento.pos):
                    estado_atual = "principal"
                elif estado_atual == "principal" and botao_voltar.collidepoint(evento.pos):
                    estado_atual = "inicial"
                elif estado_atual == "inicial" and botao_opcoes.collidepoint(evento.pos):
                    estado_atual = "carregamento"

    # Verificar se já passaram 5 segundos (5000 milissegundos)
    tempo_atual = pygame.time.get_ticks()
    if estado_atual == "carregamento" and tempo_atual - tempo_inicio >= 5000:
        estado_atual = "inicial"  # Muda para o ecrã inicial após 5 segundos

    # Limpar o ecrã
    screen.fill((30, 16, 53))

    # Desenhar a imagem correta dependendo do estado atual
    if estado_atual == "carregamento":
        screen.blit(carregamento, (0, 0))
    elif estado_atual == "inicial":
        screen.blit(inicial, (0, 0))
    elif estado_atual == "principal":
        screen.blit(principal, (0, 0))

    # Atualizar o ecrã (sem congelar!)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()