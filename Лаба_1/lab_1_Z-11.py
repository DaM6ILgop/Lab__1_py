def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

for x in frange(1, 7, 0.1):
    print(x)