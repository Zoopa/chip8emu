import unittest
from memory import Memory


class MemoryTest(unittest.TestCase):
    MEM_SIZE = 4096
    MEM_VALUE = 0xFF
    MEM_ADDRESS = 0x10
    MEM_ADDRESS_WRONG_LOW = -1
    MEM_ADDRESS_WRONG_HIGH = 4906

    def setUp(self):
        self.memory = Memory(self.MEM_SIZE)

    def tearDown(self):
        pass

    def testShouldReadCorrectBytes(self):
        self.memory.setByte(self.MEM_ADDRESS, self.MEM_VALUE)
        byte = self.memory.getByte(self.MEM_ADDRESS)
        self.assertEqual(byte, self.MEM_VALUE)

    def testShouldWriteCorrectBytes(self):
        self.memory.setByte(self.MEM_ADDRESS, self.MEM_VALUE)
        byte = self.memory.getByte(self.MEM_ADDRESS)
        self.assertEqual(byte, self.MEM_VALUE)

    def testShouldRaiseErrorOnIllegalMemoryAddressWrite(self):
        with self.assertRaises(IndexError):
            self.memory.setByte(self.MEM_ADDRESS_WRONG_LOW, self.MEM_VALUE)

        with self.assertRaises(IndexError):
            self.memory.setByte(self.MEM_ADDRESS_WRONG_HIGH, self.MEM_VALUE)

    def testShouldRaiseErrorOnIllegalMemoryAddressRead(self):
        with self.assertRaises(IndexError):
            self.memory.getByte(self.MEM_ADDRESS_WRONG_LOW)

        with self.assertRaises(IndexError):
            self.memory.getByte(self.MEM_ADDRESS_WRONG_HIGH)

    def testShouldReserveEnoughMemory(self):
        self.assertEqual(len(self.memory.memory), self.MEM_SIZE)


if __name__ == "__main__":
    unittest.main()
