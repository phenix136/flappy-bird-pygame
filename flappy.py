import pygame
import random

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Paramètres de l'oiseau
bird_width = 40
bird_height = 30
bird_x = 50
bird_y = screen_height // 2
bird_y_change = 0

# Paramètres des tuyaux
pipe_width = 70
pipe_gap = 200
pipe_velocity = 4

# Fonction pour générer les tuyaux
def create_pipe():
    pipe_height = random.randint(150, 450)
    bottom_pipe = pygame.Rect(screen_width, pipe_height, pipe_width, screen_height - pipe_height)
    top_pipe = pygame.Rect(screen_width, 0, pipe_width, pipe_height - pipe_gap)
    return bottom_pipe, top_pipe

# Générer des tuyaux
bottom_pipe, top_pipe = create_pipe()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 3

    # Déplacement de l'oiseau
    bird_y += bird_y_change

    # Déplacement des tuyaux
    bottom_pipe.x -= pipe_velocity
    top_pipe.x -= pipe_velocity

    # Réinitialiser les tuyaux quand ils sortent de l'écran
    if bottom_pipe.right < 0:
        bottom_pipe, top_pipe = create_pipe()
        score += 1

    # Détection des collisions
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)
    if bird_rect.colliderect(bottom_pipe) or bird_rect.colliderect(top_pipe) or bird_y <= 0 or bird_y >= screen_height:
        running = False  # Fin du jeu en cas de collision

    # Mise à jour de l'écran
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, bottom_pipe)
    pygame.draw.rect(screen, GREEN, top_pipe)
    pygame.draw.ellipse(screen, BLACK, bird_rect)

    # Affichage du score
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
