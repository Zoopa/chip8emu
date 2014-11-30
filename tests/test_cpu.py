import unittest
from cpu import CPU
from memory import Memory


class CpuTest(unittest.TestCase):

    def setUp(self):
        self.cpu = CPU(Memory())

    def tearDown(self):
        pass

    def testCpuHasMemory(self):
        self.assertIsInstance(self.cpu.memory, Memory)

    def testFetchOpcodeReadsCorrectOpcode(self):
        opcode = self.cpu.fetchOpcode()
        self.assertEqual(opcode, "0x1234")


if __name__ == "__main__":
    unittest.main()
