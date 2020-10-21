import pygame

# initialization (Must)
pygame.init()

# Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Test Games")

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # event = Windows Closed
            running = False

# pygame End
pygame.quit()
