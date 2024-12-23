# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import util as module_0
import tokenize as module_1
import inspect as module_2


def test_case_0():
    gzip_decompressor_0 = module_0.GzipDecompressor()
    assert (
        f"{type(gzip_decompressor_0).__module__}.{type(gzip_decompressor_0).__qualname__}"
        == "util.GzipDecompressor"
    )
    assert (
        f"{type(gzip_decompressor_0.decompressobj).__module__}.{type(gzip_decompressor_0.decompressobj).__qualname__}"
        == "zlib.Decompress"
    )
    assert (
        f"{type(module_0.GzipDecompressor.unconsumed_tail).__module__}.{type(module_0.GzipDecompressor.unconsumed_tail).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_dict_0 = module_0.ObjectDict()
    module_0.timedelta_to_seconds(object_dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_dict_0 = module_0.ObjectDict()
    object_dict_0.__getattr__(object_dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    var_0 = module_1.any()
    module_0.import_object(var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ".jr(@Lx&_y"
    module_0.import_object(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    module_0.import_object(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    module_0.errno_from_exception(none_type_0)


def test_case_7():
    var_0 = module_0.doctests()
    arg_replacer_0 = module_0.ArgReplacer(var_0, var_0)
    assert (
        f"{type(arg_replacer_0).__module__}.{type(arg_replacer_0).__qualname__}"
        == "util.ArgReplacer"
    )
    assert arg_replacer_0.arg_pos is None


@pytest.mark.xfail(strict=True)
def test_case_8():
    none_type_0 = None
    module_0.ArgReplacer(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    var_0 = module_0.doctests()
    arg_replacer_0 = module_0.ArgReplacer(var_0, var_0)
    assert (
        f"{type(arg_replacer_0).__module__}.{type(arg_replacer_0).__qualname__}"
        == "util.ArgReplacer"
    )
    assert arg_replacer_0.arg_pos is None
    arg_replacer_0.get_old_value(arg_replacer_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    var_0 = module_0.doctests()
    arg_replacer_0 = module_0.ArgReplacer(var_0, var_0)
    assert (
        f"{type(arg_replacer_0).__module__}.{type(arg_replacer_0).__qualname__}"
        == "util.ArgReplacer"
    )
    assert arg_replacer_0.arg_pos is None
    arg_replacer_0.replace(var_0, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    object_dict_0 = module_0.ObjectDict()
    object_dict_0.__setattr__(object_dict_0, object_dict_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    gzip_decompressor_0 = module_0.GzipDecompressor()
    assert (
        f"{type(gzip_decompressor_0).__module__}.{type(gzip_decompressor_0).__qualname__}"
        == "util.GzipDecompressor"
    )
    assert (
        f"{type(gzip_decompressor_0.decompressobj).__module__}.{type(gzip_decompressor_0.decompressobj).__qualname__}"
        == "zlib.Decompress"
    )
    assert (
        f"{type(module_0.GzipDecompressor.unconsumed_tail).__module__}.{type(module_0.GzipDecompressor.unconsumed_tail).__qualname__}"
        == "builtins.property"
    )
    gzip_decompressor_0.decompress(gzip_decompressor_0)


def test_case_13():
    gzip_decompressor_0 = module_0.GzipDecompressor()
    assert (
        f"{type(gzip_decompressor_0).__module__}.{type(gzip_decompressor_0).__qualname__}"
        == "util.GzipDecompressor"
    )
    assert (
        f"{type(gzip_decompressor_0.decompressobj).__module__}.{type(gzip_decompressor_0.decompressobj).__qualname__}"
        == "zlib.Decompress"
    )
    assert (
        f"{type(module_0.GzipDecompressor.unconsumed_tail).__module__}.{type(module_0.GzipDecompressor.unconsumed_tail).__qualname__}"
        == "builtins.property"
    )
    var_0 = module_2.getmembers(gzip_decompressor_0)


def test_case_14():
    gzip_decompressor_0 = module_0.GzipDecompressor()
    assert (
        f"{type(gzip_decompressor_0).__module__}.{type(gzip_decompressor_0).__qualname__}"
        == "util.GzipDecompressor"
    )
    assert (
        f"{type(gzip_decompressor_0.decompressobj).__module__}.{type(gzip_decompressor_0.decompressobj).__qualname__}"
        == "zlib.Decompress"
    )
    assert (
        f"{type(module_0.GzipDecompressor.unconsumed_tail).__module__}.{type(module_0.GzipDecompressor.unconsumed_tail).__qualname__}"
        == "builtins.property"
    )
    var_0 = gzip_decompressor_0.flush()


def test_case_15():
    var_0 = module_0.doctests()
    var_1 = module_0.u(var_0)


@pytest.mark.xfail(strict=True)
def test_case_16():
    module_0.Configurable()


@pytest.mark.xfail(strict=True)
def test_case_17():
    gzip_decompressor_0 = module_0.GzipDecompressor()
    assert (
        f"{type(gzip_decompressor_0).__module__}.{type(gzip_decompressor_0).__qualname__}"
        == "util.GzipDecompressor"
    )
    assert (
        f"{type(gzip_decompressor_0.decompressobj).__module__}.{type(gzip_decompressor_0.decompressobj).__qualname__}"
        == "zlib.Decompress"
    )
    assert (
        f"{type(module_0.GzipDecompressor.unconsumed_tail).__module__}.{type(module_0.GzipDecompressor.unconsumed_tail).__qualname__}"
        == "builtins.property"
    )
    module_0.timedelta_to_seconds(gzip_decompressor_0)


def test_case_18():
    var_0 = module_0.doctests()
