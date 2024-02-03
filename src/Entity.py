import pygame
class Entity(pygame.sprite.Sprite):
    def __init__(self,path:str, initialX, initialY,screen) -> None:
        self.speed = 5
        super().__init__()
        #global Screen 
        self.Screen = screen
        #set initial positions
        x = initialX
        y = initialY

        #path is the location of the thingy
        #global img
        #global rect
        self.img = pygame.image.load(path)
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)

    def blitImg(self,playerFlip,playerXDirection):
        self.Screen.blit(pygame.transform.flip(self.img,playerFlip,False),self.rect)
    def moveLeft(self):
        dx = 0
        dy = 0
        dx = (-self.speed)
        self.rect.x += dx
        self.rect.y += dy

    def moveRight(self):
        dx = 0
        dy = 0
        dx = (self.speed)
        self.rect.x += dx
        self.rect.y += dy

    
        