import sys
import unittest
from mock_decorators.function_mock import FunctionMock
from mock_decorators.function_mock import FunctionMockResult
from mock_decorators.function_mock import FunctionMockChangeResult
from mock_decorators.function_mock import FunctionMockCheckCall
from tests.mock_decorators import module_test
from tests.mock_decorators.module_test import TestClass


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

        result_no_mocked = module_test.function_sum(self.p1, self.p2)
        result_mocked = inner_test()
        expected_mocked = self.p1 - self.p2
        expected_no_mocked = self.p1 + self.p2

        self.assertEqual(result_mocked, expected_mocked, "The FunctionMock has failed")
        self.assertEqual(result_no_mocked, expected_no_mocked, "The FunctionMock has failed")

    def test_function_mock_correct_a_class(self):
        result_of_the_function_mock = "mock mock mock"

        def function_mocked(self, *args, **kwargs):
            return result_of_the_function_mock

        test_class = TestClass()

        @FunctionMock(entity=TestClass, function_name='function_echo', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            return test_class.function_echo("No echo")

        result_mocked = inner_test()

        self.assertEqual(result_mocked, result_of_the_function_mock, "The FunctionMock has failed")
        self.assertNotEqual(test_class.function_echo("No echo"),
                            result_of_the_function_mock, "The FunctionMock has failed")

    def test_function_mock_bad_signature(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_sum', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            module_test.function_sum(self.p1, self.p2)

        if sys.version_info < (3, 4):
            self.assertRaisesRegexp(TypeError, "signature", inner_test)
        else:
            self.assertRaisesRegex(TypeError, "signature", inner_test)

    def test_function_mock_not_exists(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_suma', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            module_test.function_suma(self.p1, self.p2)

        if sys.version_info < (3, 4):
            self.assertRaises(TypeError, inner_test)
        else:
            self.assertRaisesRegex(TypeError, "unsupported callable", inner_test)

    def test_function_mock_bad_signature_no_checked(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_sum', mocked_function=function_mocked,
                      check_signature=False)
        def inner_test():
            return module_test.function_sum(self.p1, self.p2)

        result_no_mocked = module_test.function_sum(self.p1, self.p2)
        result_mocked = inner_test()
        expected_mocked = self.p1 - self.p2
        expected_no_mocked = self.p1 + self.p2

        self.assertEqual(result_mocked, expected_mocked, "The FunctionMock has failed")
        self.assertEqual(result_no_mocked, expected_no_mocked, "The FunctionMock has failed")

    def test_function_mock_no_exists(self):
        def function_mocked(param, param_b):
            return param - param_b

        @FunctionMock(entity=module_test, function_name='function_summ', mocked_function=function_mocked,
                      check_signature=True)
        def inner_test():
            pass

        if sys.version_info < (3, 4):
            self.assertRaises(TypeError, inner_test)
        else:
            self.assertRaisesRegex(TypeError, 'unsupported callable', inner_test)


class TestFunctionMockResult(unittest.TestCase):
    def test_function_mock_result_correct(self):
        result_returned = -21231

        @FunctionMockResult(module_test, 'function_sum', result_returned, True)
        def inner_test():
            return module_test.function_sum(1, 1)

        result_value_mocked = inner_test()

        self.assertTrue(result_value_mocked, result_returned)

    def test_function_mock_result_correct_no_exist(self):
        result_returned = -21231

        @FunctionMockResult(module_test, 'function_suma', result_returned, True)
        def inner_test():
            return module_test.function_sum(1, 1)

        if sys.version_info < (3, 3):
            self.assertRaisesRegexp(TypeError, "the function don't exist", inner_test)
        else:
            self.assertRaisesRegex(TypeError, "the function don't exist", inner_test)

    def test_function_mock_result_correct_no_exist_no_checked(self):
        result_returned = -21231

        @FunctionMockResult(module_test, 'function_suma', result_returned, False)
        def inner_test():
            return module_test.function_sum(1, 1)

        result_value_mocked = inner_test()

        self.assertTrue(result_value_mocked, result_returned)

    def test_function_mock_no_function(self):
        result_returned = -21231
        invalid_function_name = 'invalid_function'

        def inner_test():
            @FunctionMockResult(module_test, invalid_function_name, result_returned)
            def call_test():
                module_test.function_sum(1, 1)

            call_test()

        if sys.version_info < (3, 0):
            self.assertRaisesRegexp(AttributeError, invalid_function_name, inner_test)
        else:
            self.assertRaisesRegex(AttributeError, invalid_function_name, inner_test)


class TestFunctionMockChangeResult(unittest.TestCase):
    first_parameter = 500
    second_parameter = 10

    def test_function_mock_change_result_correct(self):
        def function_change(value):
            return value + 2

        @FunctionMockChangeResult(module_test, 'function_sum', function_change)
        def inner_test():
            return module_test.function_sum(self.first_parameter, self.second_parameter)

        result_no_mocked = module_test.function_sum(self.first_parameter, self.second_parameter)
        result_mocked = inner_test()
        expected_mocked = self.first_parameter + self.second_parameter + 2
        expected_no_mocked = self.first_parameter + self.second_parameter

        self.assertEqual(result_mocked, expected_mocked, "The FunctionMock has failed")
        self.assertEqual(result_no_mocked, expected_no_mocked, "The FunctionMock has failed")

    def test_function_mock_change_result_incorrect_function(self):
        def function_change():
            return 2

        @FunctionMockChangeResult(module_test, 'function_sum', function_change)
        def inner_test():
            if sys.version_info < (3, 0):
                self.assertRaisesRegexp(TypeError, 'takes no arguments',
                                        module_test.function_sum, self.first_parameter, self.second_parameter)
            else:
                self.assertRaisesRegex(TypeError, 'positional arguments but 1 was given',
                                       module_test.function_sum, self.first_parameter, self.second_parameter)

        inner_test()

    def test_function_mock_change_result_no_function(self):
        def function_change(value):
            return value + 2

        invalid_function_name = 'invalid_function'

        def inner_test():
            @FunctionMockChangeResult(module_test, invalid_function_name, function_change)
            def call_test():
                module_test.function_sum(1, 1)

            call_test()

        if sys.version_info < (3, 0):
            self.assertRaisesRegexp(AttributeError, invalid_function_name, inner_test)
        else:
            self.assertRaisesRegex(AttributeError, invalid_function_name, inner_test)


class TestFunctionMockCheckCall(unittest.TestCase):
    def test_no_called(self):
        def inner_test():
            @FunctionMockCheckCall(module_test, 'function_sum')
            def call_test():
                pass

            call_test()

        self.assertRaises(ValueError, inner_test)

    def test_called(self):
        @FunctionMockCheckCall(module_test, 'function_sum')
        def inner_test():
            return module_test.function_sum(2, 2)

        result = inner_test()
        self.assertEqual(result, 4, "The function result has been modified")

    def test_call_check_invocations_ok(self):
        @FunctionMockCheckCall(module_test, 'function_sum', expected_times=3)
        def inner_test():
            module_test.function_sum(2, 2)
            module_test.function_sum(2, 2)
            return module_test.function_sum(2, 2)

        result = inner_test()
        module_test.function_sum(2, 2)
        self.assertEqual(result, 4, "The function result has been modified")

    def test_call_check_invocations_ko(self):
        @FunctionMockCheckCall(module_test, 'function_sum', expected_times=2)
        def inner_test():
            module_test.function_sum(2, 2)
            module_test.function_sum(2, 2)
            return module_test.function_sum(2, 2)

        self.assertRaises(ValueError, inner_test)
        result = module_test.function_sum(2, 2)
        self.assertEqual(result, 4, "The function result has been modified")

    def test_call_change_return(self):
        @FunctionMockCheckCall(module_test, 'function_sum', return_value=3)
        def inner_test():
            return module_test.function_sum(2, 2)

        result_change = inner_test()
        result_no_change = module_test.function_sum(2, 2)
        self.assertEqual(result_change, 3, "The function result has been modified")
        self.assertEqual(result_no_change, 4, "The function result has been modified")

    def test_call_change_return_0(self):
        @FunctionMockCheckCall(module_test, 'function_sum', expected_times=1, return_value=0)
        def inner_test():
            return module_test.function_sum(2, 2)

        result_change = inner_test()
        result_no_change = module_test.function_sum(2, 2)
        self.assertEqual(result_change, 0, "The function result has been modified")
        self.assertEqual(result_no_change, 4, "The function result has been modified")

    def test_check_no_call_ok(self):
        @FunctionMockCheckCall(module_test, 'function_sum', expected_times=0)
        def inner_test():
            return 3

        result_no_change = module_test.function_sum(2, 2)
        self.assertEqual(result_no_change, 4, "The function result has been modified")

    def test_check_no_call_ko(self):
        @FunctionMockCheckCall(module_test, 'function_sum', expected_times=0)
        def inner_test():
            return module_test.function_sum(2, 2)

        self.assertRaises(ValueError, inner_test)
