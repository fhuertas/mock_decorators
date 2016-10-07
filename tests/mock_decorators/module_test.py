def function_sum(param_a, param_b):
    return param_a + param_b


a_parameter = 10


class TestClass:
    mocked = False

    def function_echo(self, *args, **kwargs):
        return str(*args)

    def function(self):
        return False

    @classmethod
    def class_function(cls):
        return False
