import unittest
from mock_decorators.function_mock import FunctionMock
from tests.mock_decorators import module_test


class TestFunctionMock(unittest.TestCase):
    p1 = 10
    p2 = 2

    def test_function_mock_correct(self):
        def function_mocked(param_a, param_b):
            return param_a - param_b

        @FunctionMock(entity=module_test, function_name='function_sum', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            return module_test.function_sum(self.p1, self.p2)

        result = inner_test()
        expected = function_mocked(self.p1, self.p2)

        self.assertEqual(result, expected, "The FunctionMock has failed")

    def test_function_mock_bad_signature(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_sum', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            self.assertRaisesRegex(TypeError, "signature", module_test.function_sum, self.p1, self.p2)

    def test_function_mock_bad_signature_no_checked(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_sum', mocked_function=function_mocked,
                      check_signature=False)
        def inner_test():
            return module_test.function_sum(self.p1, self.p2)

        result = inner_test()
        expected = function_mocked(self.p1, self.p2)

        self.assertEqual(result, expected, "The FunctionMock has failed")

    def test_function_mock_no_exists(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_summ', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            pass

        self.assertRaises(TypeError, 'unsupported callable', inner_test)
