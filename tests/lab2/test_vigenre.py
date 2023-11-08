import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
import random, string


class TestVigenere(unittest.TestCase):
    # len keyword > 0
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(encrypt_vigenere('Test', 'ododo'), 'Hhgw')
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere('PYTHON', 'A'), 'PYTHON')
        self.assertEqual(decrypt_vigenere('Hhgw', 'ododo'), 'Test')
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))


if __name__ == "__main__":
    unittest.main()
