import pygame
import sys
import turtle

class Particle():

    def __init__(self, pos=(0, 0), size=15):
        self.pos = pos
        self.size = size
        self.color = 'Green'
        
class Button():
    def __init__(self, x, y, width, height, color, color2, text, action):
        pygame.font.init()
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
            

def create_screen(button1, button2):
    pygame.init()
    pygame.display.set_caption("Art Quiz")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    # creates button
    buttonA = button1
    buttonB = button2
    
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
            buttonA.handle_event(event)
            buttonB.handle_event(event)

        screen.fill('lavender')

        # draw button
        buttonA.draw(screen)
        buttonB.draw(screen)

        # would you rather
        text_surface = font.render("Would You Rather", True, (0,0,0))

        screen.blit(text_surface, (250, 100))

        text_surface = font.render("or", True, (0,0,0))

        screen.blit(text_surface, (380, 310))

        pygame.display.flip()
    pygame.quit()

def end_screen(drawing):
    
    pygame.quit()

    drawing()

    sys.exit()

def button_function1():
    #function stuffs
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "67", button_function3), Button(500,300,200,80, (0,200,200), (200,255,0), "69", button_function2))

def button_function2():
    #function stuffs
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "420", button_function1), Button(500,300,200,80, (0,200,200), (200,255,0), "430", button_function2))


def button_function3():
    end_screen(drawing1)

def drawing1():
    

    turtle.exitonclick()

def main():
        
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "go online", button_function1), Button(500,300,200,80, (0,200,200), (200,255,0), "touch grass", button_function2))

if __name__ == "__main__":
    main()
