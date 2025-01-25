import pygame
import random

# Initialisation de pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Charger les images
apple_image = pygame.image.load("apple.png")
apple_image = pygame.transform.scale(apple_image, (CELL_SIZE, CELL_SIZE))


font = pygame.font.SysFont(None, 35)

# Position initiale du serpent et de la première pomme
snake = [(100, 100), (90, 100), (80, 100)]
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Direction initiale du serpent
direction = "RIGHT"

# On initialise le score
score = 0

def draw_snake(surface, snake):
    for segment in snake:
        pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(surface, food):
    surface.blit(apple_image, food)


def draw_score(surface, score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    surface.blit(score_text, (10, 10))

def main():
    global direction, food, score
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gestion des touches
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

        # Déplacement du serpent
        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= CELL_SIZE
        if direction == "DOWN":
            head_y += CELL_SIZE
        if direction == "LEFT":
            head_x -= CELL_SIZE
        if direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)
        snake.insert(0, new_head)

        # Vérifier si le serpent mange la nourriture
        if snake[0] == food:
            score += 1
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        else:
            snake.pop()

        # Vérifier les collisions avec les murs
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            running = False

        # Vérifier les collisions avec le corps du serpent
        if snake[0] in snake[1:]:
            running = False

        # Dessiner le serpent, la nourriture et  afficher le score
        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_score(screen, score)


        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    print(f"Jeu terminé, Vous avez {score} points")

# Lancer le jeu
if __name__ == "__main__":
    main()
