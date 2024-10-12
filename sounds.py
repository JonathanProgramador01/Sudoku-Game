import pygame
from stuff import resource_path



class Sounds:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Intro.wav"))
        pygame.mixer.music.play(-1)


    def facil(self):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Facil.wav"))
        pygame.mixer.music.play(-1)


    def inicio(self):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Intro.wav"))
        pygame.mixer.music.play(-1)

    def medio(self):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Medio.wav"))
        pygame.mixer.music.play(-1)

    def dificil(self):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Dificil.wav"))
        pygame.mixer.music.play(-1)

    def imposible(self):
        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("Musica/Imposible.wav"))
        pygame.mixer.music.play(-1)




