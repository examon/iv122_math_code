"""
Tomas Meszaros

Module with timing utilities.
"""

import time


def timeit(message: str):
    """
    Named decorator "@timeit". Times execution of the decorated function
    in milliseconds. Prints the @message + measured time.
    Note: the is some overhead from the function calls so the measured time is
    not strictly 100% correct (but is good enough).
    """
    def timer(func):
        """ Default decorator @timer.
        """
        def inner(*args, **kwargs):
            """ This is where the measurement happens.
            """
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            total_milliseconds = (end - start) * 1000
            print("%s %.1f ms" % (message, total_milliseconds))
            return result
        return inner
    return timer
