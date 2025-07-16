def is_ith_beat_set(number, ith_beat_set):
    if number & (1 << ith_beat_set):
        print("True")
    else:
        print("False")


def clear_ith_beat_set(number, ith_beat_set):
    number = number & ~(1 << ith_beat_set)
    print(number)


N = 13
i = 2
is_ith_beat_set(N, i)
clear_ith_beat_set(N, i)
