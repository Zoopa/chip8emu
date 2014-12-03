import unittest
from cpu import CPU
from memory import Memory
from cpu_constants import CpuConstants


class CpuTest(unittest.TestCase):

    def setUp(self):
        self.memory = Memory(CpuConstants.MEM_SIZE)
        self.memory.setByte(
            CpuConstants.MEM_ADDRESS,
            (CpuConstants.OPCODE >> 8) & 0xFF
        )

        self.memory.setByte(
            CpuConstants.MEM_ADDRESS + 1,
            CpuConstants.OPCODE & 0xFF
        )

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
        opcode = self.cpu.fetchOpcode(CpuConstants.MEM_ADDRESS)
        self.assertEqual(opcode, CpuConstants.OPCODE)

    def testShouldDecodeOpcodeCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE
        decodedOpcode = self.cpu.decodeOpcode()
        self.assertEqual(decodedOpcode, CpuConstants.DECODED_OPCODE)

    def testShouldDelegateOpcodeExecutionCorrectly(self):
        """ How? """
        pass

    def testShouldIncreaseProgramCounterByTwo(self):
        self.cpu.programCounter = CpuConstants.PC_BEFORE
        self.cpu.increaseProgramCounter()
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldRaiseErrorOnWrongOpcode(self):
        with self.assertRaises(KeyError):
            self.cpu.executeOpcode(CpuConstants.OPCODE)

    def testShouldExecuteOpcodeANNNCorrectly(self):
        self.cpu.opcode = CpuConstants.ANNN_OPCODE
        self.cpu.programCounter = CpuConstants.PC_BEFORE

        self.cpu.executeOpcodeANNN()

        self.assertEqual(self.cpu.indexRegister, CpuConstants.ANNN_IR)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldExecuteOpcodeFX15Correctly(self):
        self.cpu.opcode = CpuConstants.FX15_OPCODE
        self.cpu.programCounter = CpuConstants.PC_BEFORE
        self.cpu.vRegister[CpuConstants.FX15_V_IDX] = CpuConstants.FX15_V4

        self.cpu.executeOpcodeFX15()

        self.assertEqual(self.cpu.delayTimer, CpuConstants.FX15_DT)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldExecuteOpcodeFX18Correctly(self):
        self.cpu.opcode = CpuConstants.FX18_OPCODE
        self.cpu.programCounter = CpuConstants.PC_BEFORE
        self.cpu.vRegister[CpuConstants.FX18_V_IDX] = CpuConstants.FX18_V6

        self.cpu.executeOpcodeFX18()

        self.assertEqual(self.cpu.soundTimer, CpuConstants.FX18_ST)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

if __name__ == "__main__":
    unittest.main()
