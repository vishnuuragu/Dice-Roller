import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Initialize the mixer module for Sound effects
pygame.mixer.init()

# Load the sound effect
dice_sound = pygame.mixer.Sound("E:\Programs\Python\Dice Roller\dice_roll.mp3")

# Set the dimensions of the window
ws = 400
window = pygame.display.set_mode((ws, ws))


# Define colors
WHITE = (255, 255, 255)
# Define colors
BLACK = (0, 0, 0)

# Define dice positions
dice_positions = {
    1: [(ws//4, ws//4)],
    2: [(ws//8, ws//8), (ws*3//8, ws*3//8)],
    3: [(ws//8, ws//8), (ws//4, ws//4), (ws*3//8, ws*3//8)],
    4: [(ws//8, ws//8), (ws*3//8, ws//8), (ws//8, ws*3//8), (ws*3//8, ws*3//8)],
    5: [(ws//8, ws//8), (ws*3//8, ws//8), (ws//4, ws//4), (ws//8, ws*3//8), (ws*3//8, ws*3//8)],
    6: [(ws//8, ws//8), (ws*3//8, ws//8), (ws//8, ws//4), (ws*3//8, ws//4), (ws//8, ws*3//8), (ws*3//8, ws*3//8)]
}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Play the sound effect
            dice_sound.play()

            # Roll the dice when the mouse is clicked
            for _ in range(10):
                window.fill(WHITE)
                roll1 = random.randint(1, 6)
                roll2 = random.randint(1, 6)
                for pos in dice_positions[roll1]:
                    pygame.draw.circle(window, BLACK, (pos[0], pos[1]), 20)
                for pos in dice_positions[roll2]:
                    pygame.draw.circle(window, BLACK, (ws//2 + pos[0], pos[1]), 20)
                pygame.display.flip()
                time.sleep(0.1)

pygame.quit()