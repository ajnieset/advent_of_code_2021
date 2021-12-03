def calculate_movement(direction: str, units: int):
    if direction == 'up':
        return -abs(units)
    else:
        return units

def main():
    formatted_data = []
    horizontal = depth = aim = 0
    with open("input.csv") as inputs:
        for input in inputs:
            formatted_data.append(input.split())
    
    for direction, unit in formatted_data:
        unit = int(unit)
        if direction == 'forward':
            horizontal += calculate_movement(direction, unit)
            depth += unit * aim
        else:
            aim += calculate_movement(direction, unit)
    
    total = depth * horizontal
    print(f"depth: {depth}")
    print(f"horizontal: {horizontal}")
    print(f"combined: {total}")

if __name__ == "__main__":
    main()