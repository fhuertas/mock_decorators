import unittest
from mock_decorators.dict_mock import DictMock
from tests.mock_decorators import module_test


class TestDictMock(unittest.TestCase):
    def test_dict_mock_ok(self):
        changed_result = 20
        old_value = module_test.a_dict['value_a']
        old_value_hardcoded = 22

        @DictMock(module_test.a_dict, 'value_a', changed_result, True)
        def inner_test():
            return module_test.a_dict['value_a']

        result_mocked = inner_test()

        self.assertEqual(result_mocked, changed_result)
        self.assertEqual(module_test.a_dict['value_a'], old_value)
        self.assertEqual(module_test.a_dict['value_a'], old_value_hardcoded)
        self.assertNotEqual(module_test.a_dict['value_a'], changed_result)

    def test_dict_mock_ok_no_exists(self):
        changed_result = 20

        @DictMock(module_test.a_dict, 'value_c', changed_result, False)
        def inner_test():
            return module_test.a_dict['value_c']

        result_mocked = inner_test()

        self.assertEqual(result_mocked, changed_result)
        self.assertFalse('value_c' in module_test.a_dict)

    def test_dict_mock_error_no_exists(self):
        changed_result = 20

        @DictMock(module_test.a_dict, 'value_c', changed_result, True)
        def inner_test():
            return module_test.a_dict['value_c']

        self.assertRaises(TypeError, inner_test)

    def test_dict_none_ok(self):
        changed_result = 20
        old_value = module_test.a_dict['value_b']
        old_value_hardcoded = None

        @DictMock(module_test.a_dict, 'value_b', changed_result, True)
        def inner_test():
            return module_test.a_dict['value_b']

        result_mocked = inner_test()

        self.assertEqual(result_mocked, changed_result)
        self.assertEqual(module_test.a_dict['value_b'], old_value)
        self.assertEqual(module_test.a_dict['value_b'], old_value_hardcoded)
        self.assertNotEqual(module_test.a_dict['value_b'], changed_result)
        self.assertTrue('value_b' in module_test.a_dict)

