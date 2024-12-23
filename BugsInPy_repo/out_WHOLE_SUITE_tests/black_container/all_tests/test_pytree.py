# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pytree as module_0
import _io as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    node_pattern_0 = module_0.NodePattern()
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type is None
    assert node_pattern_0.content is None
    assert node_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    none_type_0 = None
    var_0 = node_pattern_0.match(none_type_0, node_pattern_0)
    assert var_0 is True
    var_1 = node_pattern_0.optimize()
    var_0.match_seq(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    wildcard_pattern_0 = module_0.WildcardPattern()
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content is None
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = wildcard_pattern_0.optimize()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert var_0.content is None
    assert var_0.min == 0
    assert var_0.max == 2147483647
    assert var_0.name is None
    var_0.match(var_0, wildcard_pattern_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1092
    bytes_0 = b"^[ \\t\\f]*(?:[#\\r\\n]|$)"
    module_0.Node(int_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    negated_pattern_0 = module_0.NegatedPattern()
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert negated_pattern_0.content is None
    assert module_0.HUGE == 2147483647
    module_0.type_repr(none_type_0)


def test_case_4():
    dict_0 = {}
    with pytest.raises(AssertionError):
        module_0.WildcardPattern(dict_0, name=dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    wildcard_pattern_0 = module_0.WildcardPattern()
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content is None
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    module_0.Leaf(wildcard_pattern_0, wildcard_pattern_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    none_type_0 = None
    leaf_0 = module_0.Leaf(bool_0, none_type_0, prefix=bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is False
    assert leaf_0.value is None
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.__eq__(none_type_0)
    var_1 = leaf_0.get_lineno()
    assert var_1 == 0
    var_2 = var_1.__repr__()
    assert var_2 == "0"
    var_3 = leaf_0.remove()
    negated_pattern_0 = module_0.NegatedPattern(none_type_0)
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert negated_pattern_0.content is None
    var_3.insert_child(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    none_type_0 = None
    leaf_0 = module_0.Leaf(bool_0, none_type_0, prefix=bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is False
    assert leaf_0.value is None
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.get_lineno()
    assert var_0 == 0
    var_1 = var_0.__repr__()
    assert var_1 == "0"
    var_2 = leaf_0.remove()
    negated_pattern_0 = module_0.NegatedPattern(none_type_0)
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert negated_pattern_0.content is None
    var_2.insert_child(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = False
    none_type_0 = None
    leaf_0 = module_0.Leaf(bool_0, none_type_0, prefix=bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is False
    assert leaf_0.value is None
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.__repr__()
    assert var_0 == "Leaf(ENDMARKER, None)"
    leaf_0.replace(bool_0)


def test_case_9():
    none_type_0 = None
    int_0 = 35
    leaf_0 = module_0.Leaf(int_0, int_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type == 35
    assert leaf_0.value == 35
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.__eq__(none_type_0)
    var_1 = leaf_0.get_suffix()
    assert var_1 == ""
    var_2 = leaf_0.depth()
    assert var_2 == 0
    with pytest.raises(AssertionError):
        leaf_0.replace(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    list_0 = []
    node_pattern_0 = module_0.NodePattern(content=list_0, name=list_0)
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type is None
    assert node_pattern_0.content == []
    assert node_pattern_0.name == []
    assert module_0.HUGE == 2147483647
    var_0 = node_pattern_0.match_seq(list_0)
    assert var_0 is False
    var_1 = var_0.__eq__(node_pattern_0)
    node_pattern_0.match(var_1)


@pytest.mark.xfail(strict=True)
def test_case_11():
    list_0 = []
    node_pattern_0 = module_0.NodePattern(content=list_0, name=list_0)
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type is None
    assert node_pattern_0.content == []
    assert node_pattern_0.name == []
    assert module_0.HUGE == 2147483647
    node_pattern_0.match(list_0)


@pytest.mark.xfail(strict=True)
def test_case_12():
    str_0 = "i"
    none_type_0 = None
    wildcard_pattern_0 = module_0.WildcardPattern(name=str_0)
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content is None
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name == "i"
    assert module_0.HUGE == 2147483647
    var_0 = wildcard_pattern_0.match(none_type_0, none_type_0)
    assert var_0 is True
    var_1 = wildcard_pattern_0.match(none_type_0)
    assert var_1 is True
    var_2 = var_1.__repr__()
    assert var_2 == "True"
    var_3 = wildcard_pattern_0.generate_matches(wildcard_pattern_0)
    module_0.Base()


def test_case_13():
    bool_0 = True
    leaf_0 = module_0.Leaf(bool_0, bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is True
    assert leaf_0.value is True
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.__eq__(leaf_0)
    assert var_0 is True
    var_1 = leaf_0.__repr__()
    assert var_1 == "Leaf(NAME, True)"
    var_2 = leaf_0.clone()
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "pytree.Leaf"
    assert var_2.lineno == 0
    assert var_2.column == 0
    assert var_2.type is True
    assert var_2.value is True
    assert var_2.fixers_applied == []
    with pytest.raises(AssertionError):
        module_0.NegatedPattern(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    bool_0 = False
    leaf_0 = module_0.Leaf(bool_0, bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is False
    assert leaf_0.value is False
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.clone()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pytree.Leaf"
    assert var_0.lineno == 0
    assert var_0.column == 0
    assert var_0.type is False
    assert var_0.value is False
    assert var_0.fixers_applied == []
    var_1 = leaf_0.get_suffix()
    assert var_1 == ""
    var_2 = var_0.changed()
    assert var_0.was_changed is True
    module_0.type_repr(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    bool_0 = False
    leaf_0 = module_0.Leaf(bool_0, bool_0)
    assert f"{type(leaf_0).__module__}.{type(leaf_0).__qualname__}" == "pytree.Leaf"
    assert leaf_0.type is False
    assert leaf_0.value is False
    assert leaf_0.fixers_applied == []
    assert module_0.HUGE == 2147483647
    assert module_0.Leaf.lineno == 0
    assert module_0.Leaf.column == 0
    assert (
        f"{type(module_0.Leaf.prefix).__module__}.{type(module_0.Leaf.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = leaf_0.clone()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pytree.Leaf"
    assert var_0.lineno == 0
    assert var_0.column == 0
    assert var_0.type is False
    assert var_0.value is False
    assert var_0.fixers_applied == []
    var_1 = leaf_0.depth()
    assert var_1 == 0
    var_2 = leaf_0.get_suffix()
    assert var_2 == ""
    var_3 = var_0.changed()
    assert var_0.was_changed is True
    var_4 = leaf_0.depth()
    assert var_4 == 0
    var_4.optimize()


@pytest.mark.xfail(strict=True)
def test_case_16():
    leaf_pattern_0 = module_0.LeafPattern()
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type is None
    assert leaf_pattern_0.content is None
    assert leaf_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    none_type_0 = None
    var_0 = leaf_pattern_0.generate_matches(none_type_0)
    module_0.BasePattern(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    leaf_pattern_0 = module_0.LeafPattern()
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type is None
    assert leaf_pattern_0.content is None
    assert leaf_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = leaf_pattern_0.generate_matches(leaf_pattern_0)
    dict_0 = {leaf_pattern_0: leaf_pattern_0, var_0: var_0, var_0: var_0}
    var_0.__new__(dict_0, *var_0, **dict_0)


def test_case_18():
    bool_0 = False
    none_type_0 = None
    leaf_pattern_0 = module_0.LeafPattern(bool_0, name=bool_0)
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type is False
    assert leaf_pattern_0.content is None
    assert leaf_pattern_0.name is False
    assert module_0.HUGE == 2147483647
    var_0 = leaf_pattern_0.match(none_type_0)
    assert var_0 is False
    with pytest.raises(AssertionError):
        module_0.Node(var_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_19():
    bool_0 = False
    none_type_0 = None
    leaf_pattern_0 = module_0.LeafPattern(bool_0, name=bool_0)
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type is False
    assert leaf_pattern_0.content is None
    assert leaf_pattern_0.name is False
    assert module_0.HUGE == 2147483647
    var_0 = leaf_pattern_0.match(none_type_0)
    assert var_0 is False
    module_0.Base(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.generate_matches(bool_0, none_type_0)
    assert module_0.HUGE == 2147483647
    var_0.pre_order()


def test_case_21():
    bool_0 = False
    with pytest.raises(AssertionError):
        module_0.NegatedPattern(bool_0)


def test_case_22():
    float_0 = -2559.886
    text_i_o_base_0 = module_1._TextIOBase()
    with pytest.raises(AssertionError):
        module_0.WildcardPattern(min=float_0, name=text_i_o_base_0)


def test_case_23():
    bool_0 = True
    with pytest.raises(AssertionError):
        module_0.NodePattern(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_24():
    negated_pattern_0 = module_0.NegatedPattern()
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert negated_pattern_0.content is None
    assert module_0.HUGE == 2147483647
    negated_pattern_1 = module_0.NegatedPattern()
    none_type_0 = None
    var_0 = negated_pattern_0.match(none_type_0)
    assert var_0 is False
    negated_pattern_0.match_seq(negated_pattern_1)


def test_case_25():
    int_0 = -1204
    none_type_0 = None
    with pytest.raises(AssertionError):
        module_0.Leaf(int_0, int_0, prefix=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_26():
    str_0 = "R"
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content == (("R",),)
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = wildcard_pattern_0.optimize()
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert var_0.content == (("R",),)
    assert var_0.min == 0
    assert var_0.max == 2147483647
    assert var_0.name is None
    var_1 = wildcard_pattern_0.optimize()
    assert var_1.content == (("R",),)
    assert var_1.min == 0
    assert var_1.max == 2147483647
    wildcard_pattern_0.match(str_0)


@pytest.mark.xfail(strict=True)
def test_case_27():
    str_0 = "',A3Q0s"
    wildcard_pattern_0 = module_0.WildcardPattern(str_0)
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content == (
        ("'",),
        (",",),
        ("A",),
        ("3",),
        ("Q",),
        ("0",),
        ("s",),
    )
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    leaf_pattern_0 = module_0.LeafPattern(content=str_0)
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type is None
    assert leaf_pattern_0.content == "',A3Q0s"
    assert leaf_pattern_0.name is None
    wildcard_pattern_0.match(str_0)


def test_case_28():
    str_0 = ".txt"
    var_0 = module_0.convert(str_0, str_0)
    assert var_0 == "t"
    assert module_0.HUGE == 2147483647
    with pytest.raises(AssertionError):
        module_0.NodePattern(content=str_0, name=var_0)


@pytest.mark.xfail(strict=True)
def test_case_29():
    str_0 = ".txt"
    var_0 = module_0.convert(str_0, str_0)
    assert var_0 == "t"
    assert module_0.HUGE == 2147483647
    var_0.match(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_30():
    float_0 = 2291.0
    list_0 = []
    node_0 = module_0.Node(float_0, list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "pytree.Node"
    assert node_0.type == pytest.approx(2291.0, abs=0.01, rel=0.01)
    assert node_0.children == []
    assert node_0.fixers_applied is None
    assert module_0.HUGE == 2147483647
    assert (
        f"{type(module_0.Node.prefix).__module__}.{type(module_0.Node.prefix).__qualname__}"
        == "builtins.property"
    )
    node_0.set_child(list_0, node_0)


@pytest.mark.xfail(strict=True)
def test_case_31():
    float_0 = 2291.0
    list_0 = []
    node_0 = module_0.Node(float_0, list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "pytree.Node"
    assert node_0.type == pytest.approx(2291.0, abs=0.01, rel=0.01)
    assert node_0.children == []
    assert node_0.fixers_applied is None
    assert module_0.HUGE == 2147483647
    assert (
        f"{type(module_0.Node.prefix).__module__}.{type(module_0.Node.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = node_0.clone()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pytree.Node"
    assert var_0.type == pytest.approx(2291.0, abs=0.01, rel=0.01)
    assert var_0.children == []
    assert var_0.fixers_applied is None
    node_0.__repr__()


@pytest.mark.xfail(strict=True)
def test_case_32():
    float_0 = 2291.0
    list_0 = []
    node_0 = module_0.Node(float_0, list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "pytree.Node"
    assert node_0.type == pytest.approx(2291.0, abs=0.01, rel=0.01)
    assert node_0.children == []
    assert node_0.fixers_applied is None
    assert module_0.HUGE == 2147483647
    assert (
        f"{type(module_0.Node.prefix).__module__}.{type(module_0.Node.prefix).__qualname__}"
        == "builtins.property"
    )
    var_0 = node_0.clone()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "pytree.Node"
    assert var_0.type == pytest.approx(2291.0, abs=0.01, rel=0.01)
    assert var_0.children == []
    assert var_0.fixers_applied is None
    node_0.__repr__()


@pytest.mark.xfail(strict=True)
def test_case_33():
    int_0 = -1508
    node_pattern_0 = module_0.NodePattern()
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type is None
    assert node_pattern_0.content is None
    assert node_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = node_pattern_0.match(node_pattern_0)
    assert var_0 is True
    var_0.match_seq(int_0)


def test_case_34():
    int_0 = 2373
    none_type_0 = None
    node_pattern_0 = module_0.NodePattern(int_0, name=int_0)
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type == 2373
    assert node_pattern_0.content is None
    assert node_pattern_0.name == 2373
    assert module_0.HUGE == 2147483647
    with pytest.raises(AssertionError):
        module_0.Leaf(int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_35():
    negated_pattern_0 = module_0.NegatedPattern()
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert negated_pattern_0.content is None
    assert module_0.HUGE == 2147483647
    var_0 = module_0.generate_matches(negated_pattern_0, negated_pattern_0)
    var_0.optimize()


def test_case_36():
    bool_0 = True
    with pytest.raises(AssertionError):
        module_0.LeafPattern(bool_0, bool_0)


def test_case_37():
    int_0 = 38
    leaf_pattern_0 = module_0.LeafPattern(int_0)
    assert (
        f"{type(leaf_pattern_0).__module__}.{type(leaf_pattern_0).__qualname__}"
        == "pytree.LeafPattern"
    )
    assert leaf_pattern_0.type == 38
    assert leaf_pattern_0.content is None
    assert leaf_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    float_0 = -620.88404
    with pytest.raises(AssertionError):
        module_0.WildcardPattern(max=float_0)


@pytest.mark.xfail(strict=True)
def test_case_38():
    node_pattern_0 = module_0.NodePattern()
    assert (
        f"{type(node_pattern_0).__module__}.{type(node_pattern_0).__qualname__}"
        == "pytree.NodePattern"
    )
    assert node_pattern_0.type is None
    assert node_pattern_0.content is None
    assert node_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    set_0 = {node_pattern_0}
    negated_pattern_0 = module_0.NegatedPattern(node_pattern_0)
    assert (
        f"{type(negated_pattern_0).__module__}.{type(negated_pattern_0).__qualname__}"
        == "pytree.NegatedPattern"
    )
    assert (
        f"{type(negated_pattern_0.content).__module__}.{type(negated_pattern_0.content).__qualname__}"
        == "pytree.NodePattern"
    )
    var_0 = negated_pattern_0.generate_matches(set_0)
    none_type_0 = None
    node_pattern_0.match_seq(set_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_39():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    wildcard_pattern_0 = module_0.WildcardPattern()
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content is None
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = wildcard_pattern_0.match(dict_0, dict_0)
    assert var_0 is True
    none_type_0 = None
    module_0.convert(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_40():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    wildcard_pattern_0 = module_0.WildcardPattern()
    assert (
        f"{type(wildcard_pattern_0).__module__}.{type(wildcard_pattern_0).__qualname__}"
        == "pytree.WildcardPattern"
    )
    assert wildcard_pattern_0.content is None
    assert wildcard_pattern_0.min == 0
    assert wildcard_pattern_0.max == 2147483647
    assert wildcard_pattern_0.name is None
    assert module_0.HUGE == 2147483647
    var_0 = wildcard_pattern_0.match(dict_0, dict_0)
    assert var_0 is True
    none_type_0 = None
    module_0.convert(none_type_0, none_type_0)


def test_case_41():
    int_0 = 4236
    with pytest.raises(AssertionError):
        module_0.LeafPattern(int_0)
