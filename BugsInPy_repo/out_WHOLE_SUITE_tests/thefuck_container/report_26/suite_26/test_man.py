# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import man as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "RJ%U&{]PuI?P"
    module_0.get_new_command(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"3`\x85p\x91r\xe4:\xbf>/;\xaa\x1c\x13y|\xf1\xe5\x98"
    none_type_0 = None
    module_0.match(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.match(list_0, list_0)
