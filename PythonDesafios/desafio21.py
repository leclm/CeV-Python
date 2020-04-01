'''
Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3.'''
import pygame  # não deu pra instalar o módulo
pygame.init()  # inicia o módulo
pygame.mixer.music.load('musica21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
