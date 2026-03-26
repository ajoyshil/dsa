"""
String manipulation
"""
import time

text = "Python"

def padding_extra_character(*args, **kwargs):
    s = args
    kargs = kwargs
    for c in s:
        print(c.ljust(10, '-'))
    # s = s.ljust(10)
    print(kargs)
    return s

print(padding_extra_character(text, "abc", st="ajoy"))


def padding_extra_character(s):
    s = s.rjust(10, '-')
    return s

print(padding_extra_character(text))


def calculate_time(fun):

    def smart_sum(*args):
        start = time.time()
        t = fun(*args)
        end = time.time()
        return start-end
    return smart_sum




@calculate_time
def sum(*args):
    s = 0
    for i in args:
        s+=i
    time.sleep(2)
    return s

print(sum(4,5,8,0,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,))