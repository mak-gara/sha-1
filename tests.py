import unittest
from hashlib import sha1

from sha_1 import SHA1


class SHA1TestCase(unittest.TestCase):
    def test_hash(self):
        input_messages = [
            "Hello World",
            "Cryptography for Developers",
            "SHA-1",
            "Keccak",
            "Theta function"
        ]

        for message in input_messages:
            custom = SHA1(message).hash()
            standard = sha1(bytes(message, "utf-8")).hexdigest()

            self.assertEqual(custom, standard)

            print(f"Input message: {message}\n"
                  f"Custom implementation: {custom}\n"
                  f"Standard: {standard}\n\n")


if __name__ == '__main__':
    unittest.main()
