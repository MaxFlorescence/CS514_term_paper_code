# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import trackref as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    var_0 = module_0.format_live_refs()
    assert var_0 == "Live References\n\n"
    assert len(module_0.live_refs) == 1
    none_type_0 = None
    var_0.__new__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    var_0 = module_0.format_live_refs()
    assert var_0 == "Live References\n\n"
    assert len(module_0.live_refs) == 1
    var_1 = module_0.format_live_refs()
    assert var_1 == "Live References\n\n"
    var_2 = module_0.get_oldest(var_0)
    var_0.__new__(var_0)


def test_case_2():
    none_type_0 = None
    var_0 = module_0.iter_all(none_type_0)
    assert len(module_0.live_refs) == 1


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.object_ref()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "btu\\i"
    var_0 = module_0.iter_all(str_0)
    complex_0 = 5051.69293 - 2600.20377j
    var_1 = module_0.print_live_refs()
    module_0.print_live_refs(*complex_0, **var_1)


def test_case_5():
    str_0 = "object_ref"
    var_0 = module_0.get_oldest(str_0)


def test_case_6():
    str_0 = "object_ref"
    var_0 = module_0.iter_all(str_0)
    var_1 = module_0.get_oldest(str_0)


def test_case_7():
    none_type_0 = None
    var_0 = module_0.get_oldest(none_type_0)
    var_1 = module_0.format_live_refs(var_0)
    assert var_1 == "Live References\n\n"
    var_2 = module_0.iter_all(var_0)


def test_case_8():
    bool_0 = True
    bool_1 = True
    none_type_0 = None
    var_0 = module_0.get_oldest(none_type_0)
    list_0 = [bool_0, bool_0, bool_0, bool_1]
    var_1 = module_0.iter_all(list_0)
    var_2 = module_0.print_live_refs()
