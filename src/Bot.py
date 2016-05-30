import sys
import random
import time

from tanxees.client.AIBase import AIBase
from tanxees.client.ClientStateControllerBase import ClientStateControllerBase

from tanxees.api import PlayerKeysModel

class DumbAI(ClientStateControllerBase):
    PAUSE_TIME = 1.0
    
    @staticmethod
    def decideBool():
        return random.choice((True, False))

    def __init__(self, clientState=None):
        ClientStateControllerBase.__init__(self, clientState)
        self.__clock = 0
    
    def updateClientState(self, theState):
        currentClock = time.time()
        if currentClock - self.__clock >= self.PAUSE_TIME:
            self.__clock = currentClock
            keys = PlayerKeysModel(self.decideBool(), self.decideBool(),
                                   self.decideBool(), self.decideBool(),
                                   self.decideBool())
            self.clientState.keys = keys
            return True

        return False

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: %s bot-name' % sys.argv[0])
    AIBase(sys.argv[1], DumbAI()).run()

if __name__ == '__main__':
    main()
