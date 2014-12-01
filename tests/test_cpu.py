import unittest
from cpu import CPU
from memory import Memory


class CpuTest(unittest.TestCase):
    MEM_SIZE = 4096
    MEM_ADDRESS = 0x10
    OPCODE = 0xA2F0

    def setUp(self):
        self.memory = Memory(self.MEM_SIZE)
        self.memory.setByte(self.MEM_ADDRESS, (self.OPCODE >> 8) & 0xFF)
        self.memory.setByte(self.MEM_ADDRESS + 1, self.OPCODE & 0xFF)
        self.cpu = CPU(self.memory)

    def tearDown(self):
        pass

    def testCpuHasMemory(self):
        self.assertIsInstance(self.cpu.memory, Memory)

    def testFetchOpcodeReadsCorrectOpcode(self):
        opcode = self.cpu.fetchOpcode(self.MEM_ADDRESS)
        self.assertEqual(opcode, self.OPCODE)

    def testDecodeOpcodeDecodesCorrectly(self):
        pass

    def testExecuteOpcodeExecutesCorrectly(self):
        pass


if __name__ == "__main__":
    unittest.main()
