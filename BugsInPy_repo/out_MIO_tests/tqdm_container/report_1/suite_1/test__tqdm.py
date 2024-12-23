# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import _tqdm as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.format_sizeof(bool_0)
    assert var_0 == "1.00"


def test_case_1():
    float_0 = 1013.1365237818533
    var_0 = module_0.format_meter(
        float_0, float_0, float_0, float_0, ascii=float_0, unit_scale=float_0
    )
    assert (
        var_0
        == "100%|###########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################1| 1.01K/1.01K [16:53<00:00, 1.00it/s]"
    )
    var_1 = var_0.__len__()
    assert var_1 == 1014
    var_2 = module_0.StatusPrinter(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -74.19052631658907
    module_0.format_sizeof(float_0, float_0)


def test_case_3():
    int_0 = -165
    var_0 = module_0.format_sizeof(int_0)
    assert var_0 == "-165"


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -3881.26685
    module_0.format_meter(
        float_0, float_0, float_0, float_0, float_0, unit=float_0, unit_scale=float_0
    )


def test_case_5():
    float_0 = 1013.1365237818533
    tqdm_0 = module_0.tqdm(miniters=float_0, unit_scale=float_0, gui=float_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters == pytest.approx(1013.1365237818533, abs=0.01, rel=0.01)
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale == pytest.approx(1013.1365237818533, abs=0.01, rel=0.01)
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4483852, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4483852, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0


def test_case_6():
    bool_0 = True
    bool_1 = False
    var_0 = module_0.format_meter(bool_0, bool_0, bool_0, bool_1)
    assert var_0 == "100% True/True [00:01<00:00,  1.00it/s]"


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is True
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is True
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is True
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4503024, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4503024, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    module_0.format_interval(tqdm_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    float_0 = 1009.303
    object_0 = module_1.object()
    none_type_0 = None
    module_0.format_meter(
        float_0, object_0, object_0, unit=float_0, unit_scale=none_type_0
    )


def test_case_9():
    object_0 = module_1.object()
    none_type_0 = None
    tqdm_0 = module_0.tqdm(total=none_type_0, ascii=none_type_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4519522, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4519522, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = module_0.StatusPrinter(tqdm_0)


def test_case_10():
    bool_0 = True
    var_0 = module_0.format_meter(bool_0, bool_0, bool_0, bool_0)
    assert var_0 == "100%|█| True/True [00:01<00:00,  1.00it/s]"


@pytest.mark.xfail(strict=True)
def test_case_11():
    float_0 = 1009.303
    var_0 = module_0.format_meter(float_0, float_0, float_0, float_0)
    assert (
        var_0
        == "100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎| 1009.303/1009.303 [16:49<00:00,  1.00it/s]"
    )
    var_0.close()


def test_case_12():
    bool_0 = True
    tqdm_0 = module_0.tqdm(bool_0, total=bool_0, leave=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is True
    assert tqdm_0.desc == ""
    assert tqdm_0.total is True
    assert tqdm_0.leave is True
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4556139, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4556139, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0


def test_case_13():
    bool_0 = True
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is True
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is True
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is True
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.456657, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.456657, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update()
    assert tqdm_0.last_print_n == 1
    assert tqdm_0.n == 1
    var_1 = tqdm_0.update()
    assert tqdm_0.last_print_n == 2
    assert tqdm_0.n == 2


def test_case_14():
    none_type_0 = None
    tqdm_0 = module_0.tqdm(ncols=none_type_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.458733, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.458733, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    str_0 = "H4Iu? a85 "
    var_0 = tqdm_0.update()
    assert tqdm_0.n == 1
    tqdm_1 = module_0.tqdm(
        desc=str_0, leave=none_type_0, mininterval=str_0, miniters=tqdm_0
    )
    assert f"{type(tqdm_1).__module__}.{type(tqdm_1).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_1.iterable is None
    assert tqdm_1.desc == "H4Iu? a85 : "
    assert tqdm_1.total is None
    assert tqdm_1.leave is None
    assert (
        f"{type(tqdm_1.file).__module__}.{type(tqdm_1.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_1.ncols is None
    assert tqdm_1.mininterval == 0
    assert (
        f"{type(tqdm_1.miniters).__module__}.{type(tqdm_1.miniters).__qualname__}"
        == "_tqdm.tqdm"
    )
    assert tqdm_1.dynamic_miniters is False
    assert tqdm_1.ascii is False
    assert tqdm_1.disable is False
    assert tqdm_1.unit == "it"
    assert tqdm_1.unit_scale is False
    assert tqdm_1.gui is False
    assert tqdm_1.start_t == pytest.approx(1733323374.4597447, abs=0.01, rel=0.01)
    assert tqdm_1.last_print_t == pytest.approx(1733323374.4597447, abs=0.01, rel=0.01)
    assert tqdm_1.last_print_n == 0
    assert tqdm_1.n == 0


@pytest.mark.xfail(strict=True)
def test_case_15():
    str_0 = "0QE\n~hW6v\r!5"
    module_0.tqdm(str_0, str_0, file=str_0, ascii=str_0)


def test_case_16():
    bool_0 = False
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is False
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is False
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4617357, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4617357, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update()
    assert tqdm_0.last_print_n == 1
    assert tqdm_0.n == 1


def test_case_17():
    float_0 = 1997.49
    var_0 = module_0.format_meter(
        float_0, float_0, float_0, ascii=float_0, unit_scale=float_0
    )
    assert var_0 == "100%|##########| 2.00K/2.00K [33:17<00:00, 1.00it/s]"


@pytest.mark.xfail(strict=True)
def test_case_18():
    complex_0 = -17.538 + 1726.81232j
    none_type_0 = None
    module_0.tqdm(ncols=complex_0, unit=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    bool_0 = False
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is False
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is False
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4644718, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4644718, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    tqdm_0.__len__()


def test_case_20():
    bytes_0 = b"\xbd-Pv\xbe]xH\x8d\xa8\xdc\xd5p"
    tqdm_0 = module_0.tqdm(
        leave=bytes_0,
        ncols=bytes_0,
        mininterval=bytes_0,
        disable=bytes_0,
        unit_scale=bytes_0,
    )
    assert tqdm_0.desc == ""
    assert tqdm_0.ncols == b"\xbd-Pv\xbe]xH\x8d\xa8\xdc\xd5p"
    assert tqdm_0.mininterval == b"\xbd-Pv\xbe]xH\x8d\xa8\xdc\xd5p"
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0


def test_case_21():
    bool_0 = True
    tqdm_0 = module_0.tqdm(bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is True
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4664536, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4664536, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0


def test_case_22():
    bool_0 = False
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is False
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is False
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4674253, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4674253, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0


@pytest.mark.xfail(strict=True)
def test_case_23():
    float_0 = 1009.303
    set_0 = {float_0, float_0, float_0}
    object_0 = module_1.object()
    list_0 = [set_0, set_0, set_0, object_0]
    list_1 = [list_0]
    tqdm_0 = module_0.tqdm(list_0, ascii=object_0, gui=list_1)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert len(tqdm_0) == 4
    none_type_0 = None
    tqdm_1 = module_0.tqdm(total=none_type_0, ascii=none_type_0)
    assert f"{type(tqdm_1).__module__}.{type(tqdm_1).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_1.iterable is None
    assert tqdm_1.desc == ""
    assert tqdm_1.total is None
    assert tqdm_1.leave is False
    assert (
        f"{type(tqdm_1.file).__module__}.{type(tqdm_1.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_1.ncols is None
    assert tqdm_1.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_1.miniters == 0
    assert tqdm_1.dynamic_miniters is True
    assert tqdm_1.ascii is False
    assert tqdm_1.disable is False
    assert tqdm_1.unit == "it"
    assert tqdm_1.unit_scale is False
    assert tqdm_1.gui is False
    assert tqdm_1.start_t == pytest.approx(1733323374.4691195, abs=0.01, rel=0.01)
    assert tqdm_1.last_print_t == pytest.approx(1733323374.4691195, abs=0.01, rel=0.01)
    assert tqdm_1.last_print_n == 0
    assert tqdm_1.n == 0
    var_0 = module_0.StatusPrinter(tqdm_1)
    tqdm_2 = module_0.tqdm(total=list_1, mininterval=var_0, disable=list_0, unit=tqdm_1)
    assert f"{type(tqdm_2).__module__}.{type(tqdm_2).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_2.iterable is None
    assert tqdm_2.desc == ""
    assert (
        f"{type(tqdm_2.total).__module__}.{type(tqdm_2.total).__qualname__}"
        == "builtins.list"
    )
    assert len(tqdm_2.total) == 1
    assert tqdm_2.leave is False
    assert (
        f"{type(tqdm_2.file).__module__}.{type(tqdm_2.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_2.ncols is None
    assert tqdm_2.miniters == 0
    assert tqdm_2.dynamic_miniters is True
    assert tqdm_2.ascii is False
    assert (
        f"{type(tqdm_2.disable).__module__}.{type(tqdm_2.disable).__qualname__}"
        == "builtins.list"
    )
    assert len(tqdm_2.disable) == 4
    assert (
        f"{type(tqdm_2.unit).__module__}.{type(tqdm_2.unit).__qualname__}"
        == "_tqdm.tqdm"
    )
    assert tqdm_2.unit_scale is False
    assert tqdm_2.gui is False
    assert tqdm_2.start_t == pytest.approx(1733323374.4699786, abs=0.01, rel=0.01)
    assert tqdm_2.last_print_t == pytest.approx(1733323374.4699786, abs=0.01, rel=0.01)
    assert tqdm_2.last_print_n == 0
    assert tqdm_2.n == 0
    module_1.object(*tqdm_2)


@pytest.mark.xfail(strict=True)
def test_case_24():
    none_type_0 = None
    tqdm_0 = module_0.tqdm(total=none_type_0, ascii=none_type_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4716551, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4716551, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    module_0.trange(*tqdm_0)


@pytest.mark.xfail(strict=True)
def test_case_25():
    float_0 = -838.3
    var_0 = module_0.format_interval(float_0)
    assert var_0 == "-1:46:02"
    tqdm_0 = module_0.tqdm(var_0, ascii=var_0, unit=var_0, gui=var_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert len(tqdm_0) == 8
    module_1.object(*tqdm_0)


def test_case_26():
    bool_0 = True
    tqdm_0 = module_0.tqdm(total=bool_0, disable=bool_0, unit_scale=bool_0)
    assert tqdm_0.desc == ""
    assert tqdm_0.total is True
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update()


def test_case_27():
    bool_0 = False
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is False
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is False
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4760442, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4760442, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update(bool_0)
    assert tqdm_0.last_print_n == 1
    assert tqdm_0.n == 1


def test_case_28():
    float_0 = 1009.303
    tqdm_0 = module_0.tqdm(
        leave=float_0,
        mininterval=float_0,
        miniters=float_0,
        unit_scale=float_0,
        gui=float_0,
    )
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave == pytest.approx(1009.303, abs=0.01, rel=0.01)
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters == pytest.approx(1009.303, abs=0.01, rel=0.01)
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale == pytest.approx(1009.303, abs=0.01, rel=0.01)
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4781353, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4781353, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update()
    assert tqdm_0.n == 1
    object_0 = module_1.object()
    tqdm_1 = module_0.tqdm(total=var_0, ascii=var_0)
    assert tqdm_1.desc == ""
    assert tqdm_1.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_1.miniters == 0
    assert tqdm_1.dynamic_miniters is True
    assert tqdm_1.ascii is False
    assert tqdm_1.unit == "it"
    assert tqdm_1.last_print_n == 0
    assert tqdm_1.n == 0
    var_1 = module_0.StatusPrinter(tqdm_1)


def test_case_29():
    none_type_0 = None
    tqdm_0 = module_0.tqdm(total=none_type_0, ascii=none_type_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == pytest.approx(0.1, abs=0.01, rel=0.01)
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4822304, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4822304, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update()
    assert tqdm_0.n == 1


@pytest.mark.xfail(strict=True)
def test_case_30():
    bool_0 = False
    tqdm_0 = module_0.tqdm(bool_0, total=bool_0, ncols=bool_0, mininterval=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is False
    assert tqdm_0.desc == ""
    assert tqdm_0.total is False
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is False
    assert tqdm_0.mininterval is False
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4838192, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4838192, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.update(bool_0)
    assert tqdm_0.miniters == 1
    assert tqdm_0.last_print_n == 1
    assert tqdm_0.n == 1
    var_0.__len__()


def test_case_31():
    bool_0 = True
    tqdm_0 = module_0.tqdm(total=bool_0, miniters=bool_0, ascii=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is True
    assert tqdm_0.leave is False
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is True
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is True
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4855092, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4855092, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.close()


def test_case_32():
    none_type_0 = None
    set_0 = {none_type_0}
    tqdm_0 = module_0.tqdm(
        total=none_type_0, leave=set_0, ncols=none_type_0, mininterval=none_type_0
    )
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is None
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave == {None}
    assert (
        f"{type(tqdm_0.file).__module__}.{type(tqdm_0.file).__qualname__}"
        == "_io.TextIOWrapper"
    )
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval is None
    assert tqdm_0.miniters == 0
    assert tqdm_0.dynamic_miniters is True
    assert tqdm_0.ascii is False
    assert tqdm_0.disable is False
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4870222, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4870222, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.close()


@pytest.mark.xfail(strict=True)
def test_case_33():
    bool_0 = True
    tqdm_0 = module_0.tqdm(bool_0, file=bool_0, miniters=bool_0, disable=bool_0)
    assert f"{type(tqdm_0).__module__}.{type(tqdm_0).__qualname__}" == "_tqdm.tqdm"
    assert tqdm_0.iterable is True
    assert tqdm_0.desc == ""
    assert tqdm_0.total is None
    assert tqdm_0.leave is False
    assert tqdm_0.file is True
    assert tqdm_0.ncols is None
    assert tqdm_0.mininterval == 0
    assert tqdm_0.miniters is True
    assert tqdm_0.dynamic_miniters is False
    assert tqdm_0.ascii is True
    assert tqdm_0.disable is True
    assert tqdm_0.unit == "it"
    assert tqdm_0.unit_scale is False
    assert tqdm_0.gui is False
    assert tqdm_0.start_t == pytest.approx(1733323374.4884863, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_t == pytest.approx(1733323374.4884863, abs=0.01, rel=0.01)
    assert tqdm_0.last_print_n == 0
    assert tqdm_0.n == 0
    var_0 = tqdm_0.__iter__()
    var_1 = tqdm_0.close()
    var_0.__len__()


def test_case_34():
    none_type_0 = None
    var_0 = module_0.StatusPrinter(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_35():
    module_0.trange()
