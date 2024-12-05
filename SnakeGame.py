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
width = 650
height = 550
snake_block = 10
snake_speed = 15
snake_pos = (width/2, height/2)
snake_list = []
snake_length = 1
apple_pos = (round(random.randrange(0, width - snake_block)/10)*10, round(random.randrange(0, height - snake_block)/10)*10)
game_over = False
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 10 < x < 678 and 270 < y < 320:
                pygame.init()
                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption("Snake Game")
                screen.fill(background)
                display_score(score)

    pygame.display.flip()
