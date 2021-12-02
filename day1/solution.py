from typing import Literal


def check_if_increase(prev: int, depth: int) -> Literal[1, 0]:
    return 1 if prev < depth else 0

def count_measurement_increases(depths) -> int:
    increases = 0
    prev = None

    for depth in depths:
        depth = int(depth)
        if prev is None:
            prev = depth
            continue
        
        increases += check_if_increase(prev, depth)
        prev = depth
    
    return increases

def calculate_sums(depths):
    set1 = set2 = set3 = None
    sums_of_depths = []

    for depth in depths:
        depth = int(depth)
        set3 = set2
        set2 = set1
        set1 = depth
        if None in [set1, set2, set3]:
            continue
        
        depth_sum = set1 + set2 + set3
        sums_of_depths.append(depth_sum)
    
    return sums_of_depths
        


def main():
    with open("input.csv", 'r') as depths:
        summed_depths = calculate_sums(depths)
        
    print(summed_depths)
    increases = count_measurement_increases(summed_depths)

    print(f"Number of increases: {increases}")
    

if __name__ == "__main__":
    main()