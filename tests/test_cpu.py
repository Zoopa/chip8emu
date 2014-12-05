import unittest
from unittest.mock import call, Mock
from cpu import CPU
from memory import Memory
from screen import Screen
from cpu_constants import CpuConstants
from unknown_opcode_exception import UnknownOpcodeException


class CpuTest(unittest.TestCase):

    def setUp(self):
        self.memory = Memory(CpuConstants.MEM_SIZE)
        self.screen = Screen(CpuConstants.SCREEN_W, CpuConstants.SCREEN_H)
        self.cpu = CPU(self.memory, self.screen)
        self.cpu.programCounter = CpuConstants.PC_BEFORE

    def tearDown(self):
        pass

    def assertProgramCounterIncreased(self):
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER)

    def assertProgramCounterNotIncreased(self):
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_BEFORE)

    def assertRegisterIsZero(self, register):
        self.assertTrue(register == 0x00)

    def testShouldHaveMemory(self):
        self.assertIsInstance(self.cpu.memory, Memory)

    def testShouldFullyInitialiseOpcodeTable(self):
        pass

    def testShouldInitialiseAllRegisters(self):
        self.assertEqual(self.cpu.vRegister, [0x0] * 8)
        self.assertRegisterIsZero(self.cpu.opcode)
        self.assertRegisterIsZero(self.cpu.indexRegister)
        self.assertRegisterIsZero(self.cpu.delayTimer)
        self.assertRegisterIsZero(self.cpu.soundTimer)
        self.assertRegisterIsZero(self.cpu.soundTimer)

        #setUp sets program counter...
        #self.assertRegisterIsZero(self.cpu.programCounter)

    def testShouldInitialiseStackAndPointer(self):
        self.assertEqual(self.cpu.stack, [])
        self.assertEqual(self.cpu.stackPointer, 0x00)

    def testShouldFetchCorrectOpcode(self):
        self.memory.getByte = Mock(return_value=CpuConstants.OPCODE)
        self.cpu.fetchOpcode(CpuConstants.MEM_ADDRESS)
        self.memory.getByte.assert_has_calls([
            call(CpuConstants.MEM_ADDRESS),
            call(CpuConstants.MEM_ADDRESS + 1)
        ])

    def testShouldDecodeOpcodeCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE
        decodedOpcode = self.cpu.decodeOpcode()
        self.assertEqual(decodedOpcode, CpuConstants.DECODED_OPCODE)

    def testShouldRaiseExceptionOnUnknownOpcode(self):
        with self.assertRaises(UnknownOpcodeException):
            self.cpu.opcode = CpuConstants.INVALID_OPCODE
            self.cpu.decodeOpcode()

    def testShouldDelegateOpcodeExecutionCorrectly(self):
        """ How? """
        pass

    def testShouldIncreaseProgramCounterByTwo(self):
        self.cpu.increaseProgramCounter()
        self.assertProgramCounterIncreased()

    def testShouldRaiseErrorOnWrongOpcode(self):
        with self.assertRaises(KeyError):
            self.cpu.executeOpcode(CpuConstants.OPCODE)

    def testShouldExecuteOpcodeANNNCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE_ANNN
        self.cpu.executeOpcodeANNN()
        self.assertEqual(self.cpu.indexRegister, CpuConstants.IR_ANNN)
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode2NNNCorrectly(self):
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcodeFX15Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX15
        self.cpu.vRegister[CpuConstants.V_REG_FX15] = CpuConstants.V4_FX15
        self.cpu.executeOpcodeFX15()
        self.assertEqual(self.cpu.delayTimer, CpuConstants.DT_FX15)
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcodeFX18Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX18
        self.cpu.vRegister[CpuConstants.V_REG_FX18] = CpuConstants.V6_FX18
        self.cpu.executeOpcodeFX18()
        self.assertEqual(self.cpu.soundTimer, CpuConstants.ST_FX18)
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode00E0Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_00E0
        self.screen.clear = Mock()
        self.cpu.executeOpcode00E0()
        self.screen.clear.assert_called_once_with()
        self.assertProgramCounterIncreased()
