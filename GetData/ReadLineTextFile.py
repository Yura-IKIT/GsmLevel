
import os
print("read line filerom ASCI fileile with GSM data")
with open('18.09.22.TXT', 'r') as file:
     # Read the file line by line
    for line in file:
        # Print each line
        print(line)
file.close()