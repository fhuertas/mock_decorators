class AttributeMock(object):
    """
    This class is a attributes decorator
    """

    def __init__(self, entity, attribute_name, value):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.entity = entity
        self.attribute_name = attribute_name
        self.value = value

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            try:
                old_value = getattr(self.entity, self.attribute_name)
                has_value = True
            except AttributeError:
                old_value = None
                has_value = False

            setattr(self.entity, self.attribute_name, self.value)
            try:
                result = f(*args, **kwargs)
            finally:
                if has_value:
                    setattr(self.entity, self.attribute_name, old_value)
                else:
                    delattr(self.entity, self.attribute_name)

            return result

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f
