import pygame

# initialization (Must)
pygame.init()

# Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Test Games")

# background image loading
background = pygame.image.load("./SplatoonLogo.jpg")

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # event = Windows Closed
            running = False

    # Background blit
    screen.blit(background, (0, 0))

    # screen update (MUST)
    pygame.display.update()
# pygame End
pygame.quit()
