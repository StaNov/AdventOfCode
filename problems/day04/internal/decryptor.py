class Decrypter:

    @staticmethod
    def decrypt(string, key):
        result = ""

        for char in string:
            if char == "-":
                decrypted = " "
            else:
                encrypted = ord(char) - ord("a")
                decrypted_int = (encrypted + key) % 26
                decrypted = chr(ord("a") + decrypted_int)

            result += decrypted

        return result
