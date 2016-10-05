from mock_decorators import utils


class FunctionMock(object):
    """
    This class is a function decorator
    """

    def __init__(self, entity, function_name, mocked_function, check_signature=True):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.entity = entity
        self.function_name = function_name
        self.mocked_function = mocked_function
        self.check_signature = check_signature

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            try:
                old_function = getattr(self.entity, self.function_name)
                setattr(self.entity, self.function_name, self.mocked_function)
            except AttributeError:
                old_function = None

            if self.check_signature:
                utils.test_signature(old_function, self.mocked_function)
            try:
                result = f(*args, **kwargs)
            finally:
                setattr(self.entity, self.function_name, old_function)
            return result

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f


class FunctionMockResult(object):
    """
    This class is a function decorator
    """

    def __init__(self, entity, function_name, result, checkExists=True):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.entity = entity
        self.function_name = function_name
        self.result = result
        self.checkExists = checkExists

    def blank_fn(self, *args, **kwargs):
        return self.result

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def test_wrapped_f(*args, **kwargs):
            old_function = getattr(self.entity, self.function_name)
            if self.checkExists and old_function is None:
                raise TypeError("the function don't exist")
            setattr(self.entity, self.function_name, self.blank_fn)
            try:
                result = f(*args, **kwargs)
            finally:
                # Needed although the execution has failed
                setattr(self.entity, self.function_name, old_function)
            return result

        # wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return test_wrapped_f


class FunctionMockChangeResult(object):
    """
    This class is a function decorator
    """

    def __init__(self, entity, function_name, fn):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.entity = entity
        self.function_name = function_name
        self.fn = fn
        self.old_function = getattr(self.entity, self.function_name)

    def my_call(self, *args, **kwargs):
        result = self.old_function(*args, **kwargs)
        return self.fn(result)

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            # old_function = getattr(self.entity, self.function_name)
            setattr(self.entity, self.function_name, self.my_call)
            try:

                f(*args, **kwargs)
            finally:
                # Needed although the execution has failed
                setattr(self.entity, self.function_name, self.old_function)

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f
