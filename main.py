import pygame 
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test #5")
clock = pygame.time.Clock()
running = True

player_width, player_height = 40, 60
player_x = 800 // 2
player_y = 600 // 2
player_speed = 5
jump_strength = 15
gravity = 0.8
velocity_y = 0
on_ground = False
ground_level = 600 - 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = -jump_strength
        on_ground = False
    velocity_y += gravity
    player_y += velocity_y
    if player_y + player_height >= ground_level:
        player_y = ground_level - player_height
        on_ground = True
        velocity_y = 0
    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (34, 139, 34), (0, ground_level, 800, 50))
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
