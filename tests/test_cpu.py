import unittest
from cpu import CPU
from memory import Memory


class CpuTest(unittest.TestCase):
    MEM_SIZE = 4096
    MEM_ADDRESS = 0x10
    OPCODE = 0xA2F0
    DECODED_OPCODE = 0xA000
    INDEX_REGISTER_A000 = 0x02F0

    def setUp(self):
        self.memory = Memory(self.MEM_SIZE)
        self.memory.setByte(self.MEM_ADDRESS, (self.OPCODE >> 8) & 0xFF)
        self.memory.setByte(self.MEM_ADDRESS + 1, self.OPCODE & 0xFF)
        self.cpu = CPU(self.memory)

    def tearDown(self):
        pass

    def testShouldHaveMemory(self):
        self.assertIsInstance(self.cpu.memory, Memory)

    def testShouldFullyInitialiseOpcodeTable(self):
        pass

    def testShouldInitialiseAllRegisters(self):
        pass

    def testShouldFetchCorrectOpcode(self):
        opcode = self.cpu.fetchOpcode(self.MEM_ADDRESS)
        self.assertEqual(opcode, self.OPCODE)

    def testShouldDecodeOpcodeCorrectly(self):
        self.cpu.opcode = self.OPCODE
        decodedOpcode = self.cpu.decodeOpcode()
        self.assertEqual(decodedOpcode, self.DECODED_OPCODE)

    def testShouldDelegateOpcodeExecutionCorrectly(self):
        """ How? """
        pass

    def testShouldRaiseErrorOnWrongOpcode(self):
        with self.assertRaises(KeyError):
            self.cpu.executeOpcode(self.OPCODE)

    def testShouldExecuteOpcodeA000Correctly(self):
        self.cpu.opcode = self.OPCODE
        pc = self.cpu.programCounter
        self.cpu.executeOpcodeA000()
        self.assertEqual(self.cpu.indexRegister, self.INDEX_REGISTER_A000)
        self.assertEqual(self.cpu.programCounter, pc + 2)


if __name__ == "__main__":
    unittest.main()
