# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import httpobj as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x08\xd3\xa9\x92\x14\xcbo^k"
    module_0.urlparse_cached(bytes_0)
