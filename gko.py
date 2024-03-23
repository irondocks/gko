import random
import math as Math
import struct
def derivative(n, x):
    return (2 * (n + x)) / (n-1)

def find_correct_pattern(differential, f):
    largess = round(differential)
    x = 0
    while ((largess) >= 4):# (test_highest_order_bit(largess) >= threshold + 1):# and largess > number):
        i = 3
        while i >= 2:
            largess = (largess / i)
            x =  abs(largess)
            i -= 1
    largess = 1 if x == 0 else largess
    return (f*(largess)%2)
# def process_file(input_file, output_file, count):
#     with open(output_file, "wb") as outfile:
#         with open(input_file, "rb") as file:
#             while True:
#                 data = file.read(count)
#                 if not data:
#                     break
#                 string = 0
#                 for i in range(len(data)*8):
#                     t, thr = find_correct_pattern(4, i)
#                     thr = 1 if thr % 2 != 1 else 0
#                     string <<= 1
#                     string += thr
#                 outfile.write(string.to_bytes((len(data) + 7) // 8, byteorder='big'))
def derivative(n, x):
    # Dummy implementation, replace with your actual derivative function
    return ((2 * n) + x) / (n-1)

def flip_bit(bit):
    return 1 if bit == 0 else 0

def process_file(input_file, output_file, count):
    with open(output_file, "wb") as outfile:
        with open(input_file, "rb") as file:
            while True:
                byte = file.read(1)
                if not byte:
                    break
                b = int(byte[0])
                binary = 0
                for i in range(count*8 - 1, -1, -1):
                    # Pass each bit through find_correct_pattern
                    _, thr = find_correct_pattern(b, i)
                    thr = 1 if thr % 2 != 1 else 0
                    binary <<= 1
                    binary = binary + (thr)

                    if (i % 64 == 0):
                        # out = int(binary, 2)
                        while (binary > 0):
                            y = (binary%256)
                            v = chr(y)
                            outfile.write(v.encode())
                            binary >>= 8

def main():
    count = 1000
    differentials = []
    numbers = []
    with open("out3.bin", "wb") as outfile:
        with open("xfile", "rb") as file:
            while True:
                differentials.clear()
                numbers.clear()
                data = file.read(count)
                if not data:
                    break
                y = 0
                x = 0
                for truth in (data):
                    while True:
                        y += 1
                        x = 0
                        for v, a in zip(range(count,0,-1), bin(truth)[2:].zfill(8)):
                            threshold = find_correct_pattern(y, v)
                            # if (threshold%2 != a):
                            x += 1 # counter
                            # else:
                            #     print(v)
                            #     break
                        if x == 8:
                            break
                outfile.write(bytes(chr(y).encode()))
    # process_file("out3.bin", "out4.bin", 1)
    print("Finished")

if __name__ == "__main__":
    main()
