import pygame
import random
import os

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("폭탄피하기 게임")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # 현재 파일 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(current_path, "background.png"))


character = pygame.image.load(os.path.join(current_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.3
enemy_speed = 0.6

enemy = pygame.image.load(os.path.join(current_path, "bomb.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

game_font = pygame.font.Font(None, 40)

total_time = 10

start_ticks = pygame.time.get_ticks()


count = 0 # 피한 횟수
running = True
while running:

    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    enemy_y_pos += enemy_speed * dt

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        enemy = pygame.image.load(os.path.join(current_path, "boom.png"))
        print(f"피한 횟수 :", count)
        running = False

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)
        count += 1

    screen.fill((255,255,255))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    counter = game_font.render(str(count), True, (0,0,0))
    screen.blit(counter, (10,10))

    
    pygame.display.update()
count_msg = game_font.render(str(count), True, (0,0,0))
count_msg_rect = count_msg.get_rect(center = (int(screen_width / 2), int(screen_height / 2)))
screen.blit(count_msg, count_msg_rect)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit