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

def main():
    with open("input.csv", 'r') as depths:
        increases = count_measurement_increases(depths)

    print(f"Number of increases: {increases}")
    


if __name__ == "__main__":
    main()