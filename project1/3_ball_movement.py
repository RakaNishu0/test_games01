import os
import pygame
# Mac 에서는 pygame 1.9.6 으로 실행 시 창이 제대로 실행되지 않는 이슈가 있음
# 2.0.0.dev6 버전으로 설치해서 진행 함. (python3 -m pip install pygame==2.0.0.dev6)

# initialization (Must)
pygame.init()

# Resolution
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Project Games")

# FPS
clock = pygame.time.Clock()

# Path Setting
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# background image loading
background = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size  # 가로, 세로 크기를 구함
stage_height = stage_size[1]        # 0번째는 가로, 1번째는 세로

# character loading (stripe)
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height

# character moving variables
character_speed = 0.3
character_to_x_LEFT = 0
character_to_x_RIGHT = 0
# character_to_y_UP = 0
# character_to_y_DOWN = 0

# weapon loading
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# weapon fires multiple
weapons = []
weapon_speed = 10

# Ball loading
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# Ball Speed differences by Size
ball_speed = [-18, -15, -12, -9]

# Balls coordinate
balls = []
balls.append({
    "pos_x": 50,       # 공의 x 좌표
    "pos_y": 50,       # 공의 y 좌표
    "img_idx": 0,      # 공의 이미지 인덱스(ball_images) - 어느공으로 시작할까
    "to_x": 3,         # x축 이동방향
    "to_y": -3,        # y축 이동방향
    "init_speed_y": ball_speed[0]      # 최초 속도 y = ball_speed 의 0번째 값으로 적용
})

# set Text Font

# Game Time

# Calculate Times


# Event Loop
running = True
while running:
    # set FPS
    dt = clock.tick(30)
    # print("FPS= "+str(clock.get_fps()))     # print frames on running console

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event = Windows Closed
            running = False

        # Keyboard event : key pressed
        if event.type == pygame.KEYDOWN:  # WHEN USER press KEYS,
            if event.key == pygame.K_LEFT:  # move character to left
                character_to_x_LEFT -= character_speed  # calculate x to left by 2
            elif event.key == pygame.K_RIGHT:  # move character to right
                character_to_x_RIGHT += character_speed
            # elif event.key == pygame.K_UP:              # move character to up
            #     character_to_y_UP -= character_speed
            # elif event.key == pygame.K_DOWN:            # move character to down
            #     character_to_y_DOWN += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = (character_x_pos + character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        # Keyboard event : key Released
        if event.type == pygame.KEYUP:  # WHEN USER release KEYS,
            if event.key == pygame.K_LEFT:
                character_to_x_LEFT = 0
            if event.key == pygame.K_RIGHT:
                character_to_x_RIGHT = 0
            # elif event.key == pygame.K_UP or pygame.K_DOWN:
            #   to_y = 0
            # 이 경우에는 up/down 을 누른 후 해제가 되지 않는다
            # 왜냐하면, up/down을 떼었을 때, 이미 left/right도 떼어진 상태이므로
            # 위의 left/right의 if문을 받지, elif로 내려오지 않기 때문이다. 그래서 아래처럼 별개로 만들어줘야 한다.
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_UP:
        #         character_to_y_UP = 0
        #     if event.key == pygame.K_DOWN:
        #         character_to_y_DOWN = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pass

    # set character moving coordinate * frame rate
    character_x_pos += (character_to_x_LEFT + character_to_x_RIGHT) * dt
    # character_y_pos += (character_to_y_UP + character_to_y_DOWN) * dt

    # weapon moving coordinate
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    # weapon remove when y < 0:
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    # = if y < 0 = DO NOT into w[1] = no list data = remove

    # Balls pos coordinate
    for ball_idx, ball_val in enumerate(balls):     # list 의 index, value 를 반환
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
    # Ball Size
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
    # Horizontal Movement
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1    # 벽에 부딪히면 방향 전환
    # Vertical Movement
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_speed_y"]
            # stage 에 닿으면 튕기는 속도
            # Speed 라고 하지만, 초기에 설정한 속도값을 이용해 y 좌표를 크게 빼버리는 것 = 확 끌어올리는 효과
            # 결국 다 좌표 놀음이구나...
        else:
            ball_val["to_y"] += 0.7
            # 바닥에 닿지 않았을 때에는 일정하게 좌표값을 수정한다.

    # Ball's Moving Coordinate
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # set character moving Limit on screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # if character_y_pos < 0:
    #     character_y_pos = 0
    # elif character_y_pos > screen_height - stage_height - character_height:
    #     character_y_pos = screen_height - stage_height - character_height

    # Collision coordinate update
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy_rect = enemy.get_rect()
    # enemy_rect.left = enemy_x_pos
    # enemy_rect.top = enemy_y_pos

    # Check Collision Coordinate
    # if character_rect.colliderect(enemy_rect):
    #     print("Game Over")
    #     running = False

    # blit background and character
    screen.blit(background, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # Timer insert by text
    # elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 0))
    # screen.blit(timer, (15, 15))

    # if total_time - elapsed_time < 0:
    #     running = False
    #     print("Game Over")

    # screen update every frame (MUST)
    pygame.display.update()
# pygame End
pygame.quit()
