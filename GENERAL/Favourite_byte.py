def xor_single_byte(text : str, key : int) -> str:
    return ''.join([chr(ord(c)^key) for c in text])

data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d').decode('utf-8')

for i in range(256):
    flag = xor_single_byte(data, i)
    if 'crypto' in flag:
        print ('{}')
        exit(0)
#crypto{0x10_15_my_f4v0ur173_by7e}
