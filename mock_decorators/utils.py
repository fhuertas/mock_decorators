import inspect
import sys


def test_signature(function_a, function_b):
    signature_a = _check_signature_function(function_a)
    signature_b = _check_signature_function(function_b)
    if signature_a != signature_b:
        raise TypeError("The functions have not the same signature.\n\n"
                        "A) {}: Specs:\n{}\n\n"
                        "B) {}: Specs:\n{}"
                        .format(function_a.__name__, str(signature_a),
                                function_b.__name__, str(signature_b)
                                ))
    return True


def _check_signature_function(function):
    if sys.version_info < (3, 0):
        return inspect.getargspec(function)
    else:
        return inspect.getfullargspec(function)
