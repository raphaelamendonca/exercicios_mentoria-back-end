import unittest

from duckNames import (
    addNameSuffix,
)

duckNames = "JKLMNOPQ"

class AddNameSuffixTest(unittest.TestCase):
    def test_addNameSuffix(self):
        self.assertEqual(addNameSuffix(duckNames), "Jack, Kack, Lack, Mack, Nack, Ouack, Pack e Quack.")


if __name__ == "__main__":
    unittest.main()
