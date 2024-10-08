import pygame
import time
import random

pygame.init()  # Initialize the pygame library

# Colors
white = (0, 0, 0)
yellow = (255, 255, 102)
black = (255,255,255)
red = (213, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
dis_width = 800  # Width of the game window
dis_height = 600  # Height of the game window
dis = pygame.display.set_mode((dis_width, dis_height))  # Create the game window
pygame.display.set_caption('Snake Game by Akhila')  # Set the title of the window

clock = pygame.time.Clock()  # Create a clock object to manage the game's frame rate
snake_block = 10  # Size of each segment of the snake
initial_snake_speed = 10  # Initial speed of the snake

font_style = pygame.font.SysFont(None, 50)  # Font style for displaying messages

def our_snake(snake_block, snake_List):
    # Draw the snake on the screen
    for x in snake_List:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    # Display a message on the screen
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False  # Game over flag
    game_close = False  # Game close flag

    x1 = dis_width / 2  # Initial x position of the snake
    y1 = dis_height / 2  # Initial y position of the snake

    x1_change = 0  # Change in x position
    y1_change = 0  # Change in y position

    snake_List = []  # List to store the positions of the snake segments
    Length_of_snake = 1  # Initial length of the snake

    # Generate random position for the food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:  # Main game loop

        while game_close == True:  # Loop for when the game is over
            dis.fill(black)  # Fill the screen with black
            message("You Lost! Press Q-Quit or C-Play Again", red)  # Display the game over message
            pygame.display.update()  # Update the display

            for event in pygame.event.get():  # Check for user events
                if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                    if event.key == pygame.K_q:  # Quit the game if 'Q' is pressed
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart the game if 'C' is pressed
                        gameLoop()

        for event in pygame.event.get():  # Check for user events
            if event.type == pygame.QUIT:  # Quit the game if the close button is clicked
                game_over = True
            if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_LEFT:  # Move left
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # Move right
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # Move up
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # Move down
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # Check if the snake hits the wall
            game_close = True
        x1 += x1_change  # Update the x position
        y1 += y1_change  # Update the y position
        dis.fill(black)  # Fill the screen with black
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])  # Draw the food
        snake_Head = []  # Create a new head for the snake
        snake_Head.append(x1)  # Add the x position to the head
        snake_Head.append(y1)  # Add the y position to the head
        snake_List.append(snake_Head)  # Add the head to the snake list
        if len(snake_List) > Length_of_snake:  # Remove the last segment if the snake is too long
            del snake_List[0]

        for x in snake_List[:-1]:  # Check if the snake collides with itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # Draw the snake

        pygame.display.update()  # Update the display

        if x1 == foodx and y1 == foody:  # Check if the snake eats the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # Generate new food position
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # Increase the length of the snake

        snake_speed = initial_snake_speed + Length_of_snake // 5  # Increase speed as the snake length increases
        clock.tick(snake_speed)  # Control the frame rate
    print(f"your score is: {Length_of_snake}")  # Print the score
    pygame.quit()  # Quit the game
    quit()  # Exit the program

gameLoop()  # Start the game