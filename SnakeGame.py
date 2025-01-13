import pygame
import time
import random

#initialize variables
white = (255,255,255)
black = (0,0,0)
blue = (76, 120, 232)
apple = pygame.image.load("apple.png")
background = (87, 138, 52)
board_light = (170, 215, 81)
board_dark = (162, 209, 73)
width = 680
height = 550
snake_block = 34
snake_speed = 9

snake_sprite = pygame.image.load("Snake_graphics.png")
sprite_size = 64
scale_factor = snake_block/sprite_size #scale sprite to match the grid

#initialize window and start screen for game
pygame.init()
screen = pygame.display.set_mode((688, 330))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, 40)
screen.fill(board_light)
screen.blit(pygame.image.load("Snake_intro.png"), (0, 0))
pygame.draw.rect(screen, blue, [10, 270, 668, 50], 0, 5)
play_surf = font.render("Play", True, white)
screen.blit(play_surf, play_surf.get_rect(center=(344, 295)))

#initialize clock for speed control of snake
clock = pygame.time.Clock()

#displays the score in the top left of the screen
def display_score(score):
    score_surf = font.render(f"Your Score: {score}", True, white)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

#displays the snake on the screen
def draw_snake(snake_block, snake_list):
    for i, segment in enumerate(snake_list):
        x = segment[0]
        y = segment[1]
        snake_pos_x = x
        snake_pos_y = y

        sprite_x, sprite_y = 0, 0 #initialize sprite coordinates

        if i == 0: #head
            next_segment = snake_list[i + 1] #next segment
            if x > next_segment[0]: #right
                sprite_x, sprite_y = 4, 0
            elif x < next_segment[0]: #left
                sprite_x, sprite_y = 3, 1
            elif y < next_segment[1]: #up
                sprite_x, sprite_y = 3, 0
            elif y > next_segment[1]: #down
                sprite_x, sprite_y = 4, 1

        elif i == len(snake_list) - 1: #tail
            last_segment = snake_list[i - 1] #previous segment
            if last_segment[0] > x: #right
                sprite_x, sprite_y = 4, 2
            elif last_segment[0] < x: #left
                sprite_x, sprite_y = 3, 3
            elif last_segment[1] < y: #up
                sprite_x, sprite_y = 3, 2
            elif last_segment[1] > y: #down
                sprite_x, sprite_y = 4, 3

        else:  # Body
            last_segment = snake_list[i - 1]  #previous segment
            next_segment = snake_list[i + 1]  #next segment
            if (last_segment[0] < x < next_segment[0]) or (next_segment[0] < x < last_segment[0]):  #horizontal
                sprite_x, sprite_y = 1, 0
            elif (last_segment[1] < y < next_segment[1]) or (next_segment[1] < y < last_segment[1]):  #vertical
                sprite_x, sprite_y = 2, 1
            elif (last_segment[0] < x and next_segment[1] > y) or (next_segment[0] < x and last_segment[1] > y):  #angle Left-Down
                sprite_x, sprite_y = 2, 0
            elif (last_segment[1] < y and next_segment[0] < x) or (next_segment[1] < y and last_segment[0] < x):  #angle Top-Left
                sprite_x, sprite_y = 2, 2
            elif (last_segment[0] > x and next_segment[1] < y) or (next_segment[0] > x and last_segment[1] < y):  #angle Right-Up
                sprite_x, sprite_y = 0, 1
            elif (last_segment[1] > y and next_segment[0] > x) or (next_segment[1] > y and last_segment[0] > x):  #angle Down-Right
                sprite_x, sprite_y = 0, 0

        #draw the segment
        screen.blit(
            pygame.transform.scale(
                snake_sprite.subsurface(
                    pygame.Rect(sprite_x * sprite_size, sprite_y * sprite_size, sprite_size, sprite_size)),
                (snake_block, snake_block),
            ),
            (snake_pos_x, snake_pos_y),
        )

