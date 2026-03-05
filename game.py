import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Define basket class
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# Define ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(-100, -20)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# Function to display score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
def game():
    clock = pygame.time.Clock()
    basket = Basket()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(basket)
    balls = pygame.sprite.Group()
    score = 0

    running = True
    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Create new ball occasionally
        if random.random() < 0.02:
            ball = Ball()
            all_sprites.add(ball)
            balls.add(ball)

        # Update sprites
        all_sprites.update()

        # Check for collisions
        collided_balls = pygame.sprite.spritecollide(basket, balls, True)
        for ball in collided_balls:
            score += 1

        # Draw everything
        all_sprites.draw(screen)
        show_score(score)

        # Update screen
        pygame.display.flip()

        # Set frame rate
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game()
