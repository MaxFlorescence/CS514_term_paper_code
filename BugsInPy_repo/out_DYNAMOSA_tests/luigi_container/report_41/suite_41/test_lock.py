# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import lock as module_0


def test_case_0():
    str_0 = "Ygh(X%~"
    float_0 = 10000000052.422373
    var_0 = module_0.acquire_for(str_0, float_0)
    assert var_0 is True


def test_case_1():
    str_0 = "YXh(X}~"
    var_0 = module_0.acquire_for(str_0)
    assert var_0 is False


def test_case_2():
    str_0 = "2"
    var_0 = module_0.acquire_for(str_0)
    assert var_0 is False


def test_case_3():
    str_0 = '<I\t$[u)Ama95\x0b"qkf{#'
    var_0 = module_0.acquire_for(str_0)
    assert var_0 is False
    var_1 = module_0.acquire_for(str_0)
    assert var_1 is False
