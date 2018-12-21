# writing bits to the file message.txt
#
#

import bitio 

file = open('message.txt', 'wb')

bitwrite = bitio.BitWriter(file)

bitstring = [87, 101, 32, 97, 114, 101, 32, 116, 104, 101, 32, 66, 111, 114, 103, 46,
10, 82, 101, 115, 105, 115, 116, 97, 110, 99, 101, 32, 105, 115, 32,
102, 117, 116, 105, 108, 101, 33, 10]

for num in range(len(bitstring)):
    bitstring[num] == chr(bitstring[num])

for i in range(len(bitstring)):
    try:
        write = bitwrite.writebits(bitstring[i], 8)
    except EOFError:
        break
print(write)