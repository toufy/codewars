# Vigenère Cipher Helper
# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str) -> None:
        self.key = key
        self.alphabet = alphabet
        self.genkey = lambda text: f"{self.key * (len(str(text))//len(self.key)+1)}"[
            : len(str(text))
        ]

    def encode(self, text: str):
        en_key = self.genkey(text)
        letters = list(text)
        for i in range(len(text)):
            char = letters[i]
            if char in self.alphabet:
                ciph = en_key[i]
                shift = self.alphabet.index(ciph) + self.alphabet.index(char)
                if shift >= len(self.alphabet):
                    shift -= len(self.alphabet)
                letters[i] = self.alphabet[shift]
        return "".join(letters)

    def decode(self, text: str):
        en_key = self.genkey(text)
        letters = list(text)
        for i in range(len(text)):
            char = letters[i]
            if char in self.alphabet:
                ciph = en_key[i]
                shift = self.alphabet.index(char) - self.alphabet.index(ciph)
                letters[i] = self.alphabet[shift]
        return "".join(letters)
