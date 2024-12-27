import pygame
import pygame_menu
import random
import Game from "main.py"
pygame.font.init()


pygame.init()
sc_ui = pygame.display.set_mode((500, 500))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(sc)
