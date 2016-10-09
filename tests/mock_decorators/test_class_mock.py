import sys
import unittest

from mock_decorators.class_mock import ClassMock
from tests.mock_decorators.module_test import TestClass


class MockedClass:
    mocked = False
    function_called = False

    def __init__(self):
        self.mocked = True

    def function(self):
        return True

    @classmethod
    def class_function(cls):
        return True


class TestClassMock(unittest.TestCase):
    def test_mock_class_creation(self):
        if sys.version_info < (3, 0):
            print("WARNING: Ignoring test. Class mock not support python 2.*. Current version: {}".format(sys.version))
        else:

            @ClassMock(TestClass, MockedClass)
            def inner_test():
                return TestClass()

            mocked_class = inner_test()
            no_mocked_class = TestClass()
            self.assertTrue(mocked_class.mocked)
            self.assertFalse(no_mocked_class.mocked)

    def test_mock_class_static_method(self):
        if sys.version_info < (3, 0):
            print("WARNING: Ignoring test. Class mock not support python 2.*. Current version: {}".format(sys.version))
        else:
            @ClassMock(TestClass, MockedClass)
            def inner_test():
                return TestClass.class_function()

            self.assertTrue(inner_test(), "The mocked class is not mocked")
            self.assertFalse(TestClass.class_function(), "The no mocked class is mocked")

    def test_mock_class_class_method(self):
        if sys.version_info < (3, 0):
            print("WARNING: Ignoring test. Class mock not support python 2.*. Current version: {}".format(sys.version))
        else:
            no_mocked_object = TestClass()

            @ClassMock(TestClass, MockedClass)
            def inner_test():
                mocked_object = TestClass()
                return mocked_object.function()

            self.assertTrue(inner_test(), "The mocked object is not mocked")
            self.assertFalse(no_mocked_object.class_function(), "The no object class is mocked")
