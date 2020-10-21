import pygame
# Mac에서는 pygame 1.9.6 으로 실행 시 창이 제대로 실행되지 않는 이슈가 있음
# 2.0.0.dev6 버전으로 설치해서 진행 함. (python3 -m pip install pygame==2.0.0.dev6)

# initialization (Must)
pygame.init()

# Resolution
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Test Games")

# background image loading
background = pygame.image.load("./background_moon.jpg")

# character loading (stripe)
character = pygame.image.load("./stripe.png")
character_size = character.get_rect().size      # get character's size (pixel size)
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # event = Windows Closed
            running = False

    # Background blit
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # screen update (MUST)
    pygame.display.update()
# pygame End
pygame.quit()
