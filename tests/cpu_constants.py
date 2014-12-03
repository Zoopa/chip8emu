class CpuConstants(object):
    MEM_SIZE = 4096
    MEM_ADDRESS = 0x10
    OPCODE = 0xA2F0
    DECODED_OPCODE = 0xA000
    PC_BEFORE = 0x16
    PC_AFTER = 0x18

    # ANNN #
    ANNN_OPCODE = 0xABCD
    ANNN_IR = 0x0BCD

    # FX15 #
    FX15_OPCODE = 0xF415
    FX15_DT = 0x1234
    FX15_V4 = 0x1234
    FX15_V_IDX = 4

    # FX18 #
    FX18_OPCODE = 0xF615
    FX18_ST = 0x1234
    FX18_V6 = 0x1234
    FX18_V_IDX = 6
