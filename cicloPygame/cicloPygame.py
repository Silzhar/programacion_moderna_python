# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:39:18 2019  @author: silzhar
"""
import pygame, sys

width = 640
height = 480

screen = pygame.display.set_mode((width,height))
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo de Pygame ")

pygame.init()  # si no funciona : pygame.font.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get(): # traer eventos de pygame
        if event.type == pygame.QUIT:
            gameOver = True
            
    pygame.display.flip() #para refrescar pantalla 
    #  pygame.display.flip() es = a pygame.display.update() metodos iguales
    
pygame.quit()
sys.exit()
