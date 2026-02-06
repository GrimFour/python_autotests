import unittest
from homeworks.homework_12.HW12 import (
    multiplication_table,
    plus,
    avarage_func,
    reverse_string,
    longest_word,
    find_substring,
    final_temperature,
    perimeter,
    recordswaper,
    has_more_than_10_unique_chars,
)


class TestHW12(unittest.TestCase):

    # test for multiplication_table

    def test_multiplication_table_basic(self):
        self.assertEqual(
            multiplication_table(3),
            [
                "3x1=3",
                "3x2=6",
                "3x3=9",
                "3x4=12",
                "3x5=15",
                "3x6=18",
                "3x7=21",
                "3x8=24",
            ],
        )

    def test_multiplication_table_large_number(self):
        self.assertEqual(multiplication_table(30), [])

    # tests na plus

    def test_plus_positive(self):
        self.assertEqual(plus(2, 3), 5)

    def test_plus_negative(self):
        self.assertEqual(plus(-2, -3), -5)

    # test for avarage

    def test_average_normal(self):
        self.assertEqual(avarage_func([2, 4, 6]), 4)

    def test_average_empty_raises(self):
        with self.assertRaises(ValueError):
            avarage_func([])

    # test na reveers

    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

    # longest word

    def test_longest_word(self):
        self.assertEqual(longest_word(["a", "abcd", "abc"]), "abcd")

    def test_longest_word_empty(self):
        self.assertIsNone(longest_word([]))

    # test for find_substring

    def test_find_substring_found(self):
        self.assertEqual(find_substring("hello world", "world"), 6)

    def test_find_substring_not_found(self):
        self.assertEqual(find_substring("hello", "xyz"), -1)

    # test for temp

    def test_final_temperature(self):
        self.assertEqual(final_temperature(5, -10, 4), -1)

    # perimeter

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3, 4, 5), 14)

    # recordswaper

    def test_recordswaper(self):
        original = [1, 2, 3]
        swapped = recordswaper(original, 0, 2)

        self.assertEqual(swapped, [3, 2, 1])
        self.assertEqual(original, [1, 2, 3])

    # unique chars

    def test_unique_chars_true(self):
        self.assertTrue(has_more_than_10_unique_chars("abcdefghijk"))

    def test_unique_chars_false(self):
        self.assertFalse(has_more_than_10_unique_chars("aaaaabbbb"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
