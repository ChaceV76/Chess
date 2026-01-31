'''This file will be used to generate the board and pieces visually'''
import pygame

# Sets up pygaame "Turning on Engine"
pygame.init()
screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
running = True


# Create the test surface
test_surface = pygame.Surface((640, 640))
test_surface.fill('lightsalmon4')

# Create black "squares"
square = pygame.Rect((80, 80), (80, 80))


pygame.draw.rect(test_surface, 'navajowhite', square)

'''
# Make a loop that skips over to the right by 80 width and fills a 80x80 navajo white rectangle after each 4th iteration move down a line
for index, square in enumerate(range(64), start=1):
    if index % 2 == 0: # Draw the square then start at the next row, x-axis should be the same 0, but y moves down + 80
        square.move(80, 0)
    else:
        pass
'''


while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    # RENDER GAME HERE USING BLIT
    screen.blit(test_surface, (320, 0))

    # flip() the display to put work on screen
    pygame.display.flip()

    clock.tick(60) # Limits FPS to 60

pygame.quit()
