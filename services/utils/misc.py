import sys
from io import StringIO


def suppress_print(func):
    def wrapper(*args, **kwargs):
        # Redirect stdout to a dummy object
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            result = func(*args, **kwargs)
        finally:
            sys.stdout = original_stdout

        return result

    return wrapper
