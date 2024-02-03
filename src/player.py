import Entity
class Player(Entity.Entity):
    characters =  [
        "../Assets/player.png"
    ]
    def __init__(self, initialX, initialY, screen):
        path = Player.characters[0]
        x = initialX
        y = initialY
        window = screen
        super().__init__(path,x,y,window)

    def initiateBlit(self,playerFlip,playerXDirection):
        self.blitImg(playerFlip,playerXDirection)
    def move(self,movingRight,movingLeft):
        #note we are passing isFacingRight to this movingPosition

        #note we are passing KeyBeingPressed to this isPressed
        if movingRight:
            self.moveRight()
        if movingLeft:
            self.moveLeft()
