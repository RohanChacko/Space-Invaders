from alien import Inv
from engine import engine

class Missile(object):
    """Base class missile"""

    def __init__(self):
        self.collision=0;

    # def check():


class Bigmis(Missile, Inv):
    """Initialises class for the Big Missile"""

    bmisorder = []

    def __init__(self):
        self.collision=0
        super().__init__

    def start(self, xpos, ypos):
        """Initial position of the Big missile"""
        Bigmis.bmisorder.append([ypos - 100, xpos, 1])
        engine.DISP_SCREEN.blit(engine.B_MISSILE, (xpos, ypos - 100))

    def update(self):
        for i in range(len(Bigmis.bmisorder)):
            if Bigmis.bmisorder[i][2] == 1:

                    # print(int(Bigmis.bmisorder[i][0]/100),int(Bigmis.bmisorder[i][1]/100))
                if Bigmis.bmisorder[i][0] - 100 == 0:
                    if Inv.pos[int(Bigmis.bmisorder[i][0] /
                                   100) -
                               1][int(Bigmis.bmisorder[i][1] /
                                      100)] == 1 or Inv.pos[int(Bigmis.bmisorder[i][0] /
                                                                100) -
                                                            1][int(Bigmis.bmisorder[i][1] /
                                                                   100)] == 2:
                        Inv.pos[int(Bigmis.bmisorder[i][0] / 100) -
                                1][int(Bigmis.bmisorder[i][1] / 100)] = 0
                        Inv.fullcnt -= 1
                        Bigmis.bmisorder[i][2] = 0
                        self.collision=1
                    else:
                    	self.collision=0
                    	Bigmis.bmisorder[i][0] -= 100

                elif Bigmis.bmisorder[i][0] - 100 == 100:

                    # print(int(Bigmis.bmisorder[i][0]/100),int(Bigmis.bmisorder[i][1]/100))
                    if Inv.pos[int(Bigmis.bmisorder[i][0] /
                                   100) -
                               1][int(Bigmis.bmisorder[i][1] /
                                      100)] == 1 or Inv.pos[int(Bigmis.bmisorder[i][0] /
                                                                100) -
                                                            1][int(Bigmis.bmisorder[i][1] /
                                                                   100)] == 2:
                        Inv.pos[int(Bigmis.bmisorder[i][0] / 100) -
                                1][int(Bigmis.bmisorder[i][1] / 100)] = 0
                        Inv.fullcnt -= 1
                        Bigmis.bmisorder[i][2] = 0
                        self.collision=1

                    else:
                    	self.collision=0
                    	Bigmis.bmisorder[i][0] -= 100

                else:
                    if Bigmis.bmisorder[i][0] - 100 > 0:
                        Bigmis.bmisorder[i][0] -= 100

                    else:
                        # print(Bigmis.bmisorder[i][1],Bigmis.bmisorder[i][0])
                        Bigmis.bmisorder[i][2] = 0

                if Bigmis.bmisorder[i][2] == 1:
                    engine.DISP_SCREEN.blit(
                        engine.B_MISSILE, (Bigmis.bmisorder[i][1], Bigmis.bmisorder[i][0]))


class Smallmis(Missile, Inv):
    """Defines class for small missile"""
    smisorder = []

    def __init__(self):
        pass

    def start(self, xpos, ypos):
        """Initialises start position for small missile"""
        Smallmis.smisorder.append([ypos - 100, xpos, 1])
        engine.DISP_SCREEN.blit(engine.S_MISSILE, (xpos, ypos - 100))

    def update(self):

        # print("haan")
        for i in range(len(Smallmis.smisorder)):
            if Smallmis.smisorder[i][2] == 1:

                # print(int(Smallmis.smisorder[i][0]/100),int(Smallmis.smisorder[i][1]/100))
                if Smallmis.smisorder[i][0] - 100 == 0:
                    if Inv.pos[int(Smallmis.smisorder[i][0] / 100) -
                               1][int(Smallmis.smisorder[i][1] / 100)] == 1:
                        Inv.pos[int(Smallmis.smisorder[i][0] / 100) -
                                1][int(Smallmis.smisorder[i][1] / 100)] = 2
                        Inv.fullcnt -= 1
                        Smallmis.smisorder[i][2] = 0
                    else:
                        Smallmis.smisorder[i][0] -= 100

                elif Smallmis.smisorder[i][0] - 100 == 100:

                    # print(int(Bigmis.bmisorder[i][0]/100),int(Bigmis.bmisorder[i][1]/100))
                    if Inv.pos[int(Smallmis.smisorder[i][0] / 100) -
                               1][int(Smallmis.smisorder[i][1] / 100)] == 1:
                        Inv.pos[int(Smallmis.smisorder[i][0] / 100) -
                                1][int(Smallmis.smisorder[i][1] / 100)] = 2
                        Inv.fullcnt -= 1
                        Smallmis.smisorder[i][2] = 0
                    else:
                        Smallmis.smisorder[i][0] -= 100

                else:
                    if Smallmis.smisorder[i][0] - 100 > 0:
                        Smallmis.smisorder[i][0] -= 100
                    else:
                        # print(Bigmis.bmisorder[i][1],Bigmis.bmisorder[i][0])
                        Smallmis.smisorder[i][2] = 0

                if Smallmis.smisorder[i][2] == 1:
                    engine.DISP_SCREEN.blit(
                        engine.S_MISSILE, (Smallmis.smisorder[i][1], Smallmis.smisorder[i][0]))
