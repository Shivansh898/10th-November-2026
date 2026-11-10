import pygame
pygame.init()
WIDTH = 400
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class rectangle():
    def __init__(self,width,height, color,x,y,border):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.border = border
    def draw_rectangle(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),self.border)
rect1 = rectangle(50,350,"white",175,450,2)
rect2 = rectangle(200,450,"white",100,0,2)
rect3 = rectangle(120,120,"red",140,20,0)
rect4 = rectangle(120,120,"orange",140,160,0)
rect5 = rectangle(120,120,"green",140,300,0)
rect1.draw_rectangle()
rect2.draw_rectangle()
rect3.draw_rectangle()
rect4.draw_rectangle()
rect5.draw_rectangle()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
