def extra_enumerate(iterable):
    total = sum(iterable)
    cum_sum = 0
    for i, elem in enumerate(iterable):
        frac = cum_sum / total
        cum_sum += elem
        yield i, elem, cum_sum, frac


x = [2, 6, 8, 4]

for i, elem, cum, frac in extra_enumerate(x):
    print(f"({elem}, {cum}, {frac:.1f}) ", end="")
    
# Output: (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1.0)