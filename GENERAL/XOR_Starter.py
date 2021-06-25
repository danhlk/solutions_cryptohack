text = 'label'
flag = ''
for c in text:
    flag += chr(ord(c)^13)
print ('crypto{{{}}}'.format(flag))
