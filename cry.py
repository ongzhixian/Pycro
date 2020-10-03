from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64



# Encryption
# This should be fired as a single block
iv = base64.b64decode("PPPlOzBmlPUU19DuwVL1DQ==")
key = base64.b64decode("ULNbqFiOwBJ0toUblofd5aYygZoURP8m5XaoS2MvGw4=")
aes = AES.new(key, AES.MODE_CBC, iv=iv)
data = "zxcasd".encode("utf8")
encrypted_bytes = aes.encrypt(pad(data, AES.block_size))
base64.b64encode(encrypted_bytes)
# This will yield the result: b'Stg6Gw9IfPNmr+7rbYiFKQ=='

# Decryption
# This should be fired as a single block
iv = base64.b64decode("PPPlOzBmlPUU19DuwVL1DQ==")
key = base64.b64decode("ULNbqFiOwBJ0toUblofd5aYygZoURP8m5XaoS2MvGw4=")
aes = AES.new(key, AES.MODE_CBC, iv=iv)
encrypted_bytes = base64.b64decode("Stg6Gw9IfPNmr+7rbYiFKQ==")
plain_text = aes.decrypt(encrypted_bytes)
str(unpad(plain_text, 16), 'utf8')
