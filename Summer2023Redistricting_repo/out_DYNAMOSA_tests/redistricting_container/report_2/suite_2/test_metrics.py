# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import metrics as module_0
import numpy as module_1
import networkx.algorithms.triads as module_2
import networkx.algorithms.cuts as module_3
import platform as module_4
import inspect as module_5


def test_case_0():
    str_0 = "pL5~8"
    with pytest.raises(Exception):
        module_0.map_to_updater(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.round(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.cut_edge_count(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.disparity(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_0.deviation(none_type_0, none_type_0)


def test_case_5():
    var_0 = module_1.geterr()
    var_1 = module_0.producing_spanning_trees(var_0)
    assert var_1 == -1
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    str_0 = "cut edges"
    bool_0 = True
    callable_0 = module_0.map_to_updater(str_0, bool_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    module_2.triad_type(none_type_0)


def test_case_7():
    str_0 = "size deviation"
    with pytest.raises(Exception):
        module_0.map_to_updater(str_0)


def test_case_8():
    bool_0 = True
    int_0 = module_0.round(bool_0)
    assert int_0 == 1
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    str_0 = "pL5~8"
    str_1 = "size disparity"
    bool_1 = False
    callable_0 = module_0.map_to_updater(str_1, target_population=bool_1)
    with pytest.raises(Exception):
        module_0.map_to_updater(str_0)


def test_case_9():
    str_0 = "log producing spanning trees"
    callable_0 = module_0.map_to_updater(str_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "population deviation"
    callable_0 = module_0.map_to_updater(str_0, str_0, str_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    none_type_0 = None
    module_3.node_expansion(none_type_0, str_0, **str_0)


def test_case_11():
    none_type_0 = None
    str_0 = "producing spanning trees"
    callable_0 = module_0.map_to_updater(str_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    var_0 = module_0.producing_spanning_trees(none_type_0)
    assert var_0 == -1
    str_1 = "Gon"
    none_type_1 = None
    with pytest.raises(Exception):
        module_0.map_to_updater(str_1, none_type_1)


def test_case_12():
    var_0 = module_4.version()
    bool_0 = False
    bool_1 = True
    int_0 = module_0.round(bool_1)
    assert int_0 == 1
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    str_0 = "population deviation"
    callable_0 = module_0.map_to_updater(str_0, var_0, int_0)
    with pytest.raises(Exception):
        module_0.map_to_updater(str_0, bool_0)


def test_case_13():
    none_type_0 = None
    var_0 = module_4.version()
    bool_0 = True
    str_0 = "population disparity"
    callable_0 = module_0.map_to_updater(str_0, var_0, bool_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    str_1 = "Gon"
    with pytest.raises(Exception):
        module_0.map_to_updater(str_1, target_population=none_type_0)


def test_case_14():
    str_0 = "contiguous"
    callable_0 = module_0.map_to_updater(str_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]


@pytest.mark.xfail(strict=True)
def test_case_15():
    str_0 = "size deviation"
    callable_0 = module_0.map_to_updater(str_0, str_0)
    assert module_0.available == [
        "cut edges",
        "size disparity",
        "population disparity",
        "size deviation",
        "population deviation",
        "contiguous",
        "producing spanning trees",
        "log producing spanning trees",
    ]
    bool_0 = True
    bool_1 = True
    int_0 = module_0.round(bool_1)
    assert int_0 == 1
    var_0 = module_0.producing_spanning_trees(str_0, bool_0)
    assert var_0 == -1
    module_5.cleandoc(bool_0)
