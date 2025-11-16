import pygame

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
main_ui_img = pygame.image.load('assets/main-ui.png').convert_alpha()
check_img = pygame.image.load('assets/check.gif').convert_alpha()
x_img = pygame.image.load('assets/x.gif').convert_alpha()
dino_img = pygame.transform.scale(dino_img, (500, 500))
dino_left_img = pygame.transform.scale(dino_left_img, (500, 500))
nugget_img = pygame.transform.scale(nugget_img, (100, 90))
button_bg = pygame.transform.scale(button_bg, (150, 60))
main_ui_img = pygame.transform.scale(main_ui_img, (600, 350))
check_img = pygame.transform.scale(check_img, (80, 80))
x_img = pygame.transform.scale(x_img, (80, 80))
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
in_difficulty = False
in_quiz = False
volume_slider = pygame.Rect(300, 300, 200, 10)
volume_knob_x = 400
dragging_volume = False
easy_btn = pygame.Rect(800 / 2 - 225, 300, 150, 60)
normal_btn = pygame.Rect(800 / 2 - 75, 300, 150, 60)
hard_btn = pygame.Rect(800 / 2 + 75, 300, 150, 60)
font_q = pygame.font.Font(None, 40)
font_a = pygame.font.Font(None, 35)
easy_questions = [
    {"q":"question1","choices":["ans1","ans2","ans3","ans4"],"answer":"ans3"},
    {"q":"question2","choices":["ans1","ans2","ans3","ans4"],"answer":"ans2"},
    {"q":"question3","choices":["ans1","ans2","ans3","ans4"],"answer":"ans2"}
]
normal_questions = [
    {"q":"question1normal","choices":["ans1","ans2","ans3","ans4"],"answer":"ans1"},
    {"q":"question2normal","choices":["ans1","ans2","ans3","ans4"],"answer":"ans2"},
    {"q":"question3normal","choices":["ans1","ans2","ans3","ans4"],"answer":"ans3"}
]
hard_questions = [
    {"q":"question1hard","choices":["ans1","ans2","ans3","ans4"],"answer":"ans4"},
    {"q":"question2hard","choices":["ans1","ans2","ans3","ans4"],"answer":"ans3"},
    {"q":"question3hard","choices":["ans1","ans2","ans3","ans4"],"answer":"ans2"}
]
score = 0
total_questions = 0
quiz_stat = False
time = 0
difficulty = None
current_q = 0
show_feedback = False
feedback_time = 0
feedback_correct = False
answered = False
def get_answer_buttons():
    btns = []
    start_x, start_y = 210, 240
    w, h = 200, 60
    gap_x, gap_y = 220, 80
    for i in range(4):
        col = i % 2
        row = i // 2
        rect = pygame.Rect(start_x + col * gap_x, start_y + row * gap_y, w, h)
        btns.append(rect)
    return btns
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
def draw_difficulty_menu():
    screen.blit(bg_img, (0, 0))
    screen.blit(main_ui_img, (100, 120))
    title_text = title_font.render("Select Difficulty", True, WHITE)
    screen.blit(title_text, (400 - title_text.get_width() / 2, 180))
    screen.blit(button_bg, easy_btn)
    screen.blit(button_bg, normal_btn)
    screen.blit(button_bg, hard_btn)
    easy_text = button_font.render("EASY", True, BLACK)
    normal_text = button_font.render("NORMAL", True, BLACK)
    hard_text = button_font.render("HARD", True, BLACK)
    screen.blit(easy_text, (easy_btn.centerx - easy_text.get_width() / 2, easy_btn.centery - easy_text.get_height() / 2))
    screen.blit(normal_text, (normal_btn.centerx - normal_text.get_width() / 2, normal_btn.centery - normal_text.get_height() / 2))
    screen.blit(hard_text, (hard_btn.centerx - hard_text.get_width() / 2, hard_btn.centery - hard_text.get_height() / 2))
    back_btn = pygame.Rect(800 / 2 - 75, 450, 150, 60)
    screen.blit(button_bg, back_btn)
    back_text = button_font.render("BACK", True, BLACK)
    screen.blit(back_text, (back_btn.centerx - back_text.get_width() / 2, back_btn.centery - back_text.get_height() / 2))
    return back_btn
