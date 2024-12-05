import pygame
import time
import random

# Initialize variables
white = (255,255,255)
black = (0,0,0)
apple = pygame.image.load("apple.png")
background = (87, 138, 52)
board_light = (170, 215, 81)
board_dark = (162, 209, 73)
snake = (76, 120, 232)
width = 680
height = 550
snake_block = 34
snake_speed = 15
y_change = 0
x_change = 0
snake_pos = [width/2, height/2]
snake_list = []
snake_length = 1
apple_pos = [round(random.randrange(0, width - snake_block)/10)*10, round(random.randrange(0, height - snake_block)/10)*10]
score = 0

# Initialize window and start screen for game
pygame.init()
screen = pygame.display.set_mode((688, 330))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 40)
screen.fill(board_light)
screen.blit(pygame.image.load("Snake_intro.png"), (0, 0))
pygame.draw.rect(screen, snake, [10, 270, 668, 50], 0, 5)
play_surf = font.render("Play", True, white)
screen.blit(play_surf, play_surf.get_rect(center=(344, 295)))

# Initialize clock for speed control of snake
clock = pygame.time.Clock()

def display_score(score):
    score_surf = font.render(f"Your Score: {score}", True, white)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

def draw_snake(snake_block, snake_list):
    for x_pos in snake_list:
        pygame.draw.rect(screen, green, [x_pos[0], x_pos[1], snake_block, snake_block])

def in_game():
    global snake_pos, x_change, y_change, snake_length, snake_list, apple_pos, score
    game_over = False
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")
    running = True
    while running:
        screen.fill(background)
        display_score(snake_length - 1)
        for row in range(15):
            for col in range(20):
                if (row + col) % 2 == 0:
                    color = board_light
                else:
                    color = board_dark
                pygame.draw.rect(screen, color, (col*34, 40+row*34, 34, 34))

        while game_over:
            screen.fill(white)
            screen.blit(font.render("Game Over!", True, snake), [width/6, height/3])
            display_score(snake_length - 1)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_UP:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    x_change = -snake_block
                    y_change = 0

        if snake_pos[0] >= width or snake_pos[0] < 0 or snake_pos[1] >= height or snake_pos[1] < 0:
            game_over = True

        snake_pos[0] += x_change
        snake_pos[1] += y_change

        pygame.draw.rect(screen, snake, [apple_pos[0], apple_pos[1], snake_block, snake_block])
        snake_head = []
        snake_head.append(snake_pos[0])
        snake_head.append(snake_pos[1])
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.flip()

        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            apple_pos = [round(random.randrange(0, width - snake_block)/10)*10, round(random.randrange(0, height - snake_block)/10)*10]
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 10 < x < 678 and 270 < y < 320:
                in_game()

    pygame.display.flip()
