# This didn't work, but I did realise that the pattern repeats. Then realised that as the dimensions are
# prime numbers the pattern must repeat after num_x * n_num iterations (because of modulus rules) so the max iterations 
# will be 101 * 103 = 11402. 

# Hence dont' need to optimise for running very large numbers of iterations

# Also the theory that the christmas tree will appear all in one quadrant appears to be false. this is backed up by 
# the previous years puzzle which appeared to be tracing a path rather than a densly populated picture.

import re
import time
from PIL import Image

path = "./day14/day14_input.txt"
num_x = 101
num_y = 103

# path = "./day14/day14_test.txt"
# num_x = 11
# num_y = 7

with open(path) as file:
    lines = file.read().splitlines()

# print(lines)

num_iter = 100000000

regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"


pxs = []
pys = []
vxs = []
vys = []

for l_ind, l in enumerate(lines):
    tup = re.findall(regex, l)[0]
    pxs.append(int(tup[0]))
    pys.append(int(tup[1]))
    vxs.append(int(tup[2]))
    vys.append(int(tup[3]))


def in_quad(px,py):
    if px in range(0, num_x // 2) and py in range(0, num_y //2 ): return 1
    if px in range(num_x - num_x // 2 , num_x) and py in range(0, num_y //2 ): return 2
    if px in range(0, num_x //2) and py in range (num_y - num_y //2, num_y ): return 3
    if px in range(num_x - num_x // 2 , num_x) and py in range (num_y - num_y //2, num_y ): return 4

def print_grid():
    img = Image.new('RGB', (num_x, num_y), 'white')
    pix = img.load()
    for x_ind in range(len(pxs)):
        ix = (pxs[x_ind] + iter * vxs[x_ind]) % num_x
        iy = (pys[x_ind] + iter * vys[x_ind]) % num_y
        pix[ix, iy] = (0,255,0)
    img.show()


tic = time.time()

for iter in range(num_iter):
    
    # if not iter % 1000000: 
    #     toc = time.time()
    #     print(f"iter: {iter}, time: {toc - tic}")
    #     tic = toc
    
    ix = (pxs[0] + iter * vxs[0]) % num_x
    iy = (pys[0] + iter * vys[0]) % num_y
    quad = in_quad(ix,iy)

    match = True
    for x_ind in range(1,5):
        ix = (pxs[x_ind] + iter * vxs[x_ind]) % num_x
        iy = (pys[x_ind] + iter * vys[x_ind]) % num_y
        if quad != in_quad(ix,iy): 
            match = False                
            break
    if match and quad == 1: 
        print(f"Success: iter: {iter}, target: {quad}")     
        print_grid()
    
    # for target in range(1,5):
        # x_ind = 0
        # loop = True
        # while x_ind < len(pxs) and loop == True:
        #     ix = (pxs[x_ind] + iter * vxs[x_ind]) % num_x
        #     iy = (pys[x_ind] + iter * vys[x_ind]) % num_y
        #     if in_quad(ix, iy) != target:
        #         loop = False 
        #     if x_ind == 6:
        #         print(f"Success: iter: {iter}, target: {target}")
        #         print_grid()
        #     x_ind += 1









