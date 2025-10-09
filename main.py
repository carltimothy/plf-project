import pygame 
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test #9")
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
max_reach = 150
sky_color = (135, 206, 235)
dirt_color = (139, 69, 19)
player_color = (255, 255, 255)
ground_level = 600 - 50
tile_size = 32
collumns = 800 // tile_size
rows = 600 // tile_size
world = []
for row in range(rows):
    line = []
    for col in range(collumns):
        if row > 12: 
            line.append(1)
        else:
            line.append(0)
    world.append(line)
while running:
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tile_x = mouse_x // tile_size
                    tile_y = mouse_y // tile_size
                if 0 <= tile_x < collumns and 0 <= tile_y < rows:
                    player_center_x = player_x + player_width // 2
                    player_center_y = player_y + player_height // 2
                    tile_center_x = tile_x * tile_size + tile_size // 2
                    tile_center_y = tile_y * tile_size + tile_size // 2
                    distance = ((player_center_x - tile_center_x) ** 2 + (player_center_y - tile_center_y) ** 2) ** 0.5
                    if distance <= max_reach and world[tile_y][tile_x] == 1:
                        world[tile_y][tile_x] = 0
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
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_ground = False
    for r in range(rows):
        for c in range(collumns):
            if world[r][c] == 1:
                block_rect = pygame.Rect(c * tile_size, r * tile_size, tile_size, tile_size)
                if player_rect.colliderect(block_rect):
                    if velocity_y > 0 and player_rect.bottom > block_rect.top:
                        player_rect.bottom = block_rect.top
                        velocity_y = 0
                        on_ground = True
    player_y = player_rect.y
    screen.fill((135, 206, 235))
    for r in range(rows):
        for c in range(collumns):
            if world[r][c] == 1:
                pygame.draw.rect(screen, dirt_color, (c * tile_size, r * tile_size, tile_size, tile_size))
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    tile_x = mouse_x // tile_size
    tile_y = mouse_y // tile_size
    if 0 <= tile_x < collumns and 0 <= tile_y < rows:
        player_center_x = player_x + player_width // 2
        player_center_y = player_y + player_height // 2
        tile_center_x = tile_x * tile_size + tile_size // 2
        tile_center_y = tile_y * tile_size + tile_size // 2
        distance = ((player_center_x - tile_center_x) ** 2 + (player_center_y - tile_center_y) ** 2) ** 0.5
        if distance <= max_reach and world[tile_y][tile_x] == 1:
            pygame.draw.rect(screen, (255, 255, 0), (tile_x * tile_size, tile_y * tile_size, tile_size, tile_size), 2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
