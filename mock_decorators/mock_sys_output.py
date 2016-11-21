import contextlib
import sys


class MockSysOutput(object):
    @classmethod
    @contextlib.contextmanager
    def _stdout_redirect(cls, where):
        sys.stdout = where
        try:
            where.seek(0)
            where.truncate()
            yield where
        finally:
            sys.stdout = sys.__stdout__
            where.seek(0)

    def __init__(self, text_io_wrapper):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """

        # print(isinstance(text_io_wrapper))
        self.test_io_wrapper = text_io_wrapper

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            with MockSysOutput._stdout_redirect(self.test_io_wrapper):
                result = f(*args, **kwargs)
            return result

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f
