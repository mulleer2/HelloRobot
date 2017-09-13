from gopigo in *

import time

class Piggy(object):

    def __init__(self):

        print("Hello, im your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right.rot()
        time.sleep(.5)
        stop()

hotrod = Piggy()
