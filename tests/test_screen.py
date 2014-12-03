import unittest
from screen import Screen


class ScreenTest(unittest.TestCase):
    SCREEN_W = 64
    SCREEN_H = 32

    def setUp(self):
        self.screen = Screen(self.SCREEN_W, self.SCREEN_H)

    def tearDown(self):
        pass

    def testShouldHaveCorrectSize(self):
        self.assertEqual(self.screen.width, self.SCREEN_W)
        self.assertEqual(self.screen.height, self.SCREEN_H)

    def testShouldChangeCorrectPixel(self):
        self.screen.setPixel(1, 1, True)
        pixel1 = self.screen.getPixel(1, 1)
        self.assertTrue(pixel1)

        self.screen.setPixel(1, 1, False)
        pixel2 = self.screen.getPixel(1, 1)
        self.assertFalse(pixel2)

    def testShouldBeClearedAfterInit(self):
        self.assertTrue(self.screen.screen == [0] * len(self.screen.screen))

    def testShouldFullyClearScreen(self):
        self.screen.setPixel(1, 1, True)
        self.screen.clear()
        self.assertTrue(self.screen.screen == [0] * len(self.screen.screen))
