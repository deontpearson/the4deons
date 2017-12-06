from random import
import base64
from Crypto.Cipher import AES
from Crypto import Random


class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

rnd = randint(10000,99999)

res = "Kec1leNIw8qTjrvaCgyhgnoho6YtxVc0/hVrHme0CeFQD+WqvG8HvnXHUYoTEgdQlXSG+c4KA9Zi3B3r/bl7eg=="

print rnd
