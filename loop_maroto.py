# TODO: Implemente uma função loop através de ou mais loops que retornem a saída
#   conforme a lista expected.

a = list(range(6))
b = list(range(30))

expected_ = []


def loop():
    first_number = -1
    for second_number in range(30):
        if second_number % 5 == 0:
            first_number += 1
        expected_.append((first_number, second_number))
    return expected_


expected = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (1, 6),
            (1, 7), (1, 8), (1, 9), (2, 10), (2, 11), (2, 12), (2, 13),
            (2, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 19), (4, 20),
            (4, 21), (4, 22), (4, 23), (4, 24), (5, 25), (5, 26), (5, 27),
            (5, 28), (5, 29)]

# print(loop())

assert loop() == expected