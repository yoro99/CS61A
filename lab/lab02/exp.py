def print_sum(x):
    print(x)
    def num_sum(y):
        return print_sum(x+y)
    return num_sum 