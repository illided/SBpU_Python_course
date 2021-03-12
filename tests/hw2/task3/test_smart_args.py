import unittest
from solutions.hw2.task3.smart_args import Evaluated, Isolated, SmartArgs


class CallCounter:
    num_of_calls: int

    def __init__(self):
        self.num_of_calls = 0

    def get_num_of_call(self):
        self.num_of_calls += 1
        return self.num_of_calls


counter = CallCounter()


@SmartArgs
def check_evaluation_one_default(*, c=Evaluated(counter.get_num_of_call)) -> int:
    return c


class SmartArgsEvaluateTest(unittest.TestCase):
    def setUp(self) -> None:
        counter.num_of_calls = 0

    def test_when_only_default_was_used_check_with_default(self):
        check_evaluation_one_default()
        check_evaluation_one_default()
        self.assertEqual(3, check_evaluation_one_default())

    def test_when_only_default_was_used_check_with_manually_filled(self):
        check_evaluation_one_default()
        check_evaluation_one_default()
        self.assertEqual(1, check_evaluation_one_default(c=1))

    def test_when_arg_was_filled_manually_check_with_default(self):
        check_evaluation_one_default(c=1)
        check_evaluation_one_default(c=1)
        self.assertEqual(1, check_evaluation_one_default())

    def test_when_arg_was_filled_manually_check_with_manually_filled(self):
        check_evaluation_one_default(c=1)
        check_evaluation_one_default(c=1)
        self.assertEqual(1, check_evaluation_one_default(c=1))


class MixedUsageTest(unittest.TestCase):
    def test_trying_to_use_both_operation_evaluation_first(self):
        with self.assertRaises(Exception):

            @SmartArgs
            def example(*, a=Evaluated(Isolated())):
                return a

    def test_trying_to_use_both_operations_isolation_first(self):
        with self.assertRaises(Exception):

            @SmartArgs
            def example(*, a=Isolated(Evaluated())):
                return a


@SmartArgs
def check_isolation(*, d=Isolated()):
    d["a"] = 0
    return d


@SmartArgs
def check_deep_isolation(*, l=Isolated()):
    l[0] = [1, 2, 3]
    return l


class SmartArgsIsolatedTest(unittest.TestCase):
    def test_isolation_on_dict(self):
        mutable = {"a": 10}
        self.assertEqual({"a": 0}, check_isolation(d=mutable))
        self.assertEqual({"a": 10}, mutable)

    def test_isolation_when_no_arg(self):
        with self.assertRaises(Exception):
            check_isolation()

    def test_deep_isolation(self):
        mutable = [[0, 0], [0, 0]]
        self.assertEqual([[1, 2, 3], [0, 0]], check_deep_isolation(l=mutable))
        self.assertEqual([[0, 0], [0, 0]], mutable)


if __name__ == "__main__":
    unittest.main()
