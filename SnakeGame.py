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
snake_speed = 10

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
    for pos in snake_list:
        pygame.draw.rect(screen, snake, [pos[0], pos[1], snake_block, snake_block])

def in_game():
    global snake_length
    screen = pygame.display.set_mode((width, height))
    game_over = False
    y_change = 0
    x_change = 0
    snake_pos = [204, 278]
    snake_list = []
    snake_length = 1
    apple_pos = [476, 278]
    direction = "RIGHT"

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and direction != "RIGHT":
                x_change =- snake_block
                y_change = 0
                direction = "LEFT"
            elif keys[pygame.K_RIGHT] and direction != "LEFT":
                x_change =+ snake_block
                y_change = 0
                direction = "RIGHT"
            elif keys[pygame.K_UP] and direction != "DOWN":
                y_change =- snake_block
                x_change = 0
                direction = "UP"
            elif keys[pygame.K_DOWN] and direction != "UP":
                y_change =+ snake_block
                x_change = 0
                direction = "DOWN"

        snake_pos[0] += x_change
        snake_pos[1] += y_change

        screen.fill(background)
        display_score(snake_length - 1)

        for row in range(15):
            for col in range(20):
                if (row + col) % 2 == 0:
                    color = board_light
                else:
                    color = board_dark
                pygame.draw.rect(screen, color, (col * 34, 40 + row * 34, 34, 34))

        screen.blit(apple, apple.get_rect(topleft=(apple_pos[0], apple_pos[1])))

        snake_head = [snake_pos[0], snake_pos[1]]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
                break

        if width > snake_pos[0] >= 0 and height > snake_pos[1] >= 40:
            draw_snake(snake_block, snake_list)
        else:
            break

        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            apple_pos = [random.choice(range(0, 681, snake_block)), random.choice(range(40, 551, snake_block))]
            # for i in range(0, len(snake_list), 2):
            #     if apple_pos[0] == snake_list[i][0] and apple_pos[1] == snake_list[i][1]:
            #         apple_pos = [random.choice(range(0, 681, snake_block)), random.choice(range(40, 551, snake_block))]
            while apple_pos in snake_list:
                apple_pos = [random.choice(range(0, 681, snake_block)), random.choice(range(40, 551, snake_block))]
            snake_length += 1

        pygame.display.flip()

        clock.tick(snake_speed)
    end_game()

def end_game():
    font = pygame.font.SysFont(None, 40)
    screen = pygame.display.set_mode((650, 470))
    screen.fill(board_light)
    screen.blit(pygame.image.load("Snake.png"), (0, 0))
    pygame.draw.rect(screen, snake, [10, 410, 310, 50], 0, 5)
    play_surf = font.render("Play again!", True, white)
    screen.blit(play_surf, play_surf.get_rect(center=(165, 435)))
    pygame.draw.rect(screen, snake, [330, 410, 310, 50], 0, 5)
    exit_surf = font.render("Exit", True, white)
    screen.blit(exit_surf, exit_surf.get_rect(center=(485, 435)))
    display_score(snake_length - 1)
    font = pygame.font.SysFont(None, 80)
    screen.blit(font.render("Game Over!", True, white), (160, 60))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 < x < 320 and 410 < y < 460:
                    in_game()

                if 330 < x < 640 and 410 < y < 460:
                    pygame.quit()
                    quit()

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 10 < x < 678 and 270 < y < 320:
                in_game()