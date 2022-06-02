import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# Title 
pygame.display.set_caption("Hobin Game")

# FPS
clock = pygame.time.Clock()

# Load background
background = pygame.image.load("C:\\Users\\gatob\\Desktop\\새 폴더\\code\\pygame\\background.png")

# Load character
character = pygame.image.load("C:\\Users\\gatob\\Desktop\\새 폴더\\code\\pygame\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2  - character_width / 2
character_y_pos = screen_height - character_height


to_x = 0
to_y = 0
# 이동속도
character_speed = 0.3
# Event loop
running = True
while running:
    
    dt = clock.tick(60) # 게임 화면 초당 프레임 수

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:     # KEYDOWN == 키가 눌러졌는지
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 네모 안에 머무를 수 있게 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    

    screen.blit(background, (0,0))  # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면을 매 프레임마다 다시 그리기

pygame.quit
