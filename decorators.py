
def decorator(func):
    def decorated():
        print('함수시작!')
        func()
        print('함수 끝!')
    return decorated


@decorator
def hello_world():
    print('Hello World!')

hello_world()


def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            raise ValueError('Input must be positive value')
    return decorated


@check_integer
def rect_area(width, height):
    return width * height

@check_integer
def tri_area(width, height):
    return width * height/2

r_area = rect_area(-10, 10)
print(r_area)

t_area = tri_area(10, 10)
print(t_area)