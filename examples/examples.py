import os
import sys

import functions
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from mock_decorator.function_mock import FunctionMock


def fun_mocked(arg):
    print("Mocked arg={}".format(arg))

@FunctionMock(entity=functions,function_name='fun_no_mocked',mocked_function=fun_mocked)
def test_mock_function():
    functions.fun1()

def test_no_mock():
    functions.fun1()


if __name__ == '__main__':
    test_mock_function()
    test_no_mock()
