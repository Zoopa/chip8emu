import unittest
from cpu import CPU
from memory import Memory
from screen import Screen
from cpu_constants import CpuConstants


class CpuTest(unittest.TestCase):

    def setUp(self):
        self.memory = Memory(CpuConstants.MEM_SIZE)
        self.screen = Screen(CpuConstants.SCREEN_W, CpuConstants.SCREEN_H)
        self.memory.setByte(
            CpuConstants.MEM_ADDRESS,
            (CpuConstants.OPCODE >> 8) & 0xFF
        )

        self.memory.setByte(
            CpuConstants.MEM_ADDRESS + 1,
            CpuConstants.OPCODE & 0xFF
        )

        self.cpu = CPU(self.memory, self.screen)
        self.cpu.programCounter = CpuConstants.PC_BEFORE

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
        self.cpu.increaseProgramCounter()
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldRaiseErrorOnWrongOpcode(self):
        with self.assertRaises(KeyError):
            self.cpu.executeOpcode(CpuConstants.OPCODE)

    def testShouldExecuteOpcodeANNNCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE_ANNN
        self.cpu.executeOpcodeANNN()
        self.assertEqual(self.cpu.indexRegister, CpuConstants.IR_ANNN)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldExecuteOpcodeFX15Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX15
        self.cpu.vRegister[CpuConstants.V_REG_FX15] = CpuConstants.V4_FX15
        self.cpu.executeOpcodeFX15()
        self.assertEqual(self.cpu.delayTimer, CpuConstants.DT_FX15)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldExecuteOpcodeFX18Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX18
        self.cpu.vRegister[CpuConstants.V_REG_FX18] = CpuConstants.V6_FX18
        self.cpu.executeOpcodeFX18()
        self.assertEqual(self.cpu.soundTimer, CpuConstants.ST_FX18)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def testShouldExecuteOpcode00E0Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_00E0
        self.cpu.executeOpcode00E0()
        self.assertTrue(
            self.cpu.screen.screen ==
            [0] * len(self.cpu.screen.screen)
        )

if __name__ == "__main__":
    unittest.main()
