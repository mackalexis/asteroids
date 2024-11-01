from circleshape import *
from constants import *
import random

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        print(f"Asteroid created at position ({x}, {y}) with radius {radius}")

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        #Original asteroid is destroyed - maybe spawn new ones next
        self.kill()

        #If it was a small asteroid, just return at this point - don't spawn any more
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #If we're here, we need to spawn 2 new asteroids moving in random directions

        random_angle = random.uniform(20, 50)
        vec_1 = self.velocity.rotate(random_angle)
        vec_2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid_1.velocity = vec_1 * 1.2
        asteroid_2.velocity = vec_2 * 1.2

        return asteroid_1, asteroid_2