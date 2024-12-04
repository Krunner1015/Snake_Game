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


# Initialize window for game
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initialize clock for speed control of snake
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 40)

def display_score(score):
    score_surf = font.render(f"Your Score: {score}", True, white)
    score_rect = score_surf.get_rect(topleft=(0, 0))
    screen.blit(score_surf, score_rect)

def draw_snake(snake_block, snake_list):
    for x_pos in snake_list:
        pygame.draw.rect(screen, green, [x_pos[0], x_pos[1], snake_block, snake_block])

while True:
    display_score(score)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()