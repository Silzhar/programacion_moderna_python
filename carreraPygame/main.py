# -*- coding: utf-8 -*-
"""
Created on Sun May  5 20:02:18 2019     @author: silzhar
"""
import pygame
import sys


class Game():
    corredores = []
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera !")
        self.bacground = pygame.image.load("road.jpg")
        
        self.runner = pygame.image.load("turtle.png")
    
    def competir(self):
        
        x = 0 
        winner = False
        
        while True:   # comprobar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # refrescar / renderizar la pantalla        
            self.__screen.blit(self.bacground, (0,0)) # blit = volcado de ...
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
            
            x += 3
            if x>= 250:
                winner = True


if __name__== '__main__':
    pygame.init()
    game = Game()
    game.competir()
    
        