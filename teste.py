import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Horizontal Drag Volume Bar")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_COLOR = (0, 200, 0)
BAR_BG_COLOR = (200, 0, 0)

# Bar settings
BAR_X = 50
BAR_Y = 80
BAR_WIDTH = 300
BAR_HEIGHT = 30
bar_value = 50  # percentage (0–100)

# Drag state
dragging = False

def draw_horizontal_bar(surface, x, y, width, height, value):
    """Draws a horizontal bar with given percentage value."""
    # Draw background (empty part)
    pygame.draw.rect(surface, BAR_BG_COLOR, (x, y, width, height))
    
    # Calculate filled width
    filled_width = int(width * (value / 100))
    
    # Draw filled part from left to right
    pygame.draw.rect(surface, BAR_COLOR, (x, y, filled_width, height))

def set_bar_value_from_mouse(mouse_pos):
    global bar_value
    mx, my = mouse_pos
    # Clamp mouse X within bar range
    if mx < BAR_X:
        mx = BAR_X
    elif mx > BAR_X + BAR_WIDTH:
        mx = BAR_X + BAR_WIDTH
    # Calculate percentage from left
    bar_value = int(((mx - BAR_X) / BAR_WIDTH) * 100)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                # Check if click is inside bar
                if BAR_X <= event.pos[0] <= BAR_X + BAR_WIDTH and BAR_Y <= event.pos[1] <= BAR_Y + BAR_HEIGHT:
                    dragging = True
                    set_bar_value_from_mouse(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                set_bar_value_from_mouse(event.pos)

    # Draw the bar
    draw_horizontal_bar(screen, BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT, bar_value)

    # Draw text showing percentage
    font = pygame.font.SysFont(None, 24)
    text = font.render(f"{bar_value}%", True, BLACK)
    screen.blit(text, (BAR_X + BAR_WIDTH + 10, BAR_Y + BAR_HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
