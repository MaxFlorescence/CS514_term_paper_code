# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import cd_parent as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.match(object_0, object_0)


def test_case_1():
    dict_0 = {}
    none_type_0 = None
    var_0 = module_1.get_new_command(dict_0, none_type_0)
    assert var_0 == "cd .."
