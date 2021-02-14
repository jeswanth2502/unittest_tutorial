import unittest
import calc

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        print("setupClass")
    @classmethod
    def tearDownClass(cls) :
        print("TeardownClass")
    def setUp(self):
        self.obj1 = calc.Car(10,5)
        self.obj2 = calc.Car(2,3)
        print("setup")
    def tearDown(self):
        print("teardown")
    def test_add(self):
        print("Test_add")
        self.assertEqual(self.obj1.add(self.obj2.x),12)
    def test_sub(self):
        print("Test_sub")
        self.assertTrue(self.obj1.sub(self.obj2.x),8)

    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
if __name__ == '__main__':
    unittest.main()
