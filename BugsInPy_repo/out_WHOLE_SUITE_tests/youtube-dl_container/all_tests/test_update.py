# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import email._header_value_parser as module_0
import update as module_1
import codecs as module_2
import _locale as module_3


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -997.091303
    module_0.get_extended_attrtext(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa1\x13V\x9f?\x8e#[\xb9\xa7\x06];\x94\xd9"
    module_1.rsa_verify(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x03'/\xb7\x1c\x8d=;X"
    module_1.rsa_verify(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x00"
    module_1.rsa_verify(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_1.update_self(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    dict_0 = {}
    var_0 = module_1.print_notes(dict_0, dict_0)
    var_1 = module_1.print_notes(var_0, dict_0)
    var_0.parse(var_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    module_2.getencoder(none_type_0)


def test_case_7():
    none_type_0 = None
    with pytest.raises(AssertionError):
        module_1.rsa_verify(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    module_1.update_self(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    var_0 = module_3.localeconv()
    module_1.print_notes(var_0, var_0)
