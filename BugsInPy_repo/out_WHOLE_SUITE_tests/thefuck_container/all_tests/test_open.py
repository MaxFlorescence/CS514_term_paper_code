# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import open as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "ype0==kPqB:"
    module_0.get_new_command(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 192
    module_0.get_new_command(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    object_0 = module_1.object(**dict_0)
    none_type_0 = None
    module_0.get_new_command(object_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    module_0.get_new_command(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x9f\xe4\xf6\xa4\x95\x82\xe9+"
    module_0.get_new_command(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "x]fgrTzByZ"
    none_type_0 = None
    module_0.match(none_type_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "ZE$86\x0b"
    none_type_0 = None
    module_0.match(none_type_0, str_0)