def draw_score_and_done():
    global quiz_stat, time, in_quiz, in_difficulty, current_q
    if quiz_stat:
        text = f"Your Score: {score}/{total_questions}"
        max_width = 400
        font_size = 40
        font_used = pygame.font.Font(None, font_size)
        while font_used.size(text)[0] > max_width and font_size > 10:
            font_size -= 2
            font_used = pygame.font.Font(None, font_size)
        text_width, text_height = font_used.size(text)
        padding_w = 60 
        padding_h = 20
        button_temp = pygame.transform.scale(button_bg, (text_width + padding_w, text_height + padding_h))
        screen.blit(button_temp, (400 - button_temp.get_width() / 2, 480))
        result_text = font_used.render(text, True, BLACK)
        screen.blit(result_text, (400 - result_text.get_width() / 2, 480 + (button_temp.get_height() - result_text.get_height()) / 2))
        if pygame.time.get_ticks() - time > 3000:
            quiz_stat = False
            in_quiz = False
            in_difficulty = False
            current_q = 0
def draw_easy_quiz():
    global show_feedback, feedback_correct, feedback_time, current_q, answered
    screen.blit(bg_img, (0, 0))
    screen.blit(main_ui_img, (100, 120))
    if current_q < len(easy_questions):
        q = easy_questions[current_q]
        words = q["q"].split(" ")
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            if font_q.size(test_line)[0] < 500:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)
        y_offset = 170
        for l in lines:
            q_text = font_q.render(l.strip(), True, WHITE)
            screen.blit(q_text, (400 - q_text.get_width() / 2, y_offset))
            y_offset += q_text.get_height() + 5
        answer_btns = get_answer_buttons()
        for i, c in enumerate(q["choices"]):
            btn = answer_btns[i]
            screen.blit(button_bg, btn)
            max_width = btn.width - 65
            txt_surface = font_a.render(c, True, BLACK)
            if txt_surface.get_width() > max_width:
                scale = max_width / txt_surface.get_width()
                new_size = max(20, int(font_a.size(c)[1] * scale))
                temp_font = pygame.font.Font(None, new_size)
                txt_surface = temp_font.render(c, True, BLACK)
            screen.blit(txt_surface, (btn.centerx - txt_surface.get_width() / 2 - 25, btn.centery - txt_surface.get_height() / 2 - 3))
    else:
        done_txt = font_q.render(".......!", True, BLACK)
        screen.blit(done_txt, (400 - done_txt.get_width() / 2, 280))
        global quiz_stat, time
        if not quiz_stat:
            quiz_stat = True
            time = pygame.time.get_ticks()
    if show_feedback:
        img = check_img if feedback_correct else x_img
        screen.blit(img, (360, 240))
        if pygame.time.get_ticks() - feedback_time > 1000:
            show_feedback = False
            answered = False
            if feedback_correct:
                current_q += 1
def draw_normal_quiz():
    global show_feedback, feedback_correct, feedback_time, current_q, answered
    screen.blit(bg_img, (0, 0))
    screen.blit(main_ui_img, (100, 120))
    if current_q < len(normal_questions):
        q = normal_questions[current_q]
        words = q["q"].split(" ")
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            if font_q.size(test_line)[0] < 500:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)
        y_offset = 170
        for l in lines:
            q_text = font_q.render(l.strip(), True, WHITE)
            screen.blit(q_text, (400 - q_text.get_width() / 2, y_offset))
            y_offset += q_text.get_height() + 5
        answer_btns = get_answer_buttons()
        for i, c in enumerate(q["choices"]):
            btn = answer_btns[i]
            screen.blit(button_bg, btn)
            max_width = btn.width - 65
            txt_surface = font_a.render(c, True, BLACK)
            if txt_surface.get_width() > max_width:
                scale = max_width / txt_surface.get_width()
                new_size = max(20, int(font_a.size(c)[1] * scale))
                temp_font = pygame.font.Font(None, new_size)
                txt_surface = temp_font.render(c, True, BLACK)
            screen.blit(txt_surface, (btn.centerx - txt_surface.get_width() / 2 - 25, btn.centery - txt_surface.get_height() / 2 - 3))
    else:
        done_txt = font_q.render("q2 done!", True, BLACK)
        screen.blit(done_txt, (400 - done_txt.get_width() / 2, 280))
        global quiz_stat, time
        if not quiz_stat:
            quiz_stat = True
            time = pygame.time.get_ticks()
    if show_feedback:
        img = check_img if feedback_correct else x_img
        screen.blit(img, (360, 240))
        if pygame.time.get_ticks() - feedback_time > 1000:
            show_feedback = False
            answered = False
            if feedback_correct:
                current_q += 1
