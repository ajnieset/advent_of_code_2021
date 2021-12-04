def calculate_oxygen_rating(ratings: list):
    for i in range(12):
        mid = len(ratings) / 2
        bit_count = 0
        for rating in ratings:
            bit_count += 1 if rating[i] == "1" else 0
        most_common = "1" if bit_count >= mid else "0"

        if len(ratings) > 1:
            new_ratings = list(filter(lambda x: x[i] == most_common, ratings))
            if len(new_ratings) != 0:
                ratings = new_ratings
        else:
            break
    return int(ratings[0], 2)

def calculate_c02_rating(ratings: list):
    for i in range(12):
        mid = len(ratings) / 2
        bit_count = 0
        for rating in ratings:
            bit_count += 1 if rating[i] == "1" else 0
        least_common = "0" if bit_count >= mid else "1"

        if len(ratings) > 1:
            new_ratings = list(filter(lambda x: x[i] == least_common, ratings))
            if len(new_ratings) != 0:
                ratings = new_ratings
        else:
            break
    return int(ratings[0], 2)

def main():
    numbers: list = []
    with open("input.csv") as inputs:
        for input in inputs:
            numbers.append(str(input).rstrip())
    oxygen_rating = calculate_oxygen_rating(numbers)
    co2_rating = calculate_c02_rating(numbers)
    print(f"Oxygen Rating: {oxygen_rating}")
    print(f"CO2 Rating: {co2_rating}")
    total_power = oxygen_rating * co2_rating
    print(f"Total Power: {total_power}")

if __name__ == "__main__":
    main()