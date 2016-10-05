import inspect


def test_signature(function_a, function_b):
    signature_a = inspect.getfullargspec(function_a)
    signature_b = inspect.getfullargspec(function_b)
    if signature_a != signature_b:
        raise TypeError("The functions have not the same signature.\n\n"
                        "A) {}: Specs:\n{}\n\n"
                        "B) {}: Specs:\n{}"
                        .format(function_a.__name__, str(signature_a),
                                function_b.__name__, str(signature_b)
                                ))
    return True
