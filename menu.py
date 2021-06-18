"""
Tugas Besar Strategi Algoritma
Anggota Kelompok :
- Adhie Rachmatullah Sugiono (1301194059)
- Azriel Naufal Aulia (1301190374)
- Egi Shidqi	Rabbani (1301190443)
- Fiyona Anmila Syamsir (1301194201)
"""

#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
from pygame.locals import *
import TubesSA_1Bot
import TubesSA_2Bot
import TubesSA_Puzzle

# ---------
# CONSTANTS
# ---------
BG_COLOR = (145, 121, 250) #ganti warna background
WIDTH = 600
HEIGHT = 600
# pygame.rect(left, top, width, height)
rectLocSize_1 = (50, 100, 200, 50) 
rectLocSize_2 = (50, 200, 200, 50)
rectLocSize_3 = (50, 300, 200, 50)
rectColor_1 = (94, 23, 235)
rectColor_2 = (94, 23, 235)
rectColor_3 = (94, 23, 235)
text_button1 = "Vs Bot"
text_button2 = "Bot vs Bot"
text_button3 = "Random Puzzle"
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Tic-Tac-Toe Backtracking')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
font_title = pygame.font.SysFont('arial', 40)
font = pygame.font.SysFont('arial', 25)

 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill(BG_COLOR)
        draw_text("Tic-Tac-Toe", font_title, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(rectLocSize_1)
        button_2 = pygame.Rect(rectLocSize_2)
        button_3 = pygame.Rect(rectLocSize_3)
        if button_1.collidepoint((mx, my)):
            if click:
                TubesSA_1Bot.main_bot()
        if button_2.collidepoint((mx, my)):
            if click:
                TubesSA_2Bot.main_2Bot()
        if button_3.collidepoint((mx, my)):
            if click:
                TubesSA_Puzzle.main_puzzle()
        # pygame.draw.rect(surface, color, rect)		
        pygame.draw.rect(screen, rectColor_1, button_1)
        pygame.draw.rect(screen, rectColor_2, button_2)
        pygame.draw.rect(screen, rectColor_3, button_3)
		# caption di button
        draw_text(text_button1, font, (255, 255, 255), screen, 60, 110)
        draw_text(text_button2, font, (255, 255, 255), screen, 60, 210)
        draw_text(text_button3, font, (255, 255, 255), screen, 60, 310)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()