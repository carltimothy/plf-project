import pygame
import time 
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test #10")
clock = pygame.time.Clock()
running = True

player_width, player_height = 40, 60
player_x = 800 // 2
player_y = 600 // 2
player_speed = 5
jump_strength = 15
gravity = 0.8
velocity_y = 0
camera_x = 0
on_ground = False
max_reach = 150
sky_color = (135, 206, 235)
dirt_color = (139, 69, 19)
player_color = (255, 255, 255)
tile_size = 32
columns = 200
rows = 600 // tile_size
world = []
for row in range(rows):
    line = []
    for col in range(columns):
        if row > 12: 
            line.append(1)
        else:
            line.append(0)
    world.append(line)
npc_rect = pygame.Rect(600, (13 * tile_size) - player_height, 40, 60) 
npc_color = (255, 0, 0)
quest_active = False
question = "What is 5 + 7?"
answer = "12"
player_answer = ""
font = pygame.font.SysFont(None, 32)
feedback = ""
feedback_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not quest_active:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_x = (mouse_x + camera_x) // tile_size
                tile_y = mouse_y // tile_size
                if 0 <= tile_x < columns and 0 <= tile_y < rows:
                    px = player_x + player_width // 2
                    py = player_y + player_height // 2
                    tx = tile_x * tile_size + tile_size // 2
                    ty = tile_y * tile_size + tile_size // 2
                    distance = ((px - tx)**2 + (py - ty)**2)**0.5
                    if distance <= max_reach and world[tile_y][tile_x] == 1:
                        world[tile_y][tile_x] = 0
        if quest_active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if player_answer == answer:
                    feedback = "Correct! You earned points!"
                else:
                    feedback = "Wrong answer!"
                feedback_timer = time.time()
                quest_active = False
                player_answer = ""
            elif event.key == pygame.K_BACKSPACE:
                player_answer = player_answer[:-1]
            else:
                player_answer += event.unicode
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = -jump_strength
        on_ground = False
    camera_x = player_x - (800 // 2) + (player_width // 2)
    camera_x = max(0, min(camera_x, columns * tile_size - 800))
    velocity_y += gravity
    player_y += velocity_y
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_ground = False
    start_col = max(0, player_rect.left // tile_size - 1)
    end_col = min(columns, player_rect.right // tile_size + 2)
    start_row = max(0, player_rect.top // tile_size - 1)
    end_row = min(rows, player_rect.bottom // tile_size + 2)
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if world[r][c] == 1:
                block_rect = pygame.Rect(c * tile_size, r * tile_size, tile_size, tile_size)
                if player_rect.colliderect(block_rect):
                    if velocity_y > 0 and player_rect.bottom > block_rect.top:
                        player_rect.bottom = block_rect.top
                        velocity_y = 0
                        on_ground = True
                    elif velocity_y < 0 and player_rect.top < block_rect.bottom:
                        player_rect.top = block_rect.bottom
                        velocity_y = 0
    player_y = player_rect.y
    if player_rect.colliderect(npc_rect):
        if keys[pygame.K_e] and not quest_active:
            quest_active = True
    screen.fill(sky_color)
    vis_start = camera_x // tile_size
    vis_end = (camera_x + 800) // tile_size + 1
    for r in range(rows):
        for c in range(vis_start, min(vis_end, columns)):
            if world[r][c] == 1:
                pygame.draw.rect(screen, dirt_color, (c * tile_size - camera_x, r * tile_size, tile_size, tile_size))
    npc_screen_rect = pygame.Rect(npc_rect.x - camera_x, npc_rect.y, npc_rect.width, npc_rect.height)
    pygame.draw.rect(screen, npc_color, npc_screen_rect)
    pygame.draw.rect(screen, player_color, (player_x - camera_x, player_y, player_width, player_height))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    tile_x = (mouse_x + camera_x) // tile_size
    tile_y = mouse_y // tile_size
    if 0 <= tile_x < columns and 0 <= tile_y < rows:
        px = player_x + player_width // 2
        py = player_y + player_height // 2
        tx = tile_x * tile_size + tile_size // 2
        ty = tile_y * tile_size + tile_size // 2
        distance = ((px - tx)**2 + (py - ty)**2)**0.5
        if distance <= max_reach and world[tile_y][tile_x] == 1:
            pygame.draw.rect(screen, (255, 255, 0), (tile_x * tile_size - camera_x, tile_y * tile_size, tile_size, tile_size), 2)
    if quest_active:
        pygame.draw.rect(screen, (0, 0, 0), (150, 100, 500, 200))
        pygame.draw.rect(screen, (255, 255, 255), (150, 100, 500, 200), 3)
        question_surface = font.render(question, True, (255, 255, 255))
        answer_surface = font.render(player_answer, True, (255, 255, 0))
        screen.blit(question_surface, (170, 120))
        screen.blit(answer_surface, (170, 170))
    if feedback != "" and time.time() - feedback_timer < 5:
        feedback_surface = font.render(feedback, True, (255, 255, 0))
        screen.blit(feedback_surface, (170, 220))
    elif feedback != "" and time.time() - feedback_timer >= 5:
        feedback = "" 
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
