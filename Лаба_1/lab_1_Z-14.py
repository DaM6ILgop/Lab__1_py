def non_empty(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            result = [x for x in result if x not in ['', None]]
        return result
    return wrapper


@non_empty
def get_data():
    return ['', 'hello', None, 'world', ' ', 'goodbye'] # удаляет пустые строки изи return

result = get_data()
print(result)  # Output: ['hello', 'world', 'goodbye']