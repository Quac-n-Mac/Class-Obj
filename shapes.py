import pygame, math
pygame.init()
screen = pygame.display.set_mode((640,360))

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            playing = False
    screen.fill("black")
    pygame.draw.circle(screen, "white", (320, 180), 150, 0)
    pygame.draw.circle(screen, "black", (260, 120), 30, 0)
    pygame.draw.circle(screen, "black", (380, 120), 30, 0)

    pygame.draw.arc(screen, "black", (250, 140, 145, 170), math.pi, 2*math.pi, 20)


    # pygame.draw.circle(screen, "black", (320, 230), 88, 0)
    # pygame.draw.circle(screen, "white", (320, 220), 85, 0)
    # pygame.draw.line(screen, "black", (280, 270), (360, 270), 10)
    # pygame.draw.line(screen, "black", (250, 220), (280, 270), 10)
    # pygame.draw.line(screen, "black", (360, 270), (390, 220), 10)


    
    pygame.display.update()