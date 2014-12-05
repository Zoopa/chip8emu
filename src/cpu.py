from unknown_opcode_exception import UnknownOpcodeException


class CPU(object):
    OPCODE_MASK_4_BIT = 0xF000
    OPCODE_MASK_8_BIT = 0xF00F
    OPCODE_MASK_12_BIT = 0xF0FF

    def __init__(self, memory, screen):
        self.memory = memory
        self.screen = screen
        self.initialiseRegisters()
        self.initialiseInstructionTable()
        self.initialiseStack()

    def initialiseInstructionTable(self):
        self.opcodeTable = {
            0x0000: None,
            0x00E0: self.executeOpcode00E0,
            0x00EE: None,
            0x1000: None,
            0x2000: self.executeOpcode2NNN,
            0x3000: None,
            0x4000: None,
            0x5000: None,
            0x6000: None,
            0x7000: None,
            0x8000: None,
            0x8001: None,
            0x8002: None,
            0x8003: None,
            0x8004: None,
            0x8005: None,
            0x8006: None,
            0x8007: None,
            0x800E: None,
            0x9000: None,
            0xA000: self.executeOpcodeANNN,
            0xB000: None,
            0xC000: None,
            0xD000: None,
            0xE09E: None,
            0xE0A1: None,
            0xF007: None,
            0xF00A: None,
            0xF015: self.executeOpcodeFX15,
            0xF018: self.executeOpcodeFX18,
            0xF01E: None,
            0xF029: None,
            0xF033: None,
            0xF055: None,
            0xF065: None,
        }

    def initialiseStack(self):
        self.stack = [0x00] * 16
        self.stackPointer = 0x00

    def initialiseRegisters(self):
        self.opcode = 0x00
        self.programCounter = 0x200
        self.indexRegister = 0x00
        self.vRegister = [0x00] * 8
        self.delayTimer = 0x00
        self.soundTimer = 0x00

    def nextCycle(self):
        pass

    def fetchOpcode(self, address):
        firstHalf = self.memory.getByte(address) << 8
        secondHalf = self.memory.getByte(address + 1)
        return firstHalf | secondHalf

    def decodeOpcode(self):
        # TODO: does this match 0x00E0 vs 0x000?
        for mask in [
            self.OPCODE_MASK_4_BIT,
            self.OPCODE_MASK_8_BIT,
            self.OPCODE_MASK_12_BIT
        ]:
            decodedOpcode = self.opcode & mask

            if decodedOpcode in self.opcodeTable:
                return decodedOpcode

        raise UnknownOpcodeException()

    def executeOpcode(self, decodedOpcode):
        self.opcodeTable[decodedOpcode]()

    def increaseProgramCounter(self):
        self.programCounter += 2

    def executeOpcode00E0(self):
        """ Clear screen """
        self.screen.clear()
        self.increaseProgramCounter()

    def executeOpcodeANNN(self):
        """ Set index register to NNN """
        self.indexRegister = self.opcode & ~self.OPCODE_MASK_4_BIT
        self.increaseProgramCounter()

    def executeOpcode2NNN(self):
        """ Call function at address NNN """
        self.stack[self.stackPointer] = self.programCounter
        self.stackPointer += 1
        self.programCounter = self.opcode & ~self.OPCODE_MASK_4_BIT

    def executeOpcodeFX15(self):
        """ Set delay timer to value of register VX """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        self.delayTimer = self.vRegister[x]
        self.increaseProgramCounter()

    def executeOpcodeFX18(self):
        """ Set sound timer to value of register VX """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        self.soundTimer = self.vRegister[x]
        self.increaseProgramCounter()
