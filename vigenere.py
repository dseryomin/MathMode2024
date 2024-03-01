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
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            j = i % len(keyword)
            if plaintext[i].islower():
                m = ord(plaintext[i]) - ord('a')
                k = ord(keyword[j]) - ord('a')
                c = (m + k) % 26
                ciphertext += chr(c + ord('a') )
            else:
                m = ord(plaintext[i]) - ord('A')
                k = ord(keyword[j]) - ord('A')
                c = (m + k) % 26
                ciphertext += chr(c + ord('A'))
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
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            j = i % len(keyword)
            if ciphertext[i].islower():
                c = ord(ciphertext[i]) - ord('a')
                k = ord(keyword[j]) - ord('a')
                m = (c - k) % 26
                plaintext += chr(m + ord('a'))
            else:
                c = ord(ciphertext[i]) - ord('A')
                k = ord(keyword[j]) - ord('A')
                m = (c - k) % 26
                plaintext += chr(m + ord('A'))
        else:
            plaintext += ciphertext[i]
    return plaintext
