import pygame  # Pygame кітапханасын қосамыз

pygame.init()  # Pygame бастаймыз

#  Экран параметрлері
WIDTH, HEIGHT = 800, 600  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Қызыл шарды жылжыту")  

#  Шар параметрлері
BALL_RADIUS = 25  
BALL_COLOR = (255, 0, 0)  # Қызыл түс
BG_COLOR = (255, 255, 255)  # Ақ фон
STEP = 20  # Бір басқанда 20px-ге жылжиды

# 🏁 Бастапқы орын (экран ортасы)
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  

#  Ойын циклі
running = True
while running:
    screen.fill(BG_COLOR)  # Экранды ақ түске бояу
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)  # Шарды салу
    pygame.display.flip()  # Экранды жаңарту

    #  Пернелерді бақылау
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False  # Бағдарламаны жабу
        elif event.type == pygame.KEYDOWN:  
            #  Жоғары (UP)
            if event.key == pygame.K_UP and ball_y - STEP - BALL_RADIUS >= 0:
                ball_y -= STEP  
            #  Төмен (DOWN)
            elif event.key == pygame.K_DOWN and ball_y + STEP + BALL_RADIUS <= HEIGHT:
                ball_y += STEP  
            #  Солға (LEFT)
            elif event.key == pygame.K_LEFT and ball_x - STEP - BALL_RADIUS >= 0:
                ball_x -= STEP  
            #  Оңға (RIGHT)
            elif event.key == pygame.K_RIGHT and ball_x + STEP + BALL_RADIUS <= WIDTH:
                ball_x += STEP  

pygame.quit()  # Ойынды жабу
