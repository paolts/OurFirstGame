#Leonardo Paoletti
#primo progetto videogiochi

def main_loop():
    import pygame

    pygame.init()

    # lo screen (con titolo)
    screen = pygame.display.set_mode((1280, 656))
    pygame.display.set_caption("Il mio primo gioco con PyGame!")

    running = True

    while running:
        #X di chiusura in alto
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
        
        
        #schermo di verde
        screen.fill("green")

        #aggiorna il contenuto dello schermo
        pygame.display.flip()

    #Chiude pygame
    pygame.quit()
