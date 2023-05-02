import pygame
import random


roosa = [100, 155, 120]
pygame.init()
pygame.mixer.init()
fores = pygame.image.load("foress.png")

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

minban = pygame.mixer.Sound("minban.mp3")
print("Sound file loaded")

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

