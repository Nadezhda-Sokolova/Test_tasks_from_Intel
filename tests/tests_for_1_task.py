import unittest
import tasks.task_1_function

class test_correct_data(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('30'), 30)

    def test_2(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('30s'), 30)

    def test_3(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('1y'), "Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")

    def test_4(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('10seconds'), 'Only 1 unit time can be added')

    def test_5(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('1'), 1)

    def test_6(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta(''),"Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")

    def test_7(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('60.5m'), 3630)

    def test_8(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('d'), 86400)

    def test_9(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('h'), 3600)

    def test_10(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('m'), 60)

    def test_11(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('10.5h'), 37800)

    def test_12(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('5.6d'), 483840)

    def test_13(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('1/2'), "Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")

    def test_14(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('10m5s'), 'Only 1 unit time can be added')

    def test_15(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('60.5M'),"Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")

    def test_16(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('1,6m'), "Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")

    def test_17(self):
        self.assertEqual(tasks.task_1_function.Specifier.Delta('1/6h'), "Unsupported time units have been added. Possible time units are 's', 'm', 'h', 'd' and possible format is number without '/'")


if __name__ == "__main__":
  unittest.main()

