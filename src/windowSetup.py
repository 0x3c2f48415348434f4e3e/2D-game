import pygame
#to set up our window
import player
import sys

class window:
    COLOR = (255,255,255)
    def __init__(self) -> None:
        pygame.init()
        self.win = pygame.display.set_mode((1280,720))
         #set up window title
        pygame.display.set_caption("HashCon")
        clock = pygame.time.Clock()
        running = True
        #as we know, all games 2D face right
        isMovingLeft = False
        isMovingRight = False


        playerGameObject = player.Player(initialX=100,initialY=100,screen=self.win)
        while running:

            #FPS
            clock.tick(60)

            window.bg(self.win)

            #get our events
            playerGameObject.initiateBlit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #check for key press
                if event.type == pygame.KEYDOWN:
                    #check for specific key
                    if event.key == pygame.K_UP:
                        print("Up key pressed")
                        #lets try making our player jump
                    if event.key == pygame.K_RIGHT:
                        isMovingRight = True
                        print("Right ", isMovingRight)
                    if event.key == pygame.K_LEFT:
                        print("Left key pressed")
                        isMovingLeft = True
                    

                #For release key
                if event.type == pygame.KEYUP:
                    #check for specific key
                    if event.key == pygame.K_UP:
                        print("Up key Release")
                        #lets try making our player jump
                    if event.key == pygame.K_RIGHT:
                        isMovingRight = False
                        print("Right ", isMovingRight)
                    if event.key == pygame.K_LEFT:
                        print("Left key pressed")
                        isMovingLeft = False
                    #escape key to exit
                    if event.key == pygame.K_ESCAPE:
                        print("Escape key pressed")
                        running = False
            playerGameObject.move(isMovingRight,isMovingLeft)
                        
            #win.fill("black")

            #render our game

            #flip display
            pygame.display.update()

        pygame.quit
    @classmethod
    def bg(cls,win):
        win.fill(window.COLOR)

