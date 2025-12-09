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
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "brainrot!!", button_function3), Button(500,300,200,80, (0,200,200), (200,255,0), "No brainrot.", button_function5))

def button_function2():
    #function stuffs
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "look at sky", button_function6), Button(500,300,200,80, (0,200,200), (200,255,0), "look at sea", button_function7))


def button_function3():
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "2025 brainrot", button_function4), Button(500,300,200,80, (0,200,200), (200,255,0), "2020 brainrot", button_function8))

def button_function4():
    end_screen(drawing1)

def button_function5():
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "watch some movies", button_function9), Button(500,300,200,80, (0,200,200), (200,255,0), "play some games", button_function10))

def button_function6():
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "be an early bird", button_function11), Button(500,300,200,80, (0,200,200), (200,255,0), "be a night owl", button_function12))

def button_function7():
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "explore shallow waters", button_function13), Button(500,300,200,80, (0,200,200), (200,255,0), "explore deep waters", button_function14))

def button_function8():
    end_screen(drawing2)

def button_function9():
    end_screen(drawing3)

def button_function10():
    end_screen(drawing4)

def button_function11():
    end_screen(drawing5)

def button_function12():
    end_screen(drawing6)

def button_function13():
    end_screen(drawing7)

def button_function14():
    end_screen(drawing8)



def drawing1():
    screen = turtle.Screen()
    screen.bgcolor('teal')
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor('yellow')
    pen.hideturtle()

    pen.penup()
    pen.goto(-200,300)
    pen.pendown()

#outside of 6
    pen.left(180)
    pen.forward(250)
    pen.left(90)
    pen.forward(400)
    pen.left(90)
    pen.forward(250)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(175)
    pen.left(90)
    pen.forward(-125)
    pen.left(90)
    pen.forward(175)
    pen.left(90)
    pen.forward(75)

#inside of 6
    pen.penup()
    pen.goto(-275,50)
    pen.pendown()

    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(100)

#7
    pen.penup()
    pen.goto(200,300)
    pen.pendown()

    pen.left(90)
    pen.forward(250)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(175)
    pen.goto(-50,-100)
    pen.left(180)
    pen.forward(-75)
    pen.goto(200,225)
    pen.left(90)
    pen.forward(-75)

    turtle.done()

def drawing2():
    screen = turtle.Screen()
    screen.bgcolor('yellow')
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor('red')
    pen.hideturtle()

    pen.penup()
    pen.goto(50,100)
    pen.pendown()
#amogus visor
    pen.forward(150)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(75)

    pen.penup()
    pen.goto(125,175)
    pen.pendown()
#amogus crewmate
    pen.left(180)
    pen.forward(75)
    pen.left(90)
    pen.forward(175)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(-25)
    pen.left(90)
    pen.forward(75)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(150)
#amogus backpack
    pen.penup()
    pen.goto(-50,137)
    pen.pendown()

    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)

    turtle.done()

def drawing3():
    screen = turtle.Screen()
    screen.bgcolor('black')
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor('white')
    pen.hideturtle()
#film slate
    pen.penup()
    pen.goto(150,-100)
    pen.pendown()

    pen.forward(-300)
    pen.left(90)
    pen.forward(200)
    pen.goto(-175,150)
    pen.goto(100,275)
    pen.goto(130,225)
    pen.goto(-150,100)
    pen.goto(150,100) 
    pen.goto(150,-100)
#lines on slate
    pen.penup()
    pen.goto(100,0)    
    pen.pendown()

    pen.left(90)
    pen.forward(200)

    pen.penup()
    pen.goto(100,50)    
    pen.pendown()

    pen.forward(200)

    pen.penup()
    pen.goto(100,-50)    
    pen.pendown()

    pen.forward(200)

    pen.penup()
    pen.goto(0,-50)    
    pen.pendown()

    pen.left(90)
    pen.forward(25)

    pen.penup()
    pen.goto(60,-50)    
    pen.pendown()

    pen.forward(25)

    pen.penup()
    pen.goto(-60,-50)    
    pen.pendown()

    pen.forward(25)




    turtle.done()

def drawing4():
    screen = turtle.Screen()
    screen.bgcolor('maroon')
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor('white')
    pen.hideturtle()
#controller
    pen.penup()
    pen.goto(-300,-150)
    pen.pendown()

    pen.forward(600)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(600)
    pen.left(90)
    pen.forward(300)
#buttons
    pen.penup()
    pen.goto(75,-100)
    pen.pendown()

    pen.left(270)
    pen.forward(150)
    pen.left(90)
    pen.forward(-50)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(-50)

    pen.penup()
    pen.goto(50,-85)
    pen.pendown()

    pen.left(90)
    pen.forward(40)
    pen.left(270)
    pen.forward(10)
    pen.left(90)
    pen.forward(-40)
    pen.left(90)
    pen.forward(10)

    pen.penup()
    pen.goto(-10,-85)
    pen.pendown()

    pen.left(90)
    pen.forward(-40)
    pen.left(270)
    pen.forward(-10)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
    pen.forward(-10)
    pen.penup()
#circle buttons
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(5)
    turtle.color('white')
    turtle.setposition(140,-100)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()

    turtle.setposition(230,-100)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()
#directional buttons
    pen.penup()
    pen.goto(-175,-100)
    pen.pendown()

    pen.left(90)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(90)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(90)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(90)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(270)
    pen.forward(30)
    pen.left(90)
    pen.forward(30)
    pen.penup()
#line
    pen.goto(-300,75)
    pen.pendown()
    pen.left(90)
    pen.forward(600)

    turtle.done()

def drawing5(): 
    screen = turtle.Screen()
    screen.bgcolor('sky blue')   
#sun  
    pen = turtle.Turtle()
    pen.speed(5)
    pen.pencolor('yellow')
    pen.hideturtle()
    pen.width(3)
    pen.penup()
    pen.goto(100,200)
    pen.pendown()
    pen.goto(200,275)
    pen.penup()

    
    pen.goto(0,275)
    pen.pendown()
    pen.goto(25,380)
    pen.penup()

    pen.goto(-225,150)
    pen.pendown()
    pen.goto(-350,200)
    pen.penup()

    pen.goto(-130,-75)
    pen.pendown()
    pen.goto(-175,-175)
    pen.penup()

    pen.goto(100,-0)
    pen.pendown()
    pen.goto(175,-100)
    pen.penup()

    turtle.hideturtle()
    turtle.width(4)
    turtle.penup()
    turtle.speed(5)
    turtle.color('yellow')
    turtle.setposition(-50,-50)
    turtle.pendown()
    turtle.circle(150)
    turtle.penup()

    turtle.done()

def drawing6(): 
    screen = turtle.Screen()
    screen.bgcolor('dark blue')   
#moon  
    turtle.hideturtle()
    turtle.width(4)
    turtle.penup()
    turtle.speed(5)
    turtle.color('white')
    turtle.setposition(0,-200)
    turtle.pendown()
    turtle.circle(300)
    turtle.penup()

    turtle.setposition(75,100)
    turtle.pendown()
    turtle.circle(75)
    turtle.penup()

    turtle.setposition(-75,-25)
    turtle.pendown()
    turtle.circle(30)
    turtle.penup()

    turtle.setposition(75,-150)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()

    turtle.setposition(-150,175)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()

    turtle.done()

def drawing7():
    screen = turtle.Screen()
    screen.bgcolor('light blue')
    pen = turtle.Turtle()
    pen.shape('turtle')
    pen.width(3)
    pen.speed(5)
    pen.pencolor('green')
#Turtle
    pen.penup()
    pen.goto(-400,0)
    pen.pendown()

    pen.forward(600)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(600)
    pen.left(90)
    pen.forward(300)
    pen.penup()

    pen.goto(-375,0)
    pen.pendown()
    pen.forward(150)
    pen.left(90)
    pen.forward(125)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.left(270)
    pen.forward(125)
    pen.penup()

    pen.goto(75,0)
    pen.pendown()
    pen.left(180)
    pen.forward(150)
    pen.left(90)
    pen.forward(125)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.left(270)
    pen.forward(125)
    pen.left(270)
    pen.forward(100)
    pen.left(270)
    pen.forward(75)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(150)
    pen.left(90)
    pen.forward(225)
#shell details
    pen.penup()
    pen.goto(-350,200)
    pen.pendown()

    pen.left(180)
    pen.forward(475)

    pen.penup()
    pen.goto(-200,300)
    pen.pendown()

    pen.left(270)
    pen.forward(150)

    pen.penup()
    pen.goto(25,300)
    pen.pendown()

    pen.forward(150)

    turtle.done()

def drawing8():
    screen = turtle.Screen()
    screen.bgcolor('dark blue')
    turtle.hideturtle()
    turtle.width(4)
    turtle.penup()
    turtle.speed(5)
    turtle.color('pink')
    turtle.setposition(100,200)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(200,180)
    turtle.penup()

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.width(4)
    pen.speed(5)
    pen.pencolor('pink')
    pen.penup()
    pen.goto(100,200)
    pen.pendown()
    pen.left(180)
    pen.forward(400)

#stingers


    turtle.done()

def main():
        
    create_screen(Button(100,300,200,80, (255,0,200), (175,0,255), "go online", button_function1), Button(500,300,200,80, (0,200,200), (200,255,0), "touch grass", button_function2))

if __name__ == "__main__":
    main()
