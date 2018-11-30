def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg):
    print(arg)


def print_none():
    print('No args.')


print_two("Hello", "World")
print_two_again("Hello", "World")
print_one("Hello")
print_none()
