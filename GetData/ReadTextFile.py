#branch about
import os
print("read ASCI file with GSM data")
with open('18.09.22.TXT', 'r') as f:
    data = f.read()
    print(data)
f.close()

fl=os.listdir()
print(fl)
print('fl[1]=',fl[1])
print('fl[-1]=',fl[-1])
