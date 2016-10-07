import unittest
from mock_decorators.attribute_mock import AttributeMock
from tests.mock_decorators import module_test


class TestAttributeMock(unittest.TestCase):
    def test_attribute_mock_ok(self):
        changed_result = 20

        @AttributeMock(module_test, 'a_parameter', changed_result)
        def inner_test():
            return module_test.a_parameter

        result_mocked = inner_test()

        self.assertEqual(result_mocked, changed_result)
        self.assertNotEqual(module_test.a_parameter, changed_result)

    def test_attribute_mock_new_parameter(self):
        changed_result = 20

        @AttributeMock(module_test, 'other_parameter', changed_result)
        def inner_test():
            return module_test.other_parameter

        def inner_test2():
            return module_test.other_parameter

        result_mocked = inner_test()

        self.assertEqual(result_mocked, changed_result)

        self.assertRaisesRegex(AttributeError, 'other_parameter', inner_test2)
