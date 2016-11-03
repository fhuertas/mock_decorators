class DictMock(object):
    """
    This class is a map decorator
    """

    def __init__(self, entity_dict, key, value, check=False):
        """
        Constructor for map decorator
        :param map: the map to decorate
        :param key: Key to decorate
        :param value: The new value
        :param check: Checks if the value exists (False by default)
        """
        self.dict = entity_dict
        self.key = key
        self.value = value
        self.check = check
        self.has_attribute = key in entity_dict

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            if not self.has_attribute and self.check:
                raise TypeError("The map has not the key: {}".format(self.key))
            old_value = self.dict.get(self.key)
            self.dict[self.key] = self.value
            try:
                result = f(*args, **kwargs)
            finally:
                if self.has_attribute:
                    self.dict[self.key] = old_value
                else:
                    del self.dict[self.key]

            return result

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f
