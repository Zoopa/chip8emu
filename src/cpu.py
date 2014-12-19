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
            0x1000: self.executeOpcode1NNN,
            0x2000: self.executeOpcode2NNN,
            0x3000: self.executeOpcode3XNN,
            0x4000: self.executeOpcode4XNN,
            0x5000: self.executeOpcode5XY0,
            0x6000: self.executeOpcode6XNN,
            0x7000: self.executeOpcode7XNN,
            0x8000: self.executeOpcode8XY0,
            0x8001: self.executeOpcode8XY1,
            0x8002: self.executeOpcode8XY2,
            0x8003: self.executeOpcode8XY3,
            0x8004: self.executeOpcode8XY4,
            0x8005: self.executeOpcode8XY5,
            0x8006: None,
            0x8007: self.executeOpcode8XY7,
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
        self.vRegister = [0x00] * 16
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

    def setCarry(self, isSet):
        self.vRegister[0x0F] = 0x01 if isSet else 0x00

    def skipInstruction(self):
        self.programCounter += 4

    def executeOpcode00E0(self):
        """ Clear screen """
        self.screen.clear()
        self.increaseProgramCounter()

    def executeOpcode1NNN(self):
        """ Jump to address NNN """
        self.programCounter = self.opcode & ~self.OPCODE_MASK_4_BIT

    def executeOpcode2NNN(self):
        """ Call function at address NNN """
        self.stack[self.stackPointer] = self.programCounter
        self.stackPointer += 1
        self.programCounter = self.opcode & ~self.OPCODE_MASK_4_BIT

    def executeOpcode3XNN(self):
        """ Skip next instruction if VX == NN """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        nn = self.opcode & 0xFF

        if self.vRegister[x] == nn:
            self.skipInstruction()
        else:
            self.increaseProgramCounter()

    def executeOpcode4XNN(self):
        """ Skip next instruction if VX != NN """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        nn = self.opcode & 0xFF

        if self.vRegister[x] != nn:
            self.skipInstruction()
        else:
            self.increaseProgramCounter()

    def executeOpcode5XY0(self):
        """ Skip next instruction if VX == VY """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4

        if self.vRegister[x] == self.vRegister[y]:
            self.skipInstruction()
        else:
            self.increaseProgramCounter()

    def executeOpcode6XNN(self):
        """ Set VX to NN """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        nn = self.opcode & 0xFF
        self.vRegister[x] = nn
        self.increaseProgramCounter()

    def executeOpcode7XNN(self):
        """ Adds NN to VX """
        x = (self.opcode & ~self.OPCODE_MASK_12_BIT) >> 8
        nn = self.opcode & 0xFF
        vxVal = self.vRegister[x]
        self.vRegister[x] = (vxVal + nn) & 0xFF
        self.increaseProgramCounter()

    def executeOpcode8XY0(self):
        """ Set VX to VY """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        self.vRegister[x] = self.vRegister[y]
        self.increaseProgramCounter()

    def executeOpcode8XY1(self):
        """ Set VX to VX OR VY """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        self.vRegister[x] |= self.vRegister[y]
        self.increaseProgramCounter()

    def executeOpcode8XY2(self):
        """ Set VX to VX AND VY """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        self.vRegister[x] &= self.vRegister[y]
        self.increaseProgramCounter()

    def executeOpcode8XY3(self):
        """ Set VX to VX XOR VY """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        self.vRegister[x] ^= self.vRegister[y]
        self.increaseProgramCounter()

    def executeOpcode8XY4(self):
        """ Add VY to VX with carry in VF """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        val = self.vRegister[x] + self.vRegister[y]
        self.vRegister[x] = val & 0xFF
        self.setCarry(val > 0xFF)
        self.increaseProgramCounter()

    def executeOpcode8XY5(self):
        """ Subtract VY from VX with borrow in VF """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        val = self.vRegister[x] - self.vRegister[y]
        self.vRegister[x] = val & 0xFF
        self.setCarry(val > 0x00)
        self.increaseProgramCounter()

    def executeOpcode8XY7(self):
        """ Set VX to VY - VX with borrow in VF """
        x = (self.opcode & 0xF00) >> 8
        y = (self.opcode & 0xF0) >> 4
        val = self.vRegister[y] - self.vRegister[x]
        self.vRegister[x] = val & 0xFF
        self.setCarry(val > 0x00)
        self.increaseProgramCounter()

    def executeOpcodeANNN(self):
        """ Set index register to NNN """
        self.indexRegister = self.opcode & ~self.OPCODE_MASK_4_BIT
        self.increaseProgramCounter()

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
