import unittest
from tasks.task_2_function import INT


class test_correct_data(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_1(self):
        self.assertEqual(INT.integer(123), 321)

    def test_2(self):
        self.assertEqual(INT.integer(0), 0)

    def test_3(self):
        self.assertEqual(INT.integer(7777), 7777)

    def test_4(self):
        self.assertEqual(INT.integer('y'), 'Added value is not integer')

    def test_5(self):
        self.assertEqual(INT.integer(54.321), 123.45)

    def test_6(self):
        self.assertEqual(INT.integer(-1), 'The value is negative')

    def test_7(self):
        self.assertEqual(INT.integer(30), 3)

    def test_8(self):
        self.assertEqual(INT.integer([1,2,3]), 'Added value is not integer')

    def test_9(self):
        self.assertEqual(INT.integer(-0.9), 'The value is negative')

    def test_10(self):
        self.assertEqual(INT.integer({'a':'3'}), 'Added value is not integer')

    def test_11(self):
        self.assertEqual(INT.integer(''), 'Added value is not integer')




