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
GRAY = (180, 180, 180)
PURPLE = (221, 51, 255)
title_font = pygame.font.Font(None, 48)
button_font = pygame.font.Font(None, 40)
settings_button_font = pygame.font.Font(None, 40)
bg_img = pygame.image.load('assets/menu.jpeg').convert()
bg_img = pygame.transform.scale(bg_img, (800, 600))
dino_img = pygame.image.load('assets/Cute-Dinosaur.png').convert_alpha()
dino_left_img = pygame.image.load('assets/Cute-Dinosaur-Left.png').convert_alpha()
nugget_img = pygame.image.load('assets/nuggies.webp').convert_alpha()
button_bg = pygame.image.load('assets/button-large.png').convert_alpha()
dino_img = pygame.transform.scale(dino_img, (500, 500))
dino_left_img = pygame.transform.scale(dino_left_img, (500, 500))
nugget_img = pygame.transform.scale(nugget_img, (100, 90))
button_bg = pygame.transform.scale(button_bg, (150, 60))
pygame.mixer.music.load("assets/bg_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
dino_rect = dino_img.get_rect(topleft=(550, 200))
dino_rect_left = dino_left_img.get_rect(topleft=(-250, 200))
nuggets_positions = [(0, 100), (175, 10), (700, 120), (275, 470),
                     (150, 500), (420, 495), (550, 480), (400, 20), (600, 20)]
play_btn = pygame.Rect(800 / 2 - 200, 600 / 2 + 60, 150, 60)
menu_btn = pygame.Rect(800 / 2 + 50, 600 / 2 + 60, 150, 60)
menu_box = pygame.Rect(100, 120, 600, 350)
in_settings = False
volume_slider = pygame.Rect(300, 300, 200, 10)
volume_knob_x = 400
def draw_main_menu():
    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, WHITE, menu_box, border_radius=20)
    pygame.draw.rect(screen, BLACK, menu_box, 4, border_radius=20)
    title_text = title_font.render("Welcome to Dino Discovery!", True, BLACK)
    screen.blit(title_text, (menu_box.centerx - title_text.get_width() / 2, 160))
    screen.blit(button_bg, play_btn)
    screen.blit(button_bg, menu_btn)
    play_text = button_font.render("PLAY", True, BLACK)
    menu_text = settings_button_font.render("Settings", True, BLACK)
    screen.blit(play_text, (play_btn.centerx - play_text.get_width() / 2, play_btn.centery - play_text.get_height() / 2))
    screen.blit(menu_text, (menu_btn.centerx - menu_text.get_width() / 2, menu_btn.centery - menu_text.get_height() / 2))
    screen.blit(dino_img, dino_rect)
    screen.blit(dino_left_img, dino_rect_left)
    for pos in nuggets_positions:
        screen.blit(nugget_img, pos)
def draw_settings_menu(volume_knob_x):
    screen.blit(bg_img, (0, 0))
    pygame.draw.rect(screen, WHITE, menu_box, border_radius=20)
    pygame.draw.rect(screen, BLACK, menu_box, 4, border_radius=20)
    title_text = title_font.render("Settings", True, BLACK)
    screen.blit(title_text, (menu_box.centerx - title_text.get_width() / 2, 160))
    pygame.draw.rect(screen, GRAY, volume_slider)
    pygame.draw.circle(screen, PURPLE, (int(volume_knob_x), volume_slider.y + 5), 10)
    vol_text = settings_button_font.render("Volume", True, BLACK)
    screen.blit(vol_text, (volume_slider.x - 120, volume_slider.y - 10))
    volume = (volume_knob_x - volume_slider.x) / volume_slider.width
    volume_percent = settings_button_font.render(f"{int(volume*100)}%", True, BLACK)
    screen.blit(volume_percent, (volume_slider.x + volume_slider.width + 20, volume_slider.y - 10))
    back_btn = pygame.Rect(800 / 2 - 75, 600 / 2 + 60, 150, 60)
    screen.blit(button_bg, back_btn)
    back_text = button_font.render("BACK", True, BLACK)
    screen.blit(back_text, (back_btn.centerx - back_text.get_width() / 2, back_btn.centery - back_text.get_height() / 2))
    return back_btn
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not in_settings:
                if play_btn.collidepoint(event.pos):
                    print("Play")
                    os.system('play.py')
                elif menu_btn.collidepoint(event.pos):
                    in_settings = True
            else:
                back_btn = pygame.Rect(800 / 2 - 75, 600 / 2 + 60, 150, 60)
                if back_btn.collidepoint(event.pos):
                    in_settings = False
                elif volume_slider.collidepoint(event.pos[0], volume_slider.y):
                    volume_knob_x = min(max(event.pos[0], volume_slider.x), volume_slider.x + volume_slider.width)
                    volume = (volume_knob_x - volume_slider.x) / volume_slider.width
                    pygame.mixer.music.set_volume(volume if volume > 0 else 0)
        elif event.type == pygame.MOUSEMOTION and in_settings and event.buttons[0]:
            if volume_slider.collidepoint(event.pos[0], volume_slider.y):
                volume_knob_x = min(max(event.pos[0], volume_slider.x), volume_slider.x + volume_slider.width)
                volume = (volume_knob_x - volume_slider.x) / volume_slider.width
                pygame.mixer.music.set_volume(volume if volume > 0 else 0)
    if not in_settings:
        draw_main_menu()
    else:
        back_btn = draw_settings_menu(volume_knob_x)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
