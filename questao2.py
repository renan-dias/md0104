import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Adivinhação")

# Define as cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
palpite = None
tentativas = 0
fim_de_jogo = False
fonte = pygame.font.Font(None, 36)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN and not fim_de_jogo:
                try:
                    palpite = int(entrada_texto)
                    tentativas += 1
                    entrada_texto = ''

                    #Implemente o conectivo lógico "OR"
                    #Preencha a linha abaixo com o conectivo apropriado
                    if :
                        mensagem = "Muito alto!"
                    elif palpite < numero_secreto:
                        mensagem = "Muito baixo!"
                    else:
                        mensagem = f"Parabéns! Você adivinhou em {tentativas} tentativas."
                        fim_de_jogo = True
                except ValueError:
                    mensagem = "Por favor, digite um número válido."
            elif evento.key == pygame.K_BACKSPACE:
                entrada_texto = entrada_texto[:-1]
            else:
                entrada_texto += evento.unicode

    # Limpa a tela
    tela.fill(branco)

    # Desenha os textos
    texto_instrucao = fonte.render("Adivinhe um número entre 1 e 100:", True, preto)
    tela.blit(texto_instrucao, (50, 50))

    entrada_rect = pygame.Rect(50, 100, 200, 36)
    pygame.draw.rect(tela, preto, entrada_rect, 2)
    texto_entrada = fonte.render(entrada_texto, True, preto)
    tela.blit(texto_entrada, (entrada_rect.x + 5, entrada_rect.y + 5))

    if palpite is not None:
        texto_mensagem = fonte.render(mensagem, True, preto)
        tela.blit(texto_mensagem, (50, 150))

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