def draw_hard_quiz():
    global show_feedback, feedback_correct, feedback_time, current_q, answered
    screen.blit(bg_img, (0, 0))
    screen.blit(main_ui_img, (100, 120))
    if current_q < len(hard_questions):
        q = hard_questions[current_q]
        words = q["q"].split(" ")
        lines = []
        line = ""
        for word in words:
            test_line = line + word + " "
            if font_q.size(test_line)[0] < 500:
                line = test_line
            else:
                lines.append(line)
                line = word + " "
        lines.append(line)
        y_offset = 170
        for l in lines:
            q_text = font_q.render(l.strip(), True, WHITE)
            screen.blit(q_text, (400 - q_text.get_width() / 2, y_offset))
            y_offset += q_text.get_height() + 5
        answer_btns = get_answer_buttons()
        for i, c in enumerate(q["choices"]):
            btn = answer_btns[i]
            screen.blit(button_bg, btn)
            max_width = btn.width - 65
            txt_surface = font_a.render(c, True, BLACK)
            if txt_surface.get_width() > max_width:
                scale = max_width / txt_surface.get_width()
                new_size = max(20, int(font_a.size(c)[1] * scale))
                temp_font = pygame.font.Font(None, new_size)
                txt_surface = temp_font.render(c, True, BLACK)
            screen.blit(txt_surface, (btn.centerx - txt_surface.get_width() / 2 - 25, btn.centery - txt_surface.get_height() / 2 - 3))
    else:
        done_txt = font_q.render("hard questions done!", True, BLACK)
        screen.blit(done_txt, (400 - done_txt.get_width() / 2, 280))
        global quiz_stat, time
        if not quiz_stat:
            quiz_stat = True
            time = pygame.time.get_ticks()
    if show_feedback:
        img = check_img if feedback_correct else x_img
        screen.blit(img, (360, 240))
        if pygame.time.get_ticks() - feedback_time > 1000:
            show_feedback = False
            answered = False
            if feedback_correct:
                current_q += 1
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not in_settings and not in_difficulty and not in_quiz:
                if play_btn.collidepoint(event.pos):
                    in_difficulty = True
                elif menu_btn.collidepoint(event.pos):
                    in_settings = True
            elif in_settings:
                back_btn = pygame.Rect(800 / 2 - 75, 600 / 2 + 60, 150, 60)
                if back_btn.collidepoint(event.pos):
                    in_settings = False
                elif volume_slider.collidepoint(event.pos):
                    dragging_volume = True
            elif in_difficulty:
                back_btn = pygame.Rect(800 / 2 - 75, 450, 150, 60)
                if back_btn.collidepoint(event.pos):
                    in_difficulty = False
                elif easy_btn.collidepoint(event.pos):
                    difficulty = "easy"
                    in_difficulty = False
                    in_quiz = True
                    score = 0
                    total_questions = len(easy_questions)
                elif normal_btn.collidepoint(event.pos):
                    difficulty = "normal"
                    in_difficulty = False
                    in_quiz = True
                    score = 0
                    total_questions = len(normal_questions)
                elif hard_btn.collidepoint(event.pos):
                    difficulty = "hard"
                    in_difficulty = False
                    in_quiz = True
                    score = 0
                    total_questions = len(hard_questions)
            elif in_quiz and not show_feedback and not answered:
                answer_btns = get_answer_buttons()
                if difficulty == "easy":
                    set = easy_questions
                elif difficulty == "normal":
                    set = normal_questions
                elif difficulty == "hard":
                    set = hard_questions
                if current_q < len(set):
                    answer_btns = get_answer_buttons()
                    for i, btn in enumerate(answer_btns):
                        if btn.collidepoint(event.pos):
                            selected = set[current_q]["choices"][i]
                            feedback_correct = (selected == set[current_q]["answer"])
                            if feedback_correct:
                                score += 1
                            show_feedback = True
                            feedback_time = pygame.time.get_ticks()
                            answered = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging_volume = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging_volume and in_settings:
                volume_knob_x = min(max(event.pos[0], volume_slider.x), volume_slider.x + volume_slider.width)
                volume = (volume_knob_x - volume_slider.x) / volume_slider.width
                pygame.mixer.music.set_volume(volume if volume > 0 else 0)
    if not in_settings and not in_difficulty and not in_quiz:
        draw_main_menu()
    elif in_settings:
        back_btn = draw_settings_menu(volume_knob_x)
    elif in_difficulty:
        back_btn = draw_difficulty_menu()
    elif in_quiz:
        if difficulty == "easy":
            draw_easy_quiz()
        elif difficulty == "normal":
            draw_normal_quiz()
        elif difficulty == "hard":
            draw_hard_quiz()
        draw_score_and_done()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
