class CPU(object):

    def __init__(self, memory):
        self.memory = memory

    def fetchOpcode(self, address):
        firstHalf = self.memory.getByte(address) << 8
        secondHalf = self.memory.getByte(address + 1)
        return firstHalf | secondHalf

    def decodeOpcode(self, encodedOpcode):
        pass

    def executeOpcode(self, decodedOpcode, decodedValue):
        pass
