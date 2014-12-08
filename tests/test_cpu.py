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

    def assertInstructionSkipped(self):
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_AFTER_SKIP)

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
        self.assertEqual(self.cpu.stack, [0x00] * 16)
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

    def testShouldIncreaseProgramCounterByFourOnSkip(self):
        self.cpu.skipInstruction()
        self.assertInstructionSkipped()

    def testShouldRaiseErrorOnWrongOpcode(self):
        with self.assertRaises(KeyError):
            self.cpu.executeOpcode(CpuConstants.OPCODE)

    def testShouldExecuteOpcode00E0Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_00E0
        self.screen.clear = Mock()
        self.cpu.executeOpcode00E0()
        self.screen.clear.assert_called_once_with()
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcodeANNNCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE_ANNN
        self.cpu.executeOpcodeANNN()
        self.assertEqual(self.cpu.indexRegister, CpuConstants.IR_ANNN)
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode1NNNCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE_1NNN
        self.cpu.executeOpcode1NNN()
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_1NNN)

    def testShouldExecuteOpcode2NNNCorrectly(self):
        oldSp = self.cpu.stackPointer
        self.cpu.opcode = CpuConstants.OPCODE_2NNN
        self.cpu.executeOpcode2NNN()
        self.assertEqual(self.cpu.stackPointer, CpuConstants.SP_2NNN)
        self.assertEqual(self.cpu.programCounter, CpuConstants.PC_2NNN)
        self.assertEqual(self.cpu.stack[oldSp], CpuConstants.PC_ON_STACK_2NNN)

    def testShouldSkipInstructionForOpcode3XNN(self):
        self.cpu.opcode = CpuConstants.OPCODE_3XNN
        self.cpu.vRegister[CpuConstants.X_3XNN] = CpuConstants.VX_3XNN_EQ
        self.cpu.executeOpcode3XNN()
        self.assertInstructionSkipped()

    def testShouldNotSkipInstructionForOpcode3XNN(self):
        self.cpu.opcode = CpuConstants.OPCODE_3XNN
        self.cpu.vRegister[CpuConstants.X_3XNN] = CpuConstants.VX_3XNN_NEQ
        self.cpu.executeOpcode3XNN()
        self.assertProgramCounterIncreased()

    def testShouldSkipInstructionForOpcode4XNN(self):
        self.cpu.opcode = CpuConstants.OPCODE_4XNN
        self.cpu.vRegister[CpuConstants.X_4XNN] = CpuConstants.VX_4XNN_NEQ
        self.cpu.executeOpcode4XNN()
        self.assertInstructionSkipped()

    def testShouldNotSkipInstructionForOpcode4XNN(self):
        self.cpu.opcode = CpuConstants.OPCODE_4XNN
        self.cpu.vRegister[CpuConstants.X_4XNN] = CpuConstants.VX_4XNN_EQ
        self.cpu.executeOpcode4XNN()
        self.assertProgramCounterIncreased()

    def testShouldSkipInstructionForOpcode5XY0(self):
        self.cpu.opcode = CpuConstants.OPCODE_5XY0
        self.cpu.vRegister[CpuConstants.X_5XY0] = CpuConstants.VX_5XY0_EQ
        self.cpu.vRegister[CpuConstants.Y_5XY0] = CpuConstants.VY_5XY0_EQ
        self.cpu.executeOpcode5XY0()
        self.assertInstructionSkipped()

    def testShouldNotSkipInstructionForOpcode5XY0(self):
        self.cpu.opcode = CpuConstants.OPCODE_5XY0
        self.cpu.vRegister[CpuConstants.X_5XY0] = CpuConstants.VX_5XY0_EQ
        self.cpu.vRegister[CpuConstants.Y_5XY0] = CpuConstants.VY_5XY0_NEQ
        self.cpu.executeOpcode5XY0()
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode6XNNCorrectly(self):
        self.cpu.opcode = CpuConstants.OPCODE_6XNN
        self.cpu.executeOpcode6XNN()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_6XNN],
            CpuConstants.VX_6XNN
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode7XNNWithoutOverflow(self):
        self.cpu.opcode = CpuConstants.OPCODE_7XNN
        self.cpu.vRegister[CpuConstants.X_7XNN] = CpuConstants.VX_7XNN_LO
        self.cpu.executeOpcode7XNN()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_7XNN],
            CpuConstants.VX_7XNN_SUM
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode7XNNWithOverflow(self):
        self.cpu.opcode = CpuConstants.OPCODE_7XNN_OVERFLOW
        self.cpu.vRegister[CpuConstants.X_7XNN] = CpuConstants.VX_7XNN_HI
        self.cpu.executeOpcode7XNN()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_7XNN],
            CpuConstants.VX_7XNN_SUM
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode8XY0Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_8XY0
        self.cpu.vRegister[CpuConstants.X_8XY0] = CpuConstants.VX_8XY0_OLD
        self.cpu.vRegister[CpuConstants.Y_8XY0] = CpuConstants.VY_8XY0
        self.cpu.executeOpcode8XY0()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_8XY0],
            CpuConstants.VX_8XY0_NEW
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode8XY1Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_8XY1
        self.cpu.vRegister[CpuConstants.X_8XY1] = CpuConstants.VX_8XY1_OLD
        self.cpu.vRegister[CpuConstants.Y_8XY1] = CpuConstants.VY_8XY1
        self.cpu.executeOpcode8XY1()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_8XY1],
            CpuConstants.VX_8XY1_NEW
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode8XY2Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_8XY2
        self.cpu.vRegister[CpuConstants.X_8XY2] = CpuConstants.VX_8XY2_OLD
        self.cpu.vRegister[CpuConstants.Y_8XY2] = CpuConstants.VY_8XY2
        self.cpu.executeOpcode8XY2()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_8XY2],
            CpuConstants.VX_8XY2_NEW
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcode8XY3Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_8XY3
        self.cpu.vRegister[CpuConstants.X_8XY3] = CpuConstants.VX_8XY3_OLD
        self.cpu.vRegister[CpuConstants.Y_8XY3] = CpuConstants.VY_8XY3
        self.cpu.executeOpcode8XY3()
        self.assertEqual(
            self.cpu.vRegister[CpuConstants.X_8XY3],
            CpuConstants.VX_8XY3_NEW
        )
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcodeFX15Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX15
        self.cpu.vRegister[CpuConstants.X_FX15] = CpuConstants.VX_FX15
        self.cpu.executeOpcodeFX15()
        self.assertEqual(self.cpu.delayTimer, CpuConstants.DT_FX15)
        self.assertProgramCounterIncreased()

    def testShouldExecuteOpcodeFX18Correctly(self):
        self.cpu.opcode = CpuConstants.OPCODE_FX18
        self.cpu.vRegister[CpuConstants.X_FX18] = CpuConstants.VX_FX18
        self.cpu.executeOpcodeFX18()
        self.assertEqual(self.cpu.soundTimer, CpuConstants.ST_FX18)
        self.assertProgramCounterIncreased()
