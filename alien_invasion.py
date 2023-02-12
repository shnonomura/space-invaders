# -*- coding: latin-1 -*-
import sys
import pygame

def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1100,800))
    pygame.display.set_caption("Space Invaders")
    
    # define a cor de fundo
    bg_color = (230, 250, 230)


    #inicia o laco principal do jogo
    while True:

        #observa eventos de teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        # redesenha a tela a cada passagem pelo laço
        screen.fill(bg_color)
        
        # deixa a tela mais recente visivel
        pygame.display.flip()

if __name__ == '__main__':
    run_game()