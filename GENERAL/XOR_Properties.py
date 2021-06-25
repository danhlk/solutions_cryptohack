key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2 = hex(int(key1, 16) ^ int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16))
key3 = hex(int(key2, 16) ^ int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16))
flag = hex(int(key3, 16) ^ int(key2, 16) ^ int(key1, 16) ^ int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16))
print(bytes.fromhex(str(flag)[2:]))
