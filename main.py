nitrogenous_base = ('A', 'C', 'G', 'T')


def write_file_genome(new_data):
    with open('novo_genoma_covid.txt', 'w') as file:
        file.write(new_data)


def get_data(file_name):
    with open(file_name) as file:
        return file.read()


def get_combinations():
    combinations = {}
    for n in nitrogenous_base:
        for n_ in nitrogenous_base:
            combinations[n + n_] = 0
    return combinations


def how_many_combinations(data):
    combinations = get_combinations()
    combinations_ = {}
    for n in combinations.keys():
        combinations_[n] = data.count(n)
    return combinations_


def search_key(d, value):
    for k in d.keys():
        if d[k] == value:
            return k
    raise LookupError()


def get_lowest():
    data = get_data('genoma_covid.txt')
    combinations = how_many_combinations(data)
    low = sorted(combinations.values())[-1]
    return search_key(combinations, low)


def get_highwest():
    data = get_data('genoma_covid.txt')
    combinations = how_many_combinations(data)
    high = sorted(combinations.values())[0]
    return search_key(combinations, high)


def create_new_genome(data):
    low, high = get_lowest(), get_highwest()
    new_data = data.replace(low, high)
    return new_data


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
expected_2 = {'AA': 2144, 'AC': 1999, 'AG': 1711, 'AT': 2276, 'CA': 2053,
              'CC': 770, 'CG': 427, 'CT': 2049, 'GA': 1586, 'GC': 1153,
              'GG': 958, 'GT': 1962, 'TA': 2338, 'TC': 1407, 'TG': 2549,
              'TT': 2439}
assert how_many_combinations(data) == expected_2

# Third
expected_3 = get_data('novo_genoma_covid.txt')
assert create_new_genome(data) == expected_3

# Fourth
expected_4 = {'AA': 2144, 'AC': 2700, 'AG': 1711, 'AT': 1575, 'CA': 2053,
              'CC': 1202, 'CG': 2976, 'CT': 1566, 'GA': 1586, 'GC': 1685,
              'GG': 958, 'GT': 1430, 'TA': 2338, 'TC': 2207, 'TG': 0,
              'TT': 1813}

assert how_many_combinations(new_data) == expected_4
