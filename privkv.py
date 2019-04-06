import random
import math
import time

def vpp(v, epsilon):
    p = random.random()
    boundary = (1 + v) / 2
    vp = 0
    if p < boundary:
        vp = 1
    else:
        vp = -1
    p = random.random()
    boundary = math.e ** epsilon / (1 + math.e ** epsilon)
    if p > boundary:
        vp = -vp
    return vp


def lpp(k_v, epsilon1, epsilon2):
    k = k_v[0]
    v = k_v[1]
    kp = 0
    vp = 0
    if k == 1:
        vp = vpp(v, epsilon2)
        p = random.random()
        boundary = math.e ** epsilon1 / (1 + math.e ** epsilon1)
        if p < boundary:
            kp = 1
        else:
            kp = 0
            vp = 0
    else:
        v = random.random() * 2 - 1
        vp = vpp(v, epsilon2)
        p = random.random()
        boundary = math.e ** epsilon1 / (1 + math.e ** epsilon1)
        if p < boundary:
            kp = 0
            vp = 0
        else:
            kp = 1
    return kp, vp

def priv_kv(all_kv, epsilon1, epsilon2):
    all_kvp = [lpp(kv, epsilon1, epsilon2) for kv in all_kv]
    total = 0
    have = 0
    pos = 0
    neg = 0
    for kv in all_kvp:
        if kv[0] == 1:
            have += 1
        total += 1
        if kv[1] == 1:
            pos += 1
        if kv[1] == -1:
            neg += 1
    f = have / total
    p = math.e ** epsilon1 / (1 + math.e ** epsilon1)
    f = (p - 1 + f) / (2 * p - 1)
    n = pos + neg
    p = math.e ** epsilon2 / (1 + math.e ** epsilon2)
    n1 = (p - 1) / (2 * p - 1) * n + pos / (2 * p - 1)
    n2 = (p - 1) / (2 * p - 1) * n + neg / (2 * p - 1)
    if n1 < 0:
        n1 = 0
    elif n1 > n:
        n1 = n
    if n2 < 0:
        n2 = 0
    elif n2 > n:
        n2 = n
    m = (n1 - n2) / n
    return f, m

if __name__ == "__main__":
    filename = "data.txt"
    seed = 10
    random.seed(seed)
    f = open(filename, "r")
    data = f.readlines()
    data = [(int(d.split()[0]), float(d.split()[1])) for d in data]
    f, m = priv_kv(data, 100, 100)
    print(f, m)
    total = 0
    have = 0
    value = 0
    for d in data:
        if d[0] == 1:
            have += 1
            value += d[1]
        total += 1
    print(have / total, value / have)
        