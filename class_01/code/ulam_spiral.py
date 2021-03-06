"""
Tomas Meszaros

Visualization of Ulam spiral and variants.
"""

import math
import sys

from bmplib import BMPImage
from pprint import pprint as pp


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# img side in pixels
IMG_SIDE = 255

# amount of numbers
MAX_NUM = IMG_SIDE*IMG_SIDE

if MAX_NUM % 2 == 0:
    print("sqrt(MAX_NUM) has to be odd")
    sys.exit(1)

## prepare the matrix that we will fill later
nums = list(range(1, MAX_NUM + 1))
matrix = []
WIDTH = int(math.sqrt(MAX_NUM))
for i in range(WIDTH):
    matrix.append([None] * WIDTH)

## Fill the matrix with number is the "spiral" way
start = (math.floor(WIDTH / 2), math.floor(WIDTH / 2))
cnt = 0
cur_i = start[0]
cur_j = start[1]
loop = 1

# mid point
matrix[cur_i][cur_j] = nums[cnt]
cnt += 1

# one to right
cur_j += 1
matrix[cur_i][cur_j] = nums[cnt]
cnt += 1

# starting from about the middle of the matrix and making progressively bigger
# loops and filling numbers
# - could refactor this but I think the idea is more clear this way
while loop < math.ceil(WIDTH / 2):
    # up
    for i in range(cur_i-1, cur_i-1-(loop*2-1), -1):
        matrix[i][cur_j] = nums[cnt]
        cnt += 1
    cur_i = i

    # left
    for j in range(cur_j-1, cur_j-1-(loop*2-1)-1, -1):
        matrix[cur_i][j] = nums[cnt]
        cnt += 1
    cur_j = j

    # down
    for i in range(cur_i+1, cur_i+1+(loop*2-1)+1):
        matrix[i][cur_j] = nums[cnt]
        cnt += 1
    cur_i = i

    # right
    for j in range(cur_j+1, cur_j + ((loop+1)*2-1)+1):
        if cnt == len(nums):
            # we are finished, we dont want to start another loop
            continue
        matrix[cur_i][j] = nums[cnt]
        cnt += 1
    cur_j = j

    loop += 1
#pp(matrix)


## Filter number from matrix and make images
img_primes = BMPImage(width=IMG_SIDE, height=IMG_SIDE, bg="white")
img_div_by_4 = BMPImage(width=IMG_SIDE, height=IMG_SIDE, bg="white")
img_div_by_5 = BMPImage(width=IMG_SIDE, height=IMG_SIDE, bg="white")
img_div_by_8 = BMPImage(width=IMG_SIDE, height=IMG_SIDE, bg="white")

for i in range(int(img_primes.get_width())):
    for j in range(img_primes.get_height()):
        if is_prime(matrix[i][j]):
            img_primes.put_pixel(i, j, (0, 0, 0))
        if matrix[i][j] % 4 == 0:
            img_div_by_4.put_pixel(i, j, (0, 0, 0))
        if matrix[i][j] % 5 == 0:
            img_div_by_5.put_pixel(i, j, (0, 0, 0))
        if matrix[i][j] % 8 == 0:
            img_div_by_8.put_pixel(i, j, (0, 0, 0))

img_primes.save("img/ulam_spiral_primes.bmp")
img_div_by_4.save("img/ulam_spiral_div_by_4.bmp")
img_div_by_5.save("img/ulam_spiral_div_by_5.bmp")
img_div_by_8.save("img/ulam_spiral_div_by_8.bmp")
