#!/usr/bin/python3

from cryptography.fernet import Fernet

cipher_key = Fernet.generate_key()
cipher = Fernet(cipher_key)

with open("token.pickle", "rb") as file:
    token = cipher.encrypt(file.read())
    with open("../c_token", "ab") as file2:
        file2.write(token)

with open("trpo-bot-1eb977889b18.json", "rb") as file:
    json = cipher.encrypt(file.read())
    with open("../c_json", "ab") as file2:
        file2.write(json)

with open("config_Mail.py", "rb") as file:
    config = cipher.encrypt(file.read())
    with open("../c_config", "ab") as file2:
        file2.write(config)

with open("../c_config2", "ab") as file:
    file.write(cipher_key)
    file.write(cipher_key)

# decrypted_text = cipher.decrypt(encrypted_text)
# print(decrypted_text)
