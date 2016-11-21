from io import StringIO
import unittest
from mock_decorators.mock_sys_output import MockSysOutput


class TestMockIORedirect(unittest.TestCase):
    def test_stdout_redirect(self):
        output = StringIO()
        first_string = "first  string"
        second_string = "second string"
        string_out = "no string"
        with MockSysOutput._stdout_redirect(output):
            print(first_string)
            print(second_string)
        print(string_out)
        result = output.read()
        self.assertTrue(first_string in result)
        self.assertTrue(second_string in result)
        self.assertFalse(string_out in result)

    def test_mock(self):
        output = StringIO()
        i_string = "inner string"
        o_string = "outter string"

        @MockSysOutput(output)
        def inner_test():
            print(i_string)

        inner_test()
        print(o_string)

        result = output.read()

        self.assertTrue(i_string in result)
        self.assertFalse(o_string in result)

    def test_invalid(self):
        output = StringIO()
        i_string = "inner string"
        p_string = "the monkey island is the best"
        output.write(p_string)

        @MockSysOutput(output)
        def inner_test():
            print(i_string)

        inner_test()

        result = output.read()

        self.assertEqual(i_string, result[:-1])
