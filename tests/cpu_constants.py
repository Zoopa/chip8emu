class CpuConstants(object):
    OPCODE = 0xA2F0
    DECODED_OPCODE = 0xA000
    INVALID_OPCODE = 0xFFFF
    PC_BEFORE = 0x200
    PC_AFTER = 0x202
    PC_AFTER_SKIP = 0x204

    # MEM #
    MEM_SIZE = 4096
    MEM_ADDRESS = 0x0F24

    # SCREEN #
    SCREEN_W = 64
    SCREEN_H = 32

    # ANNN #
    OPCODE_ANNN = 0xABCD
    IR_ANNN = 0x0BCD

    # 1NNN #
    OPCODE_1NNN = 0x1ABC
    PC_1NNN = 0xABC

    # 2NNN #
    OPCODE_2NNN = 0x2ABC
    PC_2NNN = 0xABC
    SP_2NNN = 0x01
    PC_ON_STACK_2NNN = 0x200

    # 3XNN #
    OPCODE_3XNN = 0x3456
    V_REG_3XNN = 4
    V4_3XNN_EQ = 0x56
    V4_3XNN_NEQ = 0x57

    # 4XNN #
    OPCODE_4XNN = 0x4567
    V_REG_4XNN = 5
    V5_4XNN_EQ = 0x67
    V5_4XNN_NEQ = 0x68

    # 5XY0 #
    OPCODE_5XY0 = 0x5670
    V_REG1_5XY0 = 6
    V_REG2_5XY0 = 7
    V6_5XY0_EQ = 0x12
    V7_5XY0_EQ = 0x12
    V7_5XY0_NEQ = 0x13

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
