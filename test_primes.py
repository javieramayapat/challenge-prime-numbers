import unittest
from primes import get_primes


class TestGetPrimes(unittest.TestCase):
    def setUp(self):
        self.first_prime = 1
        self.first_six_primes = 6

        self.negative_number_of_primes = -2
        self.string_input = "second"
        self.boolean_input = True

        self.result_first_prime_number = [2]
        self.result_first_six_prime_numbers = [2, 3, 5, 7, 11, 13]

    def test_get_first_prime(self):
        self.assertAlmostEqual(
            get_primes(self.first_prime), self.result_first_prime_number
        )

    def test_get_the_six_first_primes(self):
        self.assertAlmostEqual(
            get_primes(self.first_six_primes), self.result_first_six_prime_numbers
        )

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            get_primes()

    def test_values(self):
        self.assertRaises(ValueError, get_primes, self.negative_number_of_primes)

    def test_types(self):
        self.assertRaises(TypeError, get_primes, self.string_input)

        self.assertRaises(TypeError, get_primes, self.boolean_input)
