import pygame

# Inicializar o jogo
pygame.init()
ecra = pygame.display.set_mode((800, 600))
relogio = pygame.time.Clock()

rodando = True
while rodando:
    # 1. Processar Eventos (Input do utilizador)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # 2. Atualizar Lógica do Jogo

    # 3. Desenhar na Tela
    ecra.fill((30, 16, 53))  # O teu fundo roxo do MindUp!
    pygame.display.flip()

    relogio.tick(60)  # Garantir 60 FPS

pygame.quit()