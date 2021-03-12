from solutions.hw2.task2.cacher import FunctionCallArgumentsCache
from typing import Tuple
import unittest


def create_two_caches(args1: Tuple, kwargs1: dict, args2: Tuple, kwargs2: dict):
    first_call = FunctionCallArgumentsCache(args1, kwargs1)
    second_call = FunctionCallArgumentsCache(args2, kwargs2)
    return [first_call, second_call]


class FunctionCallArgumentsCacheTestEqual(unittest.TestCase):
    def test_equal_with_unnamed_args(self):
        call, same_call = create_two_caches((4, 5), {}, (4, 5), {})
        self.assertEqual(call, same_call)

    def test_equal_with_named_args_in_same_positions(self):
        call, same_call = create_two_caches((), {"a": 2, "b": 3}, (), {"a": 2, "b": 3})
        self.assertEqual(call, same_call)

    def test_equal_with_named_args_in_different_positions(self):
        call, call_reversed = create_two_caches((), {"a": 2, "b": 3}, (), {"b": 3, "a": 2})
        self.assertEqual(call, call_reversed)

    def test_not_equal_unnamed_args_in_different_positions(self):
        call, call_reversed = create_two_caches((1, 2), {}, (2, 1), {})
        self.assertNotEqual(call, call_reversed)

    def test_equal_mixed_args_in_same_positions(self):
        call, same_call = create_two_caches((1, 2), {"a": 2, "b": 3}, (1, 2), {"a": 2, "b": 3})
        self.assertEqual(call, same_call)

    def test_equal_mixed_args_but_named_in_different_positions(self):
        call, call_reversed = create_two_caches((1, 2), {"a": 2, "b": 3}, (1, 2), {"b": 3, "a": 2})
        self.assertEqual(call, call_reversed)


class FunctionCallArgumentsTestHash(unittest.TestCase):
    def test_equal_hashes_with_unnamed_args(self):
        call, same_call = create_two_caches((4, 5), {}, (4, 5), {})
        self.assertEqual(hash(call), hash(same_call))

    def test_equal_hashes_with_named_args_in_same_positions(self):
        call, same_call = create_two_caches((), {"a": 2, "b": 3}, (), {"a": 2, "b": 3})
        self.assertEqual(hash(call), hash(same_call))

    def test_not_equal_hashes_with_same_arguments_names_but_different_values(self):
        call, different_call = create_two_caches((), {"a": 2, "b": 3}, (), {"a": 3, "b": 4})
        self.assertNotEqual(call, different_call)

    def test_not_equal_hashes_with_different_arguments_names(self):
        call, different_call = create_two_caches((), {"a": 2, "b": 3}, (), {"c": 2, "d": 3})
        self.assertNotEqual(call, different_call)

    def test_equal_hashes_with_named_args_in_different_positions(self):
        call, call_reversed = create_two_caches((), {"a": 2, "b": 3}, (), {"b": 3, "a": 2})
        self.assertEqual(hash(call), hash(call_reversed))

    def test_not_equal_hashes_unnamed_args_in_different_positions(self):
        call, call_reversed = create_two_caches((1, 2), {}, (2, 1), {})
        self.assertNotEqual(hash(call), hash(call_reversed))

    def test_equal__hashes_mixed_args_in_same_positions(self):
        call, same_call = create_two_caches((1, 2), {"a": 2, "b": 3}, (1, 2), {"a": 2, "b": 3})
        self.assertEqual(hash(call), hash(same_call))

    def test_equal_hashes_mixed_args_but_named_in_different_positions(self):
        call, call_reversed = create_two_caches((1, 2), {"a": 2, "b": 3}, (1, 2), {"b": 3, "a": 2})
        self.assertEqual(hash(call), hash(call_reversed))
