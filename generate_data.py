import random

filename = "data.txt"
f = open(filename, "w")
for i in range(100000):
    p = random.random()
    boundary = 0.8
    if p < boundary:
        k = 1
    else:
        k = 0
    v = random.random() * 2 - 1
    if k == 1:
        f.write("%d %.2f\n" % (k, v))
    else:
        f.write("0 0.00\n")