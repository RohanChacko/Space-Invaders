from engine import engine

class Ships(object):
    """Defines the spaceship class and gives position
        attribute which helps in movement of the spaceship"""

    def __init__(self):
        self.posx = 300
        self.posy = 500
        

    def move(self, key):
        """Helps move the ship"""
        if key == 'A':
            if self.posx - 100 < 0:
                pass
            else:
                self.posx -= 100
        engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))
        engine.DISP_SCREEN.blit(engine.SP_SHIP, (self.posx, self.posy))

        if key == 'D':
            if self.posx + 100 > 700:
                pass
            else:
                self.posx += 100
            engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))
            engine.DISP_SCREEN.blit(engine.SP_SHIP, (self.posx, self.posy))

    def update(self):
        """Updates ship position"""
        engine.DISP_SCREEN.blit(engine.SP_SHIP, (self.posx, self.posy))

    def position(self):
        """Returns ship position"""
        return self.posx, self.posy