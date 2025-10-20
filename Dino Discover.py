import pygame
import subprocess
import os
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

bg_img = pygame.image.load('D:/output/bg.png').convert()
bg_img = pygame.transform.scale(bg_img, (800, 600))

dino_img = pygame.image.load('D:/output/Cute-Dinosaur.png').convert_alpha()
nugget_img = pygame.image.load('D:/output/nuggies.webp').convert_alpha()
dino_img = pygame.transform.scale(dino_img, (160, 160))
nugget_img = pygame.transform.scale(nugget_img, (80, 70))

dino_rect = dino_img.get_rect(topleft=(120, 320))
nuggets_positions = [(90, 100), (680, 120), (150, 500), (600, 480), (400, 90)]

play_btn = pygame.Rect(800 / 2 - 200, 600 / 2 + 60, 150, 60)
menu_btn = pygame.Rect(800 / 2 + 50, 600 / 2 + 60, 150, 60)
menu_box = pygame.Rect(100, 120, 600, 350)

while running:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_btn.collidepoint(event.pos):
                print("Play clicked!")
                os.system("C:/Users/STUDENTS/AppData/Local/Programs/Python/Python311/python.exe D:/output/play.py")
                exit()
            elif menu_btn.collidepoint(event.pos):
                print("Menu clicked!")

    pygame.draw.rect(screen, WHITE, menu_box, border_radius=20)
    pygame.draw.rect(screen, BLACK, menu_box, 4, border_radius=20)

    title_text = title_font.render("Welcome to Dino Discovery!", True, BLACK)
    screen.blit(title_text, (menu_box.centerx - title_text.get_width() / 2, 160))

    pygame.draw.rect(screen, BLUE, play_btn, border_radius=10)
    pygame.draw.rect(screen, GRAY, menu_btn, border_radius=10)

    play_text = button_font.render("PLAY", True, WHITE)
    menu_text = button_font.render("MENU", True, BLACK)
    screen.blit(play_text, (play_btn.x + 25, play_btn.y + 10))
    screen.blit(menu_text, (menu_btn.x + 25, menu_btn.y + 10))

    screen.blit(dino_img, dino_rect)
    for pos in nuggets_positions:
        screen.blit(nugget_img, pos)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()