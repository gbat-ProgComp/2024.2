import pygame, time, sys


def detetaColisao():
    colisaoX = not ((patoX > jacareX + jacareW) or (patoX+patoW < jacareX))
    colisaoY = (patoY + patoH > jacareY)
    if colisaoX and colisaoY:
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
patoX = 800
patoY = 300
patoImg = pygame.transform.scale(patoImg, (patoW, patoH))

patoVidaImg = pygame.transform.scale(patoImg, (50, 50))
patoVidas = 3

jacareImg = pygame.image.load('jacare.jpg')
jacareW = 150
jacareH = 60
jacareX = 100
jacareY = 300
jacareImg = pygame.transform.scale(jacareImg, (jacareW, jacareH))

clock = pygame.time.Clock()

try:
    fps = int(sys.argv[1])
except:
    fps = 30

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
    
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP]:
        patoY -= 25

    if detetaColisao():
        patoVidas -= 1
        patoX = 700
        patoY = 300

    # Renderiza
    gameDisplay.fill((255,255,255))
    desenhaVidas()
    gameDisplay.blit(patoImg, (patoX,patoY))
    gameDisplay.blit(jacareImg, (jacareX,jacareY))

    # Atualiza display
    pygame.display.update()

    clock.tick(fps)

    patoY += 5
    if patoY > 300:
        patoY = 300
    if patoY <= 30:
        patoY = 30

    patoX -= 5
    if patoX < -patoW:
        patoX = 800
pygame.quit()