with open("input") as f:
    ls = f.read().strip().split("\n")
    ns = [list(map(int, l.split())) for l in ls]
    
def is_valid(nss):
    if (nss != sorted(nss) and nss != sorted(nss, reverse=True)):
        return False
    return all([1 <= abs(a-b) <= 3 for a, b in zip(nss[:-1], nss[1:])])

print(len(list(filter(is_valid, ns))))
print(len(list(filter(lambda nss: (any([is_valid (nss[:i] + nss[i + 1:]) for i in range(len(nss))])), ns))))
