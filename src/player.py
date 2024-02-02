import Entity
class Player(Entity.Entity):
    path="../Assets/player.png"
    def __init__(self, initialX, initialY, screen):
        path = Player.path
        x = initialX
        y = initialY
        window = screen
        super().__init__(path,x,y,window)

    def initiateBlit(self):
        self.blitImg()
    def move(self,movingRight,movingLeft):
        #note we are passing isFacingRight to this movingPosition

        #note we are passing KeyBeingPressed to this isPressed
        if movingRight:
            self.moveRight()
        if movingLeft:
            self.moveLeft()
