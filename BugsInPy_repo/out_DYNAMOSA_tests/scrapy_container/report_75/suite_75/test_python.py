# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import python as module_0
import ast as module_1
import inspect as module_2
import enum as module_3
import collections as module_4


def test_case_0():
    str_0 = "F\rK5XBS_y"
    var_0 = module_0.unique(str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.unique(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.str_to_unicode(none_type_0, errors=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.unicode_to_str(bool_0, errors=bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bin_op_0 = module_1.BinOp()
    none_type_0 = None
    var_0 = module_0.memoizemethod_noargs(none_type_0)
    var_1 = module_1.get_source_segment(bin_op_0, none_type_0)
    module_0.unicode_to_str(none_type_0, bin_op_0)


def test_case_5():
    str_0 = "QkT8-EWZV|\rGw{\nq("
    var_0 = module_0.isbinarytext(str_0)
    assert var_0 is False


def test_case_6():
    none_type_0 = None
    with pytest.raises(AssertionError):
        module_0.isbinarytext(none_type_0)


def test_case_7():
    none_type_0 = None
    with pytest.raises(TypeError):
        module_0.get_func_args(none_type_0, none_type_0)


def test_case_8():
    bool_0 = True
    with pytest.raises(TypeError):
        module_0.get_spec(bool_0)


def test_case_9():
    none_type_0 = None
    var_0 = module_0.equal_attributes(none_type_0, none_type_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_10():
    bool_0 = False
    module_0.is_writable(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    none_type_0 = None
    module_0.retry_on_eintr(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    none_type_0 = None
    module_0.re_rsearch(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    none_type_0 = None
    module_0.flatten(none_type_0)


def test_case_14():
    none_type_0 = None
    var_0 = module_0.memoizemethod_noargs(none_type_0)


def test_case_15():
    none_type_0 = None
    weak_key_cache_0 = module_0.WeakKeyCache(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    bytes_0 = b"\xf5\xad\xbbR9Mb\x1b\xb6\x83\x94(l\x07\xee\x1f\x84\x84\xab\xbf"
    var_0 = module_0.unique(bytes_0)
    int_0 = -4198
    var_1 = module_0.iflatten(int_0)
    none_type_0 = None
    module_0.stringify_dict(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    none_type_0 = None
    var_0 = module_0.memoizemethod_noargs(none_type_0)
    module_2.getmembers(none_type_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_18():
    none_type_0 = None
    weak_key_cache_0 = module_0.WeakKeyCache(none_type_0)
    weak_key_cache_0.__getitem__(none_type_0)


def test_case_19():
    str_0 = "PH"
    var_0 = module_0.equal_attributes(str_0, str_0, str_0)
    assert var_0 is False


def test_case_20():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.stringify_dict(enum_dict_0, keys_only=enum_dict_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    str_0 = "PH"
    module_0.str_to_unicode(str_0)


@pytest.mark.xfail(strict=True)
def test_case_22():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.equal_attributes(enum_dict_0, enum_dict_0, enum_dict_0)
    assert var_0 is False
    list_0 = [enum_dict_0]
    var_1 = module_0.flatten(list_0)
    var_2 = module_0.memoizemethod_noargs(var_0)
    var_3 = module_0.iflatten(list_0)
    var_4 = var_2.__eq__(var_1)
    module_0.str_to_unicode(var_4, var_4)


@pytest.mark.xfail(strict=True)
def test_case_23():
    str_0 = "PH"
    module_0.setattr_default(str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_24():
    str_0 = "PH"
    var_0 = module_0.unique(str_0)
    var_1 = module_0.is_writable(str_0)
    module_0.setattr_default(str_0, str_0, str_0)


def test_case_25():
    str_0 = "PH"
    var_0 = module_0.memoizemethod_noargs(str_0)
    var_1 = module_0.equal_attributes(str_0, str_0, str_0)
    assert var_1 is False
    var_2 = module_0.get_func_args(var_0)


def test_case_26():
    bytes_0 = b":\x0c"
    var_0 = module_0.flatten(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_27():
    str_0 = "RK.^{goH/0A_2"
    module_0.flatten(str_0)


@pytest.mark.xfail(strict=True)
def test_case_28():
    str_0 = "PH"
    var_0 = module_0.memoizemethod_noargs(str_0)
    var_1 = module_0.get_func_args(var_0, var_0)
    var_2 = module_0.iflatten(var_1)
    module_0.retry_on_eintr(str_0, *var_1)


def test_case_29():
    none_type_0 = None
    var_0 = module_0.memoizemethod_noargs(none_type_0)
    var_1 = module_0.get_func_args(var_0)
    var_2 = module_0.get_spec(var_0)


@pytest.mark.xfail(strict=True)
def test_case_30():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.stringify_dict(enum_dict_0, keys_only=enum_dict_0)
    var_1 = module_2.getcomments(var_0)
    var_2 = module_0.flatten(var_0)
    var_3 = var_1.__dir__()
    var_4 = module_0.equal_attributes(var_0, var_1, var_3)
    assert var_4 is False
    var_5 = module_0.memoizemethod_noargs(var_2)
    var_6 = module_0.get_spec(var_5)
    bool_0 = False
    var_5.center(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_31():
    enum_dict_0 = module_3._EnumDict()
    chain_map_0 = module_4.ChainMap(*enum_dict_0)
    var_0 = module_0.flatten(chain_map_0)
    var_1 = chain_map_0.__dir__()
    var_2 = module_0.equal_attributes(chain_map_0, var_0, var_1)
    assert var_2 is False
    var_3 = module_0.memoizemethod_noargs(var_0)
    module_0.retry_on_eintr(enum_dict_0)


@pytest.mark.xfail(strict=True)
def test_case_32():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.stringify_dict(enum_dict_0, keys_only=enum_dict_0)
    var_1 = var_0.__dir__()
    var_2 = module_0.equal_attributes(var_0, enum_dict_0, var_1)
    assert var_2 is False
    module_0.str_to_unicode(var_2, enum_dict_0)


def test_case_33():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.stringify_dict(enum_dict_0, keys_only=enum_dict_0)
    var_1 = module_0.flatten(var_0)
    weak_key_cache_0 = module_0.WeakKeyCache(var_0)
    var_2 = var_1.__iter__()
    var_3 = module_0.equal_attributes(enum_dict_0, enum_dict_0, var_2)
    assert var_3 is True
    var_4 = module_0.memoizemethod_noargs(weak_key_cache_0)
    with pytest.raises(TypeError):
        module_0.get_func_args(var_2, var_1)


@pytest.mark.xfail(strict=True)
def test_case_34():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.stringify_dict(enum_dict_0, keys_only=enum_dict_0)
    var_1 = module_2.getcomments(var_0)
    var_2 = module_0.flatten(var_0)
    var_3 = module_0.equal_attributes(var_0, var_1, var_1)
    assert var_3 is False
    var_4 = module_0.memoizemethod_noargs(var_0)
    var_5 = module_0.iflatten(var_0)
    var_6 = var_0.__setitem__(var_4, var_1)
    var_7 = module_2.BlockFinder()
    module_0.equal_attributes(enum_dict_0, var_7, var_5)


@pytest.mark.xfail(strict=True)
def test_case_35():
    enum_dict_0 = module_3._EnumDict()
    var_0 = enum_dict_0.__str__()
    var_1 = module_0.flatten(enum_dict_0)
    weak_key_cache_0 = module_0.WeakKeyCache(var_0)
    var_2 = module_0.memoizemethod_noargs(weak_key_cache_0)
    var_3 = module_0.setattr_default(weak_key_cache_0, var_0, var_2)
    var_4 = module_0.iflatten(var_3)
    var_5 = module_0.setattr_default(weak_key_cache_0, var_0, var_2)
    var_6 = module_0.equal_attributes(var_0, var_0, var_0)
    assert var_6 is False
    var_7 = module_2.getcoroutinelocals(var_2)
    var_8 = module_2.getcoroutinelocals(var_0)
    void_0 = module_2._void()
    var_9 = module_0.get_spec(var_2)
    module_0.equal_attributes(var_0, var_2, var_4)


def test_case_36():
    enum_dict_0 = module_3._EnumDict()
    var_0 = module_0.equal_attributes(enum_dict_0, enum_dict_0, enum_dict_0)
    assert var_0 is False
    list_0 = [enum_dict_0]
    var_1 = module_0.flatten(list_0)
    var_2 = module_0.memoizemethod_noargs(var_0)
    with pytest.raises(TypeError):
        module_0.get_spec(list_0)
