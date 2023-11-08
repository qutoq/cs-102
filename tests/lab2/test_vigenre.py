import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


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


if __name__ == "__main__":
    unittest.main()
