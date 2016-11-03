def function_sum(param_a, param_b):
    return param_a + param_b


a_parameter = 10


class TestClass:
    def __init__(self):
        pass

    mocked = False

    def function_echo(self, *args, **kwargs):
        return str(*args)

    def function(self):
        return False

    @classmethod
    def class_function(cls):
        return False

a_dict = {
    'value_a': 22,
    'value_b': None,
}
