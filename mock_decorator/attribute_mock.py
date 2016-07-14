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
            except AttributeError:
                old_value = None

            setattr(self.entity, self.attribute_name, self.value)
            f(*args, **kwargs)
            if old_value is None:
                delattr(self.entity, self.attribute_name)
            else:
                setattr(self.entity, self.attribute_name, old_value)

        return wrapped_f


class ObjectMock(object):
    pass
