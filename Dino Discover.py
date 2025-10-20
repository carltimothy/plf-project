import pygame
import time 
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dino Discover!")
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 230, 100)
title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 48)
try:
    dino_img = pygame.image.load("dino.png").convert_alpha()
    nugget_img = pygame.image.load("nugget.png").convert_alpha()
dino_img = pygame.transform.scale(dino_img, (80, 80))
nugget_img = pygame.transform.scale(nugget_img, (50, 50))
dino_rect = dino_img.get_rect(topleft=(100, HEIGHT - 150))
nugget_rect = nugget_img.get_rect(topleft=(250, HEIGHT - 120))
play_btn = pygame.Rect(WIDTH / 2 - 220, HEIGHT / 2 - 40, 150, 60)
menu_btn = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 40, 150, 60)
settings_btn = pygame.Rect(WIDTH / 2 + 120, HEIGHT / 2 - 40, 150, 60)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(event.pos):
                print("Play clicked!")
            elif menu_btn.collidepoint(event.pos):
                print("Menu clicked!")
            elif settings_btn.collidepoint(event.pos):
                print("Settings clicked!")
    title_text = title_font.render("Welcome to Dino Discover!", True, BLACK)
    screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 100))
    pygame.draw.rect(screen, BLUE, play_btn)
    pygame.draw.rect(screen, GRAY, menu_btn)
    pygame.draw.rect(screen, YELLOW, settings_btn)
    play_text = button_font.render("PLAY", True, WHITE)
    menu_text = button_font.render("MENU", True, BLACK)
    settings_text = button_font.render("⚙", True, BLACK)
    screen.blit(play_text, (play_btn.x + 25, play_btn.y + 10))
    screen.blit(menu_text, (menu_btn.x + 25, menu_btn.y + 10))
    screen.blit(settings_text, (settings_btn.x + 55, settings_btn.y + 10))
    screen.blit(dino_img, dino_rect)
    screen.blit(nugget_img, nugget_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
