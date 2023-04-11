from hello_world import say_hello
from calculator import calculate
from even_numbers import generate_list
from even_numbers import get_evens


if __name__ == '__main__':
    say_hello()
    print(calculate(17, 17, 'mul'))
    numbers_list = generate_list()
    print(numbers_list)
    print(get_evens(numbers_list))
