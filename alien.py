from engine import engine
import random

class Inv(object):
    """Defines the invader class and spawns new aliens"""
    fullcnt = 0
    pos = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    order = []

    def __init__(self):
        Inv.xpos = random.randint(0, 7)
        Inv.ypos = random.randint(0, 1)
        Inv.pos[Inv.ypos][Inv.xpos] = 1
        Inv.order.append([Inv.xpos, Inv.ypos])
        Inv.fullcnt += 1
        engine.DISP_SCREEN.blit(engine.INVADER, (Inv.xpos * 100, Inv.ypos * 100))

    def create(self):
        """Spawns new alien"""
        Inv.xpos = random.randint(0, 7)
        Inv.ypos = random.randint(0, 1)

        if Inv.fullcnt == 16:
            return
        else:
            while Inv.pos[Inv.ypos][Inv.xpos] == 1 or Inv.pos[Inv.ypos][Inv.xpos] == 2:
                Inv.xpos = random.randint(0, 7)
                Inv.ypos = random.randint(0, 1)

        Inv.pos[Inv.ypos][Inv.xpos] = 1
        Inv.order.append([Inv.xpos, Inv.ypos])
        Inv.fullcnt += 1

        # print(xpos*100,ypos*100)
        engine.DISP_SCREEN.blit(engine.INVADER, (Inv.xpos * 100, Inv.ypos * 100))

    def dreate(self):
        """Deletes alien"""
        if Inv.order == []:
            return
        else:
            temp_pos = Inv.order.pop(0)
            Inv.fullcnt -= 1
            if Inv.pos[temp_pos[1]][temp_pos[0]] == 2:
                pass
            else:
                Inv.pos[temp_pos[1]][temp_pos[0]] = 0

    def update(self):
        """Updates alien position"""
        for i in range(2):
            for j in range(8):
                if Inv.pos[i][j] == 1:
                    engine.DISP_SCREEN.blit(engine.INVADER, (j * 100, i * 100))
                elif Inv.pos[i][j] == 2:
                    engine.DISP_SCREEN.blit(engine.DEAD_INVADER, (j * 100, i * 100))