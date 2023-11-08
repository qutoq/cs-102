def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""
    keyword = keyword.lower()
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('a')
            el = chr(ord('a') + (ord(plaintext[i].lower()) - ord('a') + shift) % 26)
            if plaintext[i].isupper():
                el = el.upper()
            ciphertext += el
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    plaintext = ""
    keyword = keyword.lower()
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('a')
            el = chr(ord('a') + (ord(ciphertext[i].lower()) - ord('a') - shift) % 26)
            if ciphertext[i].isupper():
                el = el.upper()
            plaintext += el
        else:
            plaintext += ciphertext[i]
    return plaintext
