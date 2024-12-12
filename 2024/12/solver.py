from typing import Set, Tuple, Dict, List
from collections import defaultdict


def main(filename: str):
    with open(filename) as f:
        farm = [list(line) for line in f.read().strip().split("\n")]
        region_id_dict: Dict[int, Set[Tuple[int, int]]] = defaultdict(set)
        visited = set()

        # Add each region to region_id_dict with an ID
        id = 0
        for y, line in enumerate(farm):
            for x, plant in enumerate(line):
                if (x, y) in visited:
                    continue
                visited.add((x, y,))

                region_id_dict[id].add((x, y,))
                deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
                adjacent_plots = [(x + dx, y + dy) for dx, dy in deltas if 0 <= y + dy < len(farm) and 0 <= x + dx < len(farm[0])]
                for ax, ay in adjacent_plots:
                    if farm[ay][ax] == plant:
                        visited.add((x, y,))
                        region_id_dict[id].add((x, y,))
                
                id += 1
        print(region_id_dict)


# def get_region(x: int, y: int, plant: str, visited: Set[Tuple[int, int]]):



if __name__ == "__main__":
    main("test_input")



        # plants: Dict[str, Set[Tuple[int, int]]] = defaultdict(list)
        # for y, line in enumerate(farm):
        #     for x, plant in enumerate(line):
        #         plants[plant].add((x, y,))