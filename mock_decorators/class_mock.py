import sys


class ClassMock(object):
    """
    This class is a object mock decorator
    """

    def __init__(self, old_class_name, new_class):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """

        self.old_class_name = old_class_name
        self.new_class = new_class

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """

        def wrapped_f(*args, **kwargs):
            old_class = self.old_class_name
            old_methods = {}
            methods = dir(self.new_class)
            old_methods.update({"__init__": getattr(old_class, "__init__", None)})
            setattr(old_class, "__init__", getattr(self.new_class, "__init__"))
            for method_name in methods:
                if not method_name.startswith("__"):
                    old_method = getattr(old_class, method_name, None)
                    new_method = getattr(self.new_class, method_name)

                    # Saving old methods
                    old_methods.update({method_name: old_method})
                    # Setting the new methods
                    setattr(old_class, method_name, new_method)
            try:
                result = f(*args, **kwargs)
            finally:
                # Restore methods changed
                for method_name in old_methods:
                    setattr(old_class, method_name, old_methods.get(method_name))
            return result

        wrapped_f.__name__ = '{}_{}'.format(f.__name__, wrapped_f.__name__)

        return wrapped_f
