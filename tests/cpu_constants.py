class CpuConstants(object):
    OPCODE = 0xA2F0
    DECODED_OPCODE = 0xA000
    INVALID_OPCODE = 0xFFFF
    PC_BEFORE = 0x200
    PC_AFTER = 0x202

    # MEM #
    MEM_SIZE = 4096
    MEM_ADDRESS = 0x0F24

    # SCREEN #
    SCREEN_W = 64
    SCREEN_H = 32

    # ANNN #
    OPCODE_ANNN = 0xABCD
    IR_ANNN = 0x0BCD

    # 2NNN #
    OPCODE_2NNN = 0x2ABC
    PC_2NNN = 0xABC
    SP_2NNN = 0x01
    PC_ON_STACK_2NNN = 0x200

    # FX15 #
    OPCODE_FX15 = 0xF415
    DT_FX15 = 0x1234
    V4_FX15 = 0x1234
    V_REG_FX15 = 4

    # FX18 #
    OPCODE_FX18 = 0xF615
    ST_FX18 = 0x1234
    V6_FX18 = 0x1234
    V_REG_FX18 = 6

    # 00E0 #
    OPCODE_00E0 = 0x00E0
