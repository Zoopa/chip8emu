import unittest
import memory


class CpuTest(unittest.TestCase):

    def setUp(self):
        self.memory = memory.Memory(4096)

    def tearDown(self):
        pass

    def testGetByteReturnsCorrectValue(self):
        self.memory.setByte(0x10, 0xFF)
        byte = self.memory.getByte(0x10)
        self.assertEqual(byte, 0xFF)

    def testSetByteSetsCorrectValue(self):
        self.memory.setByte(0x10, 0xFF)
        byte = self.memory.getByte(0x10)
        self.assertEqual(byte, 0xFF)

    def testSetBytesRaisesErrorOnWrongPosition(self):
        with self.assertRaises(IndexError):
            self.memory.setByte(-1, 0xFF)

        with self.assertRaises(IndexError):
            self.memory.setByte(4096, 0xFF)

    def testGetBytesRaisesErrorOnWrongPosition(self):
        with self.assertRaises(IndexError):
            self.memory.getByte(-1)

        with self.assertRaises(IndexError):
            self.memory.getByte(4096)

    def testConstructorRequestsEnoughMemory(self):
        self.assertEqual(len(self.memory.memory), 4096)


if __name__ == "__main__":
    unittest.main()
