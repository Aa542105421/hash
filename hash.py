import hashlib
import sys

password = []
with open('password.txt','r') as OAO:
    for line in OAO:
        currentPlace = line [:-1]
        password.append(currentPlace)

if len(sys.argv)>1:
    msg = sys.argv[1].encode()
    hashvalue = hashlib.sha256(msg)
    print(hashvalue)
    print(hashvalue.hexdigest().upper())
