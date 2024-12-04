import pygame
import time
import random

# Initialize variables
white = (255,255,255)
black = (0,0,0)
red = (255,50,80)
green = (0,255,0)
blue = (50, 153, 213)
width = 800
height = 600
snake_block = 10
snake_speed = 15
snake_pos = ()
game_over = False
score = 0


# Initialize window for game
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Initialize clock for speed control of snake
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont('bahnschrift', 25)

def display_score(score):
    score_surf = font.render(f"Your Score: {score}", True, white)
    score_rect = score_surf.get_rect(topleft=(0, 0))
    screen.blit(score_surf, score_rect)

def draw_snake(snake_block, snake_list):


while True:
    display_score(score)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()