import pygame
import sys
from biblioteca import *


pygame.init()


pygame.display.set_caption("Batalla Naval")


pygame.display.set_icon(imagen_icono)


pygame.mixer.music.load("2do_parcial_pygame.py/sonidos/sonido_menuu.wav")
pygame.mixer.music.set_volume(0.2) # 0 - 1 -> 0.2 es el 20% del volumen
pygame.mixer.music.play(-1, 0.0)
sonido_botones = pygame.mixer.Sound("2do_parcial_pygame.py/sonidos/sonido_boton.wav")
sonido_clic_juego = pygame.mixer.Sound("2do_parcial_pygame.py\sonidos\sonido_cañones.wav")
dificultad = "facil"


while True:
    seleccion = menu_principal()
    
    if seleccion == "Dificultad":
        dificultad = mostrar_pantalla_dificultad()
    if seleccion == "jugar":
        pygame.mixer.music.stop()  
        pygame.mixer.music.load("2do_parcial_pygame.py\sonidos\sonido_oceano.mp3")
        pygame.mixer.music.set_volume(1)  
        pygame.mixer.music.play(-1, 0.0)  


        tablero = inicializar_matriz(10, 10)
        colocar_todos_los_barcos(tablero, dificultad)
        puntaje = 0
        juego_en_curso = True
        
        
        while juego_en_curso:
            salir_rect, reiniciar_rect = pantalla_juego(puntaje, tablero)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                if evento.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = evento.pos
                    columna = mouse_x // TAMANIO_CASILLA
                    fila = mouse_y // TAMANIO_CASILLA
                    

                    #al hacer click este dentro del tablero 
                    if 0 <= fila < FILAS and 0 <= columna < COLUMNAS:
                        puntaje = detectar_clic(tablero, fila, columna, puntaje)
                        
                        #sonido del cañon al hacer click
                        sonido_clic_juego.play()  
                        

                    if salir_rect.collidepoint(evento.pos):
                        sonido_botones.play()
                        juego_en_curso = False
                        break

                    if reiniciar_rect.collidepoint(evento.pos):
                        sonido_botones.play()
                        tablero = inicializar_matriz(10, 10)
                        colocar_todos_los_barcos(tablero, dificultad)
                        puntaje = 0
                        break
                  
            pantalla_juego(puntaje, tablero)
