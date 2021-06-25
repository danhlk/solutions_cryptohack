from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail.pem', 'r') as f:
    key = RSA.importKey(f.read())

print (key.d)
