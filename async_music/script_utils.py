import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        d1 = time.perf_counter()
        res = func(*args, **kwargs)
        d2 = time.perf_counter()
        wrapper.runtime = d2 - d1

        return res

    return wrapper

