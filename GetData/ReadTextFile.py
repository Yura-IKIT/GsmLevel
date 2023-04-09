#new branch develop

import os
print("read ASCI dile with GSM data")
with open('18.09.22.TXT', 'r') as d:
    data = d.read()
    print(data)
d.close()
d=os.listdir()
print(d)
print(d[1])
print(d[-1])
