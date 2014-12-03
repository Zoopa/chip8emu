class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        self.screen = [0] * self.width * self.height
