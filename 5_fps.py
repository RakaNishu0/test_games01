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

# FPS
clock = pygame.time.Clock()

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

# character moving speed
character_speed = 0.5

# Event Loop
running = True
while running:
    # set FPS
    dt = clock.tick(60)
    # print("FPS= "+str(clock.get_fps()))     # print frames on running console

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       # event = Windows Closed
            running = False

        # Keyboard event : key pressed
        if event.type == pygame.KEYDOWN:            # WHEN USER press KEYS,
            if event.key == pygame.K_LEFT:              # move character to left
                to_x -= character_speed                     # calculate x to left by 2
            elif event.key == pygame.K_RIGHT:           # move character to right
                to_x += character_speed
            elif event.key == pygame.K_UP:              # move character to up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:            # move character to down
                to_y += character_speed

        # Keyboard event : key Released
        if event.type == pygame.KEYUP:              # WHEN USER release KEYS,
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
            # elif event.key == pygame.K_UP or pygame.K_DOWN:   # 이 경우에는 up/down 을 누른 후 해제가 되지 않는다
            #   to_y = 0                                        # 왜냐하면, up/down을 떼었을 때, 이미 left/right도 떼어진 상태이므로
            # 위의 left/right의 if문을 받지, elif로 내려오지 않기 때문이다. 그래서 아래처럼 별개로 만들어줘야 한다.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                to_y = 0

    # set character moving coordinate * frame rate
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # set character moving Limit on screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # blit background and character
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # screen update every frame (MUST)
    pygame.display.update()
# pygame End
pygame.quit()
