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

# moving coordinate
to_x = 0
to_y = 0

# Event Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # event = Windows Closed
            running = False

        # Keyboard event
        if event.type == pygame.KEYDOWN:            # WHEN USER press KEYS,
            if event.key == pygame.K_LEFT:              # move character to left
                to_x -= 2                                   # calculate x to left by 2
            elif event.key == pygame.K_RIGHT:           # move character to right
                to_x += 2
            elif event.key == pygame.K_UP:              # move character to up
                to_y -= 2
            elif event.key == pygame.K_DOWN:            # move character to down
                to_y += 2

        if event.type == pygame.KEYUP:              # WHEN USER release KEYS,
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0

    # set character moving coordinate
    character_x_pos += to_x
    character_y_pos += to_y

    # set character moving Limit on screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Background blit
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # screen update every frame (MUST)
    pygame.display.update()
# pygame End
pygame.quit()
