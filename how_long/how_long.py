from functools import wraps

import pendulum


def timer(function):
    """
    Simple Decorator to measure a function execution time.
    """

    @wraps(function)
    def function_wrapper():
        start = pendulum.now()
        function()
        elapsed_time = pendulum.now() - start
        print(f"Execution Time: {elapsed_time.microseconds} ms.")

    return function_wrapper
