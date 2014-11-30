class Memory(object):

    def __init__(self, size):
        self.memory = [None] * size

    def setByte(self, position, newByte):
        if position < 0:
            raise IndexError

        self.memory[position] = newByte

    def getByte(self, position):
        if position < 0:
            raise IndexError

        return self.memory[position]
