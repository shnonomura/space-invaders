import sys

import pygame

def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1100,800))
    pygame.display.set_caption("Space Invaders")


    #inicia o laco principal do jogo
    while True:

        #observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # deixa a tela mais recente visivel
        pygame.display.flip()

if __name__ == '__main__':
    run_game()