class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setPixel(self, x, y, on):
        pass

    def getPixel(self, x, y):
        pass

    def clear(self):
        self.screen = [0] * self.width * self.height
