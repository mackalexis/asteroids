from circleshape import *
from constants import *

class Shot(CircleShape):
    #containers = (updatable, drawable)
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 0, 0)  # Bright red
        self.velocity = pygame.math.Vector2(0, 0)  # Initialize velocity
        print(f"Shot created at position: {self.position}")

    def update(self, dt):
        print(f"Shot position: {self.position}, velocity: {self.velocity}")
        # Move based on velocity
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 0)