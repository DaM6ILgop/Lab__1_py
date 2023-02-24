def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i-1]
            return func(s)
        return wrapper
    return decorator


@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

signal = [1, 2, 3, 4, 5]
plot_signal(signal)