import pygame


class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = 'Green'
        


def main():
    pygame.init()
    pygame.display.set_caption("Art Quiz")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    particle = Particle()
    print(particle.pos)
    print(particle.size)
    print(particle.color)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('lavender')
        pygame.display.flip()
    pygame.quit()
    

if __name__ == "__main__":
    main()
