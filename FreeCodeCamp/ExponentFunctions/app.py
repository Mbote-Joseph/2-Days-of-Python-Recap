def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(f"2 to the power of 5 is {raise_to_power(2, 5)}")