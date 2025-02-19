import pygame, time, sys

def detetaColisao():
    if jacareX + jacareW >= patoX:
        return True
    return False

def desenhaVidas():
    nVida = patoVidas
    while nVida > 0:
        gameDisplay.blit(patoVidaImg, (780 - 60 * nVida, 20))
        nVida -= 1
        
        
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jacare vs Pato')

patoImg = pygame.image.load('pato.jpg')
patoW = 100
patoH = 60
patoX = 700
patoY = 300
patoImg = pygame.transform.scale(patoImg, (patoW, patoH))

patoVidaImg = pygame.transform.scale(patoImg, (50, 50))
patoVidas = 3

jacareImg = pygame.image.load('jacare.jpg')
jacareW = 150
jacareH = 60
jacareX = 100
jacareImg = pygame.transform.scale(jacareImg, (jacareW, jacareH))


FIM = False
while (not FIM) and (patoVidas > 0):
    # ler o teclado e se tiver o espaco, paused = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            FIM = True
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            FIM = True
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            patoY -= 25

    if detetaColisao():
        patoVidas -= 1
        patoX = 700
        patoY = 300
        
    # Renderiza
    gameDisplay.fill((255,255,255))
    desenhaVidas()
    gameDisplay.blit(patoImg, (patoX,patoY))
    gameDisplay.blit(jacareImg, (jacareX,300))

    # Atualiza display
    pygame.display.update()

    time.sleep(0.1)
    
    patoY += 5
    if patoY > 300:
        patoY = 300
        
    patoX -= 20
    if patoX < 0: 
        patoX = 800
pygame.quit()