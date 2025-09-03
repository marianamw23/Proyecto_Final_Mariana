#utilizando pygame
import pygame

#Inicio del juego
pygame.init()
#crear ventana=
ventana = pygame.display.set_mode(400 , 300)
pygame.display.set_caption("coloque un mensaje")
#color ventana
AZUL= (0,0,255)

ejecutando = True
while ejecutand:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
           ejecutando = False

        ventana.fill(AZUL)#fill llenar
        
     pygame.display.flip()
pygame.quit()

