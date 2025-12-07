import pygame
import random


class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = 'Green'
        
class Button():
    def __init__(self, x, y, width, height, color, color2, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = color
        self.hover_color = color2
        self.current_color = color
        self.font = pygame.font.Font(None, 30)
    
    def draw(self, screen):
        pygame.draw.rect(screen,self.current_color,self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.current_color = self.hover_color
            else:
                self.current_color = self.color
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

def button_function():
    #function stuffs

    return 0

def main():
    pygame.init()
    pygame.display.set_caption("Art Quiz")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    # creates button
    button1 = Button(100,300,200,80, (255,0,200), (175,0,255), "go online", button_function)
    button2 = Button(500,300,200,80, (0,200,200), (200,255,0), "touch grass", button_function)
    
    particle = Particle()
    print(particle.pos)
    print(particle.size)
    print(particle.color)

    font = pygame.font.SysFont("Arial", 48) 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # button events
            button1.handle_event(event)
            button2.handle_event(event)

        screen.fill('lavender')

        # draw button
        button1.draw(screen)
        button2.draw(screen)

        # would you rather
        text_surface = font.render("Would You Rather", True, (0,0,0))

        screen.blit(text_surface, (250, 100))

        text_surface = font.render("or", True, (0,0,0))

        screen.blit(text_surface, (380, 310))

        pygame.display.flip()
    pygame.quit()
    

if __name__ == "__main__":
    main()