def in_game():
    global snake_length
    screen = pygame.display.set_mode((width, height))
    game_over = False
    y_change = 0
    x_change = 0
    snake_pos = [204, 278]
    snake_list = [[204, 278],[170, 278], [136, 278]]
    snake_length = 3
    apple_pos = [476, 278]
    direction = "RIGHT"
    next_direction = "RIGHT"

    #initialize list to identify all tile positions as empty
    tiles = []
    for row in range(15):
        tiles_row = []
        for col in range(20):
            tiles_row.append(0)
        tiles.append(tiles_row)

    #keeps game at standstill until user presses the right arrow key, initiating game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #user can only initiate game by pressing right arrow key, moving towards the first apple
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    x_change = snake_block
                    y_change = 0
                    waiting = False

        #initial screen
        screen.fill(background)
        display_score(snake_length - 3)

        #draw the board
        for row in range(15):
            for col in range(20):
                if (row + col) % 2 == 0:
                    color = board_light
                else:
                    color = board_dark
                pygame.draw.rect(screen, color, (col * snake_block, 40 + row * snake_block, snake_block, snake_block))

        #draw the snake in starting position
        draw_snake(snake_block, snake_list)

        #draw the apple in starting position
        screen.blit(apple, apple.get_rect(topleft=(apple_pos[0], apple_pos[1])))

        pygame.display.flip()
        clock.tick(snake_speed)

    #interprets the key pressing making sure the user cannot make the snake turn back on itself
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    next_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    next_direction = "RIGHT"
                elif event.key == pygame.K_UP and direction != "DOWN":
                    next_direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    next_direction = "DOWN"

        direction = next_direction #commit to the new direction

        #update direction and movement
        if direction == "LEFT":
            x_change = -snake_block
            y_change = 0
        elif direction == "RIGHT":
            x_change = snake_block
            y_change = 0
        elif direction == "UP":
            x_change = 0
            y_change = -snake_block
        elif direction == "DOWN":
            x_change = 0
            y_change = snake_block

        #moves the snake according the key presses defined above
        snake_pos[0] += x_change
        snake_pos[1] += y_change

        #adjusts snake list for new position
        snake_head = [snake_pos[0], snake_pos[1]]
        snake_list.insert(0, snake_head)

        #increases the length of the snake and generates a new apple location when snake eats the apple
        if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
            valid = False
            while not valid:
                apple_pos = [random.choice(range(0, 647, snake_block)), random.choice(range(40, 517, snake_block))]
                tile_x = apple_pos[0] // snake_block
                tile_y = apple_pos[1] // snake_block - 1
                if tiles[tile_y][tile_x] == 0:
                    valid = True
            snake_length += 1
        else:
            # removes the tail if the snake did not eat an apple yet
            if len(snake_list) > snake_length:
                snake_list.pop()

        #reset tiles list
        for row in range(15):
            for col in range(20):
                tiles[row][col] = 0

        #update the position of the snake in the tiles list
        for segment in snake_list:
            x, y = segment
            tile_x = x//snake_block - 1
            tile_y = y//snake_block - 2
            tiles[tile_y][tile_x] = 1 #mark of snake body

        #reinitiates the screen
        screen.fill(background)
        display_score(snake_length - 3)

        #draws the checkered board
        for row in range(15):
            for col in range(20):
                if (row + col) % 2 == 0:
                    color = board_light
                else:
                    color = board_dark
                pygame.draw.rect(screen, color, (col * 34, 40 + row * 34, 34, 34))

        #displays the snake if it is within the board, otherwise the game ends (if the snake crashes into a wall)
        if width > snake_pos[0] >= 0 and height > snake_pos[1] >= 40:
            draw_snake(snake_block, snake_list)
        else:
            break

        #displays the apple on the screen
        screen.blit(apple, apple.get_rect(topleft=(apple_pos[0], apple_pos[1])))

        #ends game if snake collides with itself
        for x in snake_list[1:]:
            if x == snake_head:
                print("collision")
                game_over = True
                break

        pygame.display.flip()

        clock.tick(snake_speed)

    end_game() #add disintigration functionality, to watch snake die :(

#displays game over screen
def end_game():
    font = pygame.font.SysFont(None, 40)

    #set screen
    screen = pygame.display.set_mode((650, 470))
    screen.fill(board_light)
    screen.blit(pygame.image.load("Game_over.png"), (0, 0))

    #play again button
    pygame.draw.rect(screen, blue, [10, 410, 310, 50], 0, 5)
    play_surf = font.render("Play again!", True, white)
    screen.blit(play_surf, play_surf.get_rect(center=(165, 435)))

    #exit button
    pygame.draw.rect(screen, blue, [330, 410, 310, 50], 0, 5)
    exit_surf = font.render("Exit", True, white)
    screen.blit(exit_surf, exit_surf.get_rect(center=(485, 435)))

    #score count displayed
    font = pygame.font.SysFont(None, 60)
    score_surf = font.render(f"Your Score: {snake_length - 3}", True, white)
    screen.blit(score_surf, score_surf.get_rect(center=(325, 40)))

    #game over displayed
    font = pygame.font.SysFont(None, 80)
    screen.blit(font.render("Game Over!", True, white), (160, 75))
    pygame.display.flip()

    #interprets screen clicks allowing the user to restart the game, or exit the game depending on the button they click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                #restart button
                if 10 < x < 320 and 410 < y < 460:
                    in_game()

                #exit button
                if 330 < x < 640 and 410 < y < 460:
                    pygame.quit()
                    quit()

#inteprets the screen being clicked to start the game when the play button is clicked
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            #play button
            if 10 < x < 678 and 270 < y < 320:
                in_game()