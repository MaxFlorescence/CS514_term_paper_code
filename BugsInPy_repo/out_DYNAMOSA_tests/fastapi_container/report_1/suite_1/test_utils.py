# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import utils as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.get_authorization_scheme_param(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    tuple_0 = module_0.get_authorization_scheme_param(none_type_0)
    int_0 = -3016
    module_0.get_authorization_scheme_param(int_0)
