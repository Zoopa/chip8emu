class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        self.screen = [0] * self.width * self.height

    def setPixel(self, x, y, isOn):
        self.screen[x + y * self.width] = isOn

    def getPixel(self, x, y):
        return self.screen[x + y * self.width]


