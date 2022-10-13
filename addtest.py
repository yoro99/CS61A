import add
import unittest

class AddTest(unittest.TestCase):
    test_v = (
        (1,2),
        (3,4),
        (5,6),
        (10,11),
        (15,16)
    )
    def testadd(self):
        for v1,v2 in self.test_v:
            res = add.add(v1)
            self.assertEqual(res,v2)
    def test_outrange(self):
        self.assertRaises(add.OutOfRangeRrror,add.add,17)
    def test_int(self):
        self.assertRaises(add.NotIntegerError,add.add,0.1)


if __name__ == '__main__':
    unittest.main()