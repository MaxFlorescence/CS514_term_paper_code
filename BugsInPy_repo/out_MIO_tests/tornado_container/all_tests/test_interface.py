# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import interface as module_0


def test_case_0():
    waker_0 = module_0.Waker()


def test_case_1():
    none_type_0 = None
    module_0.set_close_exec(none_type_0)


def test_case_2():
    waker_0 = module_0.Waker()
    waker_0.fileno()


def test_case_3():
    waker_0 = module_0.Waker()
    waker_0.write_fileno()


def test_case_4():
    waker_0 = module_0.Waker()
    waker_0.wake()


def test_case_5():
    waker_0 = module_0.Waker()
    waker_0.consume()


def test_case_6():
    waker_0 = module_0.Waker()
    waker_0.close()
