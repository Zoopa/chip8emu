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

    def testShouldBeClearedAfterInit(self):
        self.assertTrue(self.screen.screen == [0] * len(self.screen.screen))
