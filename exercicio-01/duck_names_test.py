import unittest

from duck_names import (
    add_suffix_for_ducks_names,
)

letters = "JKLMNOPQ"

class AddNameSuffixTest(unittest.TestCase):
    def test_if_added_suffix_is_the_expected(self):
        self.assertEqual(add_suffix_for_ducks_names(letters), "Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack.")


if __name__ == "__main__":
    unittest.main()
