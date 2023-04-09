
import os
print("read ASCI file with GSM data")
with open('18.09.22.TXT', 'r') as f:
    data = f.read()
    print(data)
f=os.listdir()
print(f)
print(f[1])
print(f[-1])
