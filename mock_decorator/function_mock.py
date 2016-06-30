import inspect


class FunctionMock(object):
    """
    This class is a function decorator
    """
    def __init__(self, entity, function_name, mocked_function):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.entity = entity
        self.function_name = function_name
        self.mocked_function = mocked_function

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            old_function = getattr(self.entity, self.function_name)
            setattr(self.entity, self.function_name, self.mocked_function)
            if (inspect.getargspec(old_function)) != inspect.getargspec(self.mocked_function):
                raise TypeError("The function ({}) has not the same signature than the mocked function"
                                .format(self.function_name))
            f(*args, **kwargs)
            setattr(self.entity, self.function_name, old_function)

        return wrapped_f
