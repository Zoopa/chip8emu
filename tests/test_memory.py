import unittest
import memory


class MemoryTest(unittest.TestCase):
    MEM_POSITION = 0x10
    MEM_VALUE = 0xFF
    MEM_SIZE = 4096
    MEM_ADDRESS_WRONG_LOW = -1
    MEM_ADDRESS_WRONG_HIGH = 4906

    def setUp(self):
        self.memory = memory.Memory(self.MEM_SIZE)

    def tearDown(self):
        pass

    def testGetByteReturnsCorrectValue(self):
        self.memory.setByte(self.MEM_POSITION, self.MEM_VALUE)
        byte = self.memory.getByte(self.MEM_POSITION)
        self.assertEqual(byte, self.MEM_VALUE)

    def testSetByteSetsCorrectValue(self):
        self.memory.setByte(self.MEM_POSITION, self.MEM_VALUE)
        byte = self.memory.getByte(self.MEM_POSITION)
        self.assertEqual(byte, self.MEM_VALUE)

    def testSetBytesRaisesErrorOnWrongPosition(self):
        with self.assertRaises(IndexError):
            self.memory.setByte(self.MEM_ADDRESS_WRONG_LOW, self.MEM_VALUE)

        with self.assertRaises(IndexError):
            self.memory.setByte(self.MEM_ADDRESS_WRONG_HIGH, self.MEM_VALUE)

    def testGetBytesRaisesErrorOnWrongPosition(self):
        with self.assertRaises(IndexError):
            self.memory.getByte(self.MEM_ADDRESS_WRONG_LOW)

        with self.assertRaises(IndexError):
            self.memory.getByte(self.MEM_ADDRESS_WRONG_HIGH)

    def testConstructorRequestsEnoughMemory(self):
        self.assertEqual(len(self.memory.memory), self.MEM_SIZE)


if __name__ == "__main__":
    unittest.main()
