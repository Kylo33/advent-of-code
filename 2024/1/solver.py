from collections import Counter as C

with open("input") as f:
    ls = [l.split() for l in f.read().strip().split("\n")]
    f = sorted([int(l[0]) for l in ls])
    s = sorted([int(l[1]) for l in ls])

cs = C(s)
print(sum([abs(a - b) for a, b in zip(f,s)]))
print(sum([a * cs[a] for a in f]))
