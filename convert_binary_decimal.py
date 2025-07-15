binary_value = "1101"
decimal_number = 0
length = len(binary_value)
power_of_two = 1
# length is 4
# decimal_number 1*2^0 + 0+2^1 + 1*2^2 + 1*2^3 = 13
# (start, end, step)
for i in range(length - 1, -1, -1):
    if binary_value[i] == "1":
        decimal_number += power_of_two
    power_of_two *= 2
print(decimal_number)
