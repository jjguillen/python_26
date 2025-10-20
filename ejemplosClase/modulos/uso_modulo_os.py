from os import getcwd, mkdir
from statistics import mean
from math import *
from random import random, randint

print("Current Working Directory:", getcwd())

print("Create folder trash:", "mkdir trash")
#mkdir('trash')

data = [10, 20, 30, 40, 50]
print("Mean of data:", mean(data))


print("Square root of 16:", sqrt(16))
print(pi)
print(pow(2, 5))
print("Ceiling of 4.3:", ceil(4.3))
print("Floor of 4.7:", floor(4.7))

print("Random float between 0 and 1:", random())
print("Random integer between 1 and 100:", randint(1, 100))


