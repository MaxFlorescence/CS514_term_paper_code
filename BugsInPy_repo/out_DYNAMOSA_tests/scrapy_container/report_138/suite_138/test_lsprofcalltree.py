# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import re as module_0
import lsprofcalltree as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    var_0 = module_0.purge()
    module_1.label(var_0)


def test_case_1():
    str_0 = 'V![xF"tr.\x0cgx1[vB,\\'
    var_0 = module_1.label(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.KCacheGrind(none_type_0)
