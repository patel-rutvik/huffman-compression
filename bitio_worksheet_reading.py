# bitio worksheet 

# Part 1

import bitio

file = open('simple.txt', 'rb')

bitread = bitio.BitReader(file)

finalbits = [] 
n = 0

try:
    while True:
        bit = bitread.readbits(8)
            # print("x \n",bit)
# https://www.afternerd.com/blog/how-to-print-without-a-newline-in-python/
        print(bit, ' ', chr(bit))
except:
    file.close()

file.close()

    

