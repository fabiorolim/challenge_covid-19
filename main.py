combinations = {}
nitrogenous_base = ('A', 'C', 'G', 'T')


def write_file_genome(new_data):
    with open('novo_genoma_covid.txt', 'w') as file:
        file.write(new_data)


def get_data(file_name):
    with open(file_name) as file:
        return file.read()


def get_combinations():
    # Your code
    pass


def how_many_combinations(data):
    # Your code
    pass


def create_new_genome(data):
    # Your code
    pass


# Tests. Don't touch here!
# SetUP
data = get_data('genoma_covid.txt')
new_data = create_new_genome(data)

# First
expected_1 = {'AA': 0, 'AC': 0, 'AG': 0, 'AT': 0, 'CA': 0, 'CC': 0, 'CG': 0,
              'CT': 0, 'GA': 0, 'GC': 0, 'GG': 0, 'GT': 0, 'TA': 0, 'TC': 0,
              'TG': 0, 'TT': 0}
assert get_combinations() == expected_1

# Second
expected_2 = {'AA': 2880, 'AC': 2023, 'AG': 1742, 'AT': 2308, 'CA': 2084,
              'CC': 888, 'CG': 439, 'CT': 2081, 'GA': 1612, 'GC': 1168,
              'GG': 1093, 'GT': 1990, 'TA': 2377, 'TC': 1413, 'TG': 2589,
              'TT': 3215}
assert how_many_combinations(data) == expected_2

# Third
expected_3 = get_data('novo_genoma_covid.txt')
assert create_new_genome(data) == expected_3

# Fourth
expected_4 = {'AA': 2880, 'AC': 2622, 'AG': 1742, 'AT': 1709, 'CA': 2084,
              'CC': 1547, 'CG': 2451, 'CT': 1422, 'GA': 2181, 'GC': 2258,
              'GG': 1654, 'GT': 1782, 'TA': 1808, 'TC': 1077, 'TG': 2028,
              'TT': 657}
assert how_many_combinations(new_data) == expected_4
