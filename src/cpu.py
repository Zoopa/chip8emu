class CPU(object):

    def __init__(self, memory):
        self.memory = memory

    def fetchOpcode(self):
        return self.memory.fetch(1234)
