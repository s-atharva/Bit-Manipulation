def is_ith_beat_set(Number, ith_beat_set):
    if Number & (1 << ith_beat_set):
        print("True")
    else:
        print("False")


N = 13
i = 2
is_ith_beat_set(N, i)
