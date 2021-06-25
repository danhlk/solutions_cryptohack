from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode()))
print(xor(flag, 'myXORkey'.encode()))
#crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
