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
        self.assertEqual(calc.Car.add(self.obj1.x,self.obj2.x),12)
    def test_sub(self):

        print("Test_sub")
        self.assertTrue(calc.Car.sub(self.obj1.x,self.obj2.x),8)
if __name__ == '__main__':
    unittest.main()
