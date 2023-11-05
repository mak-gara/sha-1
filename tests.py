import unittest
import time
from hashlib import sha1

from sha_1 import SHA1


def measure_time(func):
    start_time = time.perf_counter()
    result = func()
    execution_time = time.perf_counter() - start_time
    return result, execution_time


class SHA1TestCase(unittest.TestCase):
    def test_hash(self):
        """Hash match test with library implementation."""

        input_messages = [
            "Hello World",
            "Cryptography for Developers",
            "SHA-1",
            "Keccak",
            "Theta function"
        ]

        for message in input_messages:
            custom, custom_exec_time = measure_time(SHA1(message).hash)
            standard, standard_exec_time = measure_time(sha1(bytes(message, "utf-8")).hexdigest)

            print(f"\n\nInput message: {message}")
            print(f"Custom implementation:\t{custom} \tExecution time: {custom_exec_time}\tseconds")
            print(f"Library implementation:\t{standard}\tExecution time: {standard_exec_time}\tseconds")

            self.assertEqual(custom, standard)


if __name__ == '__main__':
    unittest.main()
