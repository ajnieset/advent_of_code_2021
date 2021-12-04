from typing import List


def calculate_gamma_rate(data: list) -> str:
    bit1 = bit2 = bit3 = bit4 = bit5 = bit6 = 0
    bit7 = bit8 = bit9 = bit10 = bit11 = bit12 = 0
    total_inputs = len(data)
    gamma_rate = []
    for number in data:
        bit1 += 1 if number[0] == "1" else 0
        bit2 += 1 if number[1] == "1" else 0
        bit3 += 1 if number[2] == "1" else 0
        bit4 += 1 if number[3] == "1" else 0
        bit5 += 1 if number[4] == "1" else 0
        bit6 += 1 if number[5] == "1" else 0
        bit7 += 1 if number[6] == "1" else 0
        bit8 += 1 if number[7] == "1" else 0
        bit9 += 1 if number[8] == "1" else 0
        bit10 += 1 if number[9] == "1" else 0
        bit11 += 1 if number[10] == "1" else 0
        bit12 += 1 if number[11] == "1" else 0
    
    gamma_rate.append('1' if bit1 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit2 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit3 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit4 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit5 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit6 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit7 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit8 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit9 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit10 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit11 > (total_inputs / 2) else '0')
    gamma_rate.append('1' if bit12 > (total_inputs / 2) else '0')

    return gamma_rate

def calculate_epsilon_rate(gamma_rate: List[str]):
    epsilon_rate = []
    for bit in gamma_rate:
        epsilon_rate.append("1" if bit == "0" else "0")
    
    return epsilon_rate


def main():
    numbers: list = []
    with open("input.csv") as inputs:
        for input in inputs:
            numbers.append(str(input))
    gamma_rate = calculate_gamma_rate(numbers)
    epsilon_rate = calculate_epsilon_rate(gamma_rate)
    gamma_rate_b10 = int("".join(gamma_rate), 2)
    epsilon_rate_b10 = int("".join(epsilon_rate), 2)
    print("Gamma Rate: " + "".join(gamma_rate) + f" | Base 10: {gamma_rate_b10}")
    print("Epsilon Rate: " + "".join(epsilon_rate) + f" | Base 10: {epsilon_rate_b10}")

    total_power = gamma_rate_b10 * epsilon_rate_b10
    print(f"Total Power: {total_power}")

if __name__ == "__main__":
    main()