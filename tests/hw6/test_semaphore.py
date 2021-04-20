import random
import unittest
from solutions.hw6.semaphore import Semaphore
from random import shuffle
import concurrent.futures


class MyTestCase(unittest.TestCase):
    class Counter:
        count: int
        semaphore: Semaphore

        def __init__(self):
            self.semaphore = Semaphore()
            self.count = 0

        def increment(self):
            with self.semaphore:
                self.count += 1

        def decrement(self):
            with self.semaphore:
                self.count -= 1

        def stressTest(self):
            tasks = [self.increment for i in range(1000)] + [self.decrement for i in range(1000)]
            random.seed(42)
            shuffle(tasks)
            for task in tasks:
                task()

    def test_one_thread_increment(self):
        counter = self.Counter()
        counter.increment()
        self.assertEqual(1, counter.count)

    def test_multiple_threads_increment(self):
        counter = self.Counter()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            [executor.submit(counter.stressTest) for i in range(100)]
        self.assertEqual(0, counter.count)

    def test_one_thread_adding_to_list(self):
        some_list = []
        with Semaphore():
            some_list.append("hello")
        self.assertEqual(len(some_list), 1)

    def test_multiple_threads_adding_to_list(self):
        semaphore = Semaphore()
        some_list = []

        def async_append():
            with semaphore:
                some_list.append("a")

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            [executor.submit(async_append) for i in range(100)]

        self.assertEqual(100, len(some_list))


if __name__ == "__main__":
    unittest.main()
