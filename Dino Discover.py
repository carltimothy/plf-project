import pygame
import os
pygame.init()

icon = pygame.image.load("assets/Cute-Dinosaur-Left.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dino Discovery!")
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (221, 51, 255)
ORANGE = (255, 153, 51)
title_font = pygame.font.Font(None, 48)
button_font = pygame.font.Font(None, 48)
settings_button_font = pygame.font.Font(None, 40)
bg_img = pygame.image.load('assets/menu.jpeg').convert()
bg_img = pygame.transform.scale(bg_img, (800, 600))
dino_img = pygame.image.load('assets/Cute-Dinosaur.png').convert_alpha()
dino_left_img = pygame.image.load('assets/Cute-Dinosaur-Left.png').convert_alpha()
nugget_img = pygame.image.load('assets/nuggies.webp').convert_alpha()
dino_img = pygame.transform.scale(dino_img, (500, 500))
dino_left_img = pygame.transform.scale(dino_left_img, (500, 500))
nugget_img = pygame.transform.scale(nugget_img, (100, 90))
dino_rect = dino_img.get_rect(topleft=(550, 200))
dino_rect_left = dino_left_img.get_rect(topleft=(-250, 200))
nuggets_positions = [(0, 100), (175, 10), (700, 120), (275, 470),
                     (150, 500), (420, 495), (550, 480), (400, 20), (600, 20)]
play_btn = pygame.Rect(800 / 2 - 200, 600 / 2 + 60, 150, 60)
menu_btn = pygame.Rect(800 / 2 + 50, 600 / 2 + 60, 150, 60)
menu_box = pygame.Rect(100, 120, 600, 350)
print("Debug Mode:")
while running:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(event.pos):
                print("Play")
                os.system("C:/Users/STUDENTS/AppData/Local/Programs/Python/Python311/python.exe assets/play.py")
            elif menu_btn.collidepoint(event.pos):
                print("Settings")
    pygame.draw.rect(screen, WHITE, menu_box, border_radius=20)
    pygame.draw.rect(screen, BLACK, menu_box, 4, border_radius=20)
    title_text = title_font.render("Welcome to Dino Discovery!", True, BLACK)
    screen.blit(title_text, (menu_box.centerx - title_text.get_width() / 2, 160))
    pygame.draw.rect(screen, PURPLE, play_btn, border_radius=10)
    pygame.draw.rect(screen, ORANGE, menu_btn, border_radius=10)
    play_text = button_font.render("PLAY", True, WHITE)
    menu_text = settings_button_font.render("Settings", True, BLACK)
    screen.blit(play_text, (play_btn.x + 25, play_btn.y + 10))
    screen.blit(menu_text, (menu_btn.x + 25, menu_btn.y + 10))
    screen.blit(dino_img, dino_rect)
    screen.blit(dino_left_img, dino_rect_left)
    for pos in nuggets_positions:
        screen.blit(nugget_img, pos)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
