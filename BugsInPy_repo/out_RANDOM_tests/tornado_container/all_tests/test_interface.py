# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import interface as module_0
import builtins as module_1


def test_case_0():
    waker_0 = module_0.Waker()


def test_case_1():
    bool_0 = True
    module_0.set_close_exec(bool_0)


def test_case_2():
    set_0 = set()
    module_0.set_close_exec(set_0)


def test_case_3():
    list_0 = []
    waker_0 = module_0.Waker(*list_0)
    waker_0.consume()


def test_case_4():
    int_0 = 879
    tuple_0 = (int_0,)
    module_0.set_close_exec(tuple_0)


def test_case_5():
    complex_0 = -279.8 - 2412.5j
    module_0.set_close_exec(complex_0)


def test_case_6():
    str_0 = "/sp5#+u"
    dict_0 = {str_0: str_0}
    module_1.object(**dict_0)


def test_case_7():
    str_0 = "_F4"
    module_0.set_close_exec(str_0)


def test_case_8():
    waker_0 = module_0.Waker()
    waker_0.fileno()


def test_case_9():
    waker_0 = module_0.Waker()
    waker_0.consume()


def test_case_10():
    int_0 = -948
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.Waker(*list_0, **list_0)


def test_case_11():
    bytes_0 = b""
    module_0.set_close_exec(bytes_0)


def test_case_12():
    pass


def test_case_13():
    none_type_0 = None
    module_0.Waker(*none_type_0)


def test_case_14():
    bytes_0 = b"\xe9\xa9\xd1 \xbb\x9c\x11\xf8`\xca\xfc\xbc\x82\xbf\xb9?\xe3\xae"
    module_0.set_close_exec(bytes_0)


def test_case_15():
    waker_0 = module_0.Waker()
    waker_0.close()


def test_case_16():
    waker_0 = module_0.Waker()
    module_0.set_close_exec(waker_0)


def test_case_17():
    bool_0 = True
    bool_1 = True
    int_0 = -1334
    dict_0 = {bool_0: bool_1, bool_0: bool_1, bool_1: bool_0, bool_0: int_0}
    module_0.set_close_exec(dict_0)


def test_case_18():
    int_0 = 3093
    set_0 = {int_0, int_0, int_0, int_0}
    module_0.set_close_exec(set_0)


def test_case_19():
    waker_0 = module_0.Waker()
    waker_0.close()


def test_case_20():
    str_0 = ";w~4e|'G1s0I8\r]"
    str_1 = "\x0bhBE G"
    str_2 = "$U"
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_1, str_1: str_1}
    module_0.Waker(**dict_0)


def test_case_21():
    waker_0 = module_0.Waker()
    str_0 = "P\nH\raF6#m!)6\nW\ra\x0bQn"
    str_1 = "V~,: vzF\x0c6RJ+?7?"
    dict_0 = {str_0: str_0, str_1: str_1, str_1: waker_0}
    module_0.Waker(**dict_0)


def test_case_22():
    none_type_0 = None
    module_0.set_close_exec(none_type_0)


def test_case_23():
    bool_0 = False
    bytes_0 = b'\xe2\xb2",=\xf5\x1a\xa5\xbc'
    tuple_0 = (bool_0, bool_0, bool_0, bytes_0)
    list_0 = [tuple_0, bool_0, tuple_0, bool_0]
    module_0.set_close_exec(list_0)


def test_case_24():
    waker_0 = module_0.Waker()
    waker_0.fileno()


def test_case_25():
    str_0 = ":mN"
    list_0 = [str_0, str_0]
    module_0.set_close_exec(list_0)


def test_case_26():
    pass


def test_case_27():
    waker_0 = module_0.Waker()
    waker_0.fileno()


def test_case_28():
    int_0 = 1638
    module_0.set_close_exec(int_0)


def test_case_29():
    waker_0 = module_0.Waker()
    waker_0.consume()


def test_case_30():
    str_0 = "H"
    none_type_0 = None
    str_1 = "{g`"
    dict_0 = {str_0: none_type_0, str_1: none_type_0}
    module_0.Waker(**dict_0)


def test_case_31():
    str_0 = "I+?+xk$Yz "
    str_1 = "nVV#0"
    dict_0 = {str_0: str_0, str_1: str_1}
    module_0.Waker(**dict_0)


def test_case_32():
    waker_0 = module_0.Waker()
    waker_0.wake()


def test_case_33():
    bool_0 = True
    module_0.set_close_exec(bool_0)


def test_case_34():
    waker_0 = module_0.Waker()
    waker_0.fileno()


def test_case_35():
    none_type_0 = None
    module_0.set_close_exec(none_type_0)


def test_case_36():
    waker_0 = module_0.Waker()
    waker_0.write_fileno()
