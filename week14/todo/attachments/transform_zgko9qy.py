import pygame

BLACK =(0,0,0)
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((300,300))

degree = 0
done = False
clock = pygame.time.Clock()

while not done :
    clock.tick(10)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
    
    surf = pygame.Surface((100,100))
    surf.fill((0,0,0))
    rectangle = pygame.Rect(0,0,100,100)
    pygame.draw.rect(surf, (255,0,0),rectangle,5)

    oldCenter = (170,200)
    rotatedSurf = pygame.transform.rotate(surf,degree)
    rotRec = rotatedSurf.get_rect()
    rotRec.center = oldCenter
    screen.blit(rotatedSurf, rotRec)
    degree -= 5
    if degree < 0:
        degree = 360
 
    pygame.display.update()
 
pygame.quit()