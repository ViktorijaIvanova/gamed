import pygame
import random


roosa = [100, 155, 120]
pygame.init()

fores = pygame.image.load("puud.png")

# Установка размеров окна
ekraan_WIDTH = 1000
ekraan_HEIGHT = 800
ekraan_SIZE = (ekraan_WIDTH, ekraan_HEIGHT)

# Создание окна
ekraan = pygame.display.set_mode(ekraan_SIZE)
pygame.display.set_caption("миньон и фрукты")
ekraan.fill(roosa)

# Загрузка изображения фрукта и ловушки
banana = pygame.image.load("banana.png")
minion = pygame.image.load("minion.png")

#minban = pygame.mixer.Sound("minban.mp3")
#print("Sound file loaded")

# Установка начальных координат фрукта и ловушки
banana_x = random.randint(0, ekraan_WIDTH)
banana_y = 0
minion_x = ekraan_WIDTH // 2 - minion.get_width() // 2
minion_y = ekraan_HEIGHT - minion.get_height()

# Установка скорости падения фрукта
banana_speed = 2
minion_speed = 5

# Установка начального счета игрока
score = 0

# Создание шрифта для отображения счета
font = pygame.font.Font(None, 40)

# Установка максимального количества упущенных фруктов
max_missed_bananas = 3
missed_bananas = 0

# Основной цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Обновление координат фрукта
    banana_y += banana_speed

    # Если фрукт достиг нижней границы окна, сгенерировать новый фрукт и добавить очки
    if banana_y > ekraan_HEIGHT:
        banana_x = random.randint(0, ekraan_WIDTH)
        banana_y = 0
        score += 1
        missed_bananas += 1

        # Проверка столкновения фрукта и ловушки
    if (minion_x < banana_x + banana.get_width() and
        minion_x + minion.get_width() > banana_x and
        minion_y < banana_y + banana.get_height() and
            minion_y + minion.get_height() > banana_y):

    # Воспроизведение звука при пойманном фрукте
        #pygame.mixer.Sound.play(minban)

    # Генерация новой координаты для фрукта и добавление очков
        banana_x = random.randint(0, ekraan_WIDTH)
        banana_y = 0
        score += 1

# Обработка нажатия клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
       minion_x -= minion_speed
    elif keys[pygame.K_RIGHT]:
       minion_x += minion_speed

# Отрисовка объектов на экране
    ekraan.blit(fores, (0, 0))
    ekraan.blit(banana, (banana_x, banana_y))
    ekraan.blit(minion, (minion_x, minion_y))

# Отображение счета игрока
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    ekraan.blit(score_text, (10, 10))

# Проверка на конец игры
    if missed_bananas >= max_missed_bananas:
        pygame.time.wait(1000)
        ekraan.fill((0, 0, 0))
        gameover_text = font.render("Game Over!", True, (255, 0, 0))
        score_text = font.render("Your score: " + str(score), True, (255, 255, 255))
        ekraan.blit(gameover_text, (ekraan_WIDTH//2 - gameover_text.get_width()//2, ekraan_HEIGHT//2 - gameover_text.get_height()//2))
        ekraan.blit(score_text, (ekraan_WIDTH//2 - score_text.get_width()//2, ekraan_HEIGHT//2 - score_text.get_height()//2 + 50))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    pygame.display.update()



 

"""# Инициализация Pygame
pygame.init()
roheline=[100,255,100] 
# Установка размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Создание окна
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Ловец фруктов")
window.fill(roheline) 

# Загрузка изображения фрукта
banana= pygame.image.load("banana.png")

# Установка начальных координат фрукта
fruit_x = random.randint(0, WINDOW_WIDTH)
fruit_y = 0

# Установка скорости падения фрукта
fruit_speed = 1

# Установка начального счета игрока
score = 0

# Создание шрифта для отображения счета
font = pygame.font.Font(None, 36)

# Основной цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Отрисовка фрукта
    window.blit(banana, (fruit_x, fruit_y))

    # Обновление координат фрукта
    fruit_y += fruit_speed

    # Если фрукт достиг нижней границы окна, сгенерировать новый фрукт и добавить очки
    if fruit_y > WINDOW_HEIGHT:
        fruit_x = random.randint(0, WINDOW_WIDTH)
        fruit_y = 0
        score += 1

    # Отображение счета игрока
    score_text = font.render("Счет: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Обновление окна
    pygame.display.update()"""
