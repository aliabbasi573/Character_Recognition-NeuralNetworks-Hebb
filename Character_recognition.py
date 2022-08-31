"""
َAli Abbasi
Computational Intelligence Project
Character recognition Function with Hebbian Learning Algorithm
"""

import itertools
import threading
import time
import sys


# Initialize to w & b:
w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
b = 0


def Hebb(x, T):
    y = T
    global w1_New, w2_New, w3_New, w4_New, w5_New, w6_New, w7_New, w8_New, w9_New, w10_New, w11_New, w12_New, w13_New, w14_New, w15_New ,w16_New, w17_New, w18_New, w19_New, w20_New ,w21_New, w22_New, w23_New, w24_New, w25_New
    global w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, w19, w20, w21, w22, w23, w24, w25
    global b, b_New
    w1_New = w1 + int(x[0]) * int(y)
    w2_New = w2 + int(x[1]) * int(y)
    w3_New = w3 + int(x[2]) * int(y)
    w4_New = w4 + int(x[3]) * int(y)
    w5_New = w5 + int(x[4]) * int(y)
    w6_New = w6 + int(x[5]) * int(y)
    w7_New = w7 + int(x[6]) * int(y)
    w8_New = w8 + int(x[7]) * int(y)
    w9_New = w9 + int(x[8]) * int(y)
    w10_New = w10 + int(x[9]) * int(y)
    w11_New = w11 + int(x[10]) * int(y)
    w12_New = w12 + int(x[11]) * int(y)
    w13_New = w13 + int(x[12]) * int(y)
    w14_New = w14 + int(x[13]) * int(y)
    w15_New = w15 + int(x[14]) * int(y)
    w16_New = w16 + int(x[15]) * int(y)
    w17_New = w17 + int(x[16]) * int(y)
    w18_New = w18 + int(x[17]) * int(y)
    w19_New = w19 + int(x[18]) * int(y)
    w20_New = w20 + int(x[19]) * int(y)
    w21_New = w21 + int(x[20]) * int(y)
    w22_New = w22 + int(x[21]) * int(y)
    w23_New = w23 + int(x[22]) * int(y)
    w24_New = w24 + int(x[23]) * int(y)
    w25_New = w25 + int(x[24]) * int(y)
    b_New = b + int(y)

    return w1_New, w2_New, w3_New, w4_New, w5_New, w6_New, w7_New, w8_New, w9_New, w10_New, w11_New, w12_New, w13_New, w14_New, w15_New ,w16_New, w17_New, w18_New, w19_New, w20_New ,w21_New, w22_New, w23_New, w24_New, w25_New

    w1 = w1_New
    w2 = w2_New
    w3 = w3_New
    w4 = w4_New
    w5 = w5_New
    w6 = w6_New
    w7 = w7_New
    w8 = w8_New
    w9 = w9_New
    w10 = w10_New
    w11 = w11_New
    w12 = w12_New
    w13 = w13_New
    w14 = w14_New
    w15 = w15_New
    w16 = w16_New
    w17 = w17_New
    w18 = w18_New
    w19 = w19_New
    w20 = w20_New
    w21 = w21_New
    w22 = w22_New
    w23 = w23_New
    w24 = w24_New
    w25 = w25_New
    b = b_New


"""
giving the training input by reading the dataset.txt File:
   in each line:
      first 25 numbers are making the matrix
      And
      the last number is our target for that input
"""
#  this function will turn our string input to list
def Convert(string):
    li = list(string.split(","))
    return li


#  reading file line by line
with open("dataset.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
        list_of_inputs = Convert(line)
        x = list_of_inputs[0:25]  # Learning input that include 25 X values
        T = list_of_inputs[25]  # Value of Our Target
        # Target -1 for (O) data & 1 for (X)
        Hebb(x, T)


#  Testing system:

test1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
print("[1 1 1 1 1]")
print("[1 0 0 0 1]")
print("[1 0 0 0 1]")
print("[1 0 0 0 1]")
print("[1 1 1 1 1]")

print("Wait a Sec Pleas...")

# Loading icon:
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True


# Pattern Classification
y_NI = b_New + (w1_New * int(test1[0])) + (w2_New * int(test1[1])) + (w3_New * int(test1[2])) + (w4_New * int(test1[3])) + (w5_New * int(test1[4])) + (w6_New * int(test1[5])) + (w7_New * int(test1[6])) + (w8_New * int(test1[7])) + (w9_New * int(test1[8])) + (w10_New * int(test1[9])) + (w11_New * int(test1[10])) + (w12_New * int(test1[11])) + (w13_New * int(test1[12])) + (w14_New * int(test1[13])) + (w15_New * int(test1[14])) + (w16_New * int(test1[15])) + (w17_New * int(test1[16])) + (w18_New * int(test1[17])) + (w19_New * int(test1[18])) + (w20_New * int(test1[19])) + (w21_New * int(test1[20])) + (w22_New * int(test1[21])) + (w23_New * int(test1[22])) + (w24_New * int(test1[23])) + (w25_New * int(test1[24]))
if y_NI >= 0:
    F_y = 1
else:
    F_y = -1

if F_y == 1:
    print()
    print("----┊┊----")
    print("    ┊┊    ")
    print("    \/    ")
    print("This shape is X")
elif F_y == -1:
    print()
    print("----┊┊----")
    print("    ┊┊    ")
    print("    \/    ")
    print("This shape is O")


'''
Other shape for test:
test1 = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
print("Lets Try this")
print("[1 0 0 0 1]")
print("[0 1 0 1 0]")
print("[0 0 1 0 0]")
print("[0 1 0 1 0]")
print("[1 0 0 0 1]")

'''

