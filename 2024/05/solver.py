from collections import defaultdict, deque

with open("input") as f:
    dlns, ulns = [p.split("\n") for p in f.read().strip().split("\n\n")]
    ups = [list(map(int, up.split(","))) for up in ulns]

    dm = defaultdict(set)
    for fir, sec in [map(int, dep.split("|")) for dep in dlns]:
        dm[fir].add(sec)

    v_ups = [up for up in ups if not any([len(dm[k] & set(up[:i])) > 0 for i, k in enumerate(up)])]
    i_ups = [up for up in ups if any([len(dm[k] & set(up[:i])) > 0 for i, k in enumerate(up)])]

def part1():
    return sum([v[int(len(v) / 2)] for v in v_ups])

def part2(): # lol, i stopped trying code golf here — i'm tired

    # this is just khan's algorithm

    count = 0
    for up in i_ups:
        s = set(up)
        # Put the numbers in the right order

        # Calculate the in-degree of each number in up
        ind = defaultdict(int)
        for u in up:
            for v in dm[u]:
                if v in s:
                    ind[v] += 1

        # Add each number whose in-degree is zero to a queue

        q = deque([u for u in up if ind[u] == 0])

        l = []

        # While the queue is not empty:
        while q:
            e = q.pop()
            l.append(e)
            for n in dm[e]:
                if n in s:
                    ind[n] -= 1
                    if ind[n] == 0:
                        q.append(n)

        count += l[int(len(l) / 2)]
    
    return count

if __name__ == "__main__":
    print(part2())