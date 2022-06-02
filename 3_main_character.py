import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# Title 
pygame.display.set_caption("Hobin Game")

# Load background
background = pygame.image.load("C:\\Users\\gatob\\Desktop\\새 폴더\\code\\pygame\\background.png")

# Load character
character = pygame.image.load("C:\\Users\\gatob\\Desktop\\새 폴더\\code\\pygame\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2  - character_width / 2
character_y_pos = screen_height - character_height


# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.blit(background, (0,0))  # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 게임화면을 매 프레임마다 다시 그리기

pygame.quit
