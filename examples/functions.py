
def fun1():
    fun_no_mocked("argument")


def fun_no_mocked(arg):
    print("No mocked arg={}".format(arg))
