import hashlib
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class EncryptionConfig(object):

    def sha512(input):
        hashed_input = hashlib.sha512(input.encode('utf-8'))
        hex_dig = hashed_input.hexdigest()
        return hex_dig

    def AES128(self, enc_key, input, enc_iv):
        data = input.encode()
        key = enc_key.encode()
        iv = enc_iv.encode()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode()
        ct = b64encode(ct_bytes).decode()
        return ct

