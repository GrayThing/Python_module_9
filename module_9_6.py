import itertools


def all_variants(text):
    iteration = 1
    while iteration <= len(text):
        generated_combinations = itertools.combinations(text, iteration)
        for combinations in generated_combinations:
            combination = ''
            for symbol in combinations:
                combination += symbol
            yield combination
        iteration += 1
