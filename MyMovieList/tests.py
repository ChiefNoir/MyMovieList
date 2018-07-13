from django.test import TestCase

# Create your tests here.
def balding(func):
    def func_wrap(*args, **kwargs):
        return "<b>{val}</b>".format(val = func(*args, **kwargs))
    return func_wrap

@balding
def dotxt():
    return 'ЫЫЫЫ'

@balding
def dottt(text):
    return text


va = dotxt()
print(va)

v = dottt('loh')
print(v)

def fib():
    prev, current = 0, 1
    while 1==1:
        yield current
        prev, current = current, current + prev

lst = list(i for i in fib())[0:15]

for i in 






