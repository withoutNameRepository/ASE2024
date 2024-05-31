import random


# This function generates a list of random integers. The output of this function will be passed to the generated code
# by the large language model and the model solution.
def input_generator(l, random_seed):
    random.seed(random_seed)
    x = max(int(l[0]), int(l[1]), int(l[2])) + 2
    result = []
    for _ in range(2):
        random_selection = random.randint(0, 1)
        if random_selection:
            result += random.choices(range(1, 2000), k=x)
        else:
            result += random.sample(range(1, 2000), x)

    return result
