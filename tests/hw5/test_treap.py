from unittest import TestCase
from solutions.hw5.treap import Deramida


class TestDeramida(TestCase):
    def test_set_and_get_one_item(self):
        der = Deramida()
        der[0] = "Hello"
        self.assertEqual("Hello", der[0])

    def test_set_and_get_many_items(self):
        der = Deramida()
        keys = [45, 2, -4, 6, 12]
        values = ["Sometimes", "i", "dream", "about", "cheese"]
        for key, value in zip(keys, values):
            der[key] = value
        self.assertTrue(all([der[key] == value for key, value in zip(keys, values)]))

    def test_set_and_get_rewrite_one(self):
        der = Deramida()
        der[0] = "Hello"
        der[0] = "World"
        self.assertEqual("World", der[0])

    def test_set_and_get_rewrite_many(self):
        der = Deramida()
        keys = [10, -2, 4, 64, 12]
        old_values = ["Sometimes", "i", "dream", "about", "cheese"]
        new_values = ["But", "sometimes", "i", "eat", "vegetables"]
        for key, value in zip(keys, old_values):
            der[key] = value
        for key, value in zip(keys, new_values):
            der[key] = value
        self.assertTrue(all([der[key] == value for key, value in zip(keys, new_values)]))

    def test_delete_one_time(self):
        der = Deramida()
        der[0] = "Hello"
        del der[0]
        with self.assertRaises(KeyError):
            a = der[0]

    def test_delete_one_item_twice(self):
        der = Deramida()
        der[0] = "Hello"
        del der[0]
        with self.assertRaises(KeyError):
            del der[0]

    def test_delete_many_items(self):
        der = Deramida()
        keys = [-2, 3, -4, 5, -6]
        for key in keys:
            der[key] = "a"
        for key in keys:
            del der[key]
            with self.assertRaises(KeyError):
                a = der[key]

    def test_delete_many_items_twice(self):
        der = Deramida()
        keys = [-2, 3, -4, 5, -6]
        for key in keys:
            der[key] = "a"
        for key in keys:
            del der[key]
            with self.assertRaises(KeyError):
                del der[key]

    def test_get_length_empty(self):
        der = Deramida()
        self.assertEqual(0, len(der))

    def test_get_length_one_item(self):
        der = Deramida()
        der[1] = "Hello"
        self.assertEqual(1, len(der))

    def test_get_length_many_items(self):
        der = Deramida()
        for i in range(1, 101):
            der[i] = i
            der[-1 * i] = i
        self.assertEqual(200, len(der))

    def test_get_length_where_one_item_deleted(self):
        der = Deramida()
        der[0] = "Hello"
        der[1] = "world"
        del der[1]
        self.assertEqual(len(der), 1)

    def test_get_length_where_all_items_deleted(self):
        der = Deramida()
        for i in range(1, 100):
            der[i] = i
            der[-1 * i] = i
        for i in range(1, 100):
            del der[i]
            del der[-1 * i]
        self.assertEqual(0, len(der))

    def test_contains_one_key(self):
        der = Deramida()
        der[0] = "Hello"
        self.assertTrue(0 in der)

    def test_does_not_contains_key_after_deletion(self):
        der = Deramida()
        der[0] = "Hello"
        del der[0]
        self.assertFalse(0 in der)

    def test_iteration_one_item(self):
        der = Deramida()
        der[0] = "Hello"
        items = [item for item in der]
        self.assertEqual(["Hello"], items)

    def test_iteration_many_items(self):
        der = Deramida()
        keys = [-1, 1, -2, 2]
        for key in keys:
            der[key] = str(key)
        items = [item for item in der]
        self.assertEqual(["-2", "-1", "1", "2"], items)

    def test_reversed_iteration_one_item(self):
        der = Deramida()
        der[0] = "Hello"
        items = [item for item in reversed(der)]
        self.assertEqual(["Hello"], items)

    def test_reversed_iteration_many_items(self):
        der = Deramida()
        keys = [-1, 1, -2, 2]
        for key in keys:
            der[key] = str(key)
        items = [item for item in reversed(der)]
        self.assertEqual(["2", "1", "-1", "-2"], items)

    def test_basic_balance(self):
        der = Deramida()
        for i in range(100):
            der[i] = i
            der[-1 * i] = i
        self.assertFalse(der.root.right_child is None or der.root.left_child is None)
