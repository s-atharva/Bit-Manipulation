def convert_number_to_binary(number: int) -> str:
    binary_value = str()
    if number == 0:
        return "0"
    while number > 0:
        bit = number % 2
        binary_value += str(bit)
        number = number // 2
    return binary_value


if __name__ == "__main__":
    print(convert_number_to_binary(number=13))
