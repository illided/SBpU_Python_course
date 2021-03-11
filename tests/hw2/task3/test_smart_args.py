import unittest
from solutions.hw2.task3.smart_args import Evaluated, Isolated, SmartArgs
import random


def get_random_number():
    return random.randint(0, 100)


@SmartArgs
def check_evaluation(*, x=get_random_number(), y=Evaluated(get_random_number)):
    print(x,y)

@SmartArgs
def check_isolation(*, d=Isolated()):
  d['a'] = 0
  return d

class SmartArgsEvaluateTest(unittest.TestCase):
    def test_something(self):
        check_evaluation()
        check_evaluation()
        check_evaluation()
        check_evaluation(y=150)

class SmartArgsIsolatedTest(unittest.TestCase):
    def test_something(self):
        no_mutable = {'a': 10}

        print(check_isolation(d=no_mutable))
        print(no_mutable)

if __name__ == "__main__":
    unittest.main()
