# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pretty as module_0


def test_case_0():
    h_t_t_p_lexer_0 = module_0.HTTPLexer()
    assert (
        f"{type(h_t_t_p_lexer_0).__module__}.{type(h_t_t_p_lexer_0).__qualname__}"
        == "pretty.HTTPLexer"
    )
    assert h_t_t_p_lexer_0.options == {}
    assert h_t_t_p_lexer_0.stripnl is True
    assert h_t_t_p_lexer_0.stripall is False
    assert h_t_t_p_lexer_0.ensurenl is True
    assert h_t_t_p_lexer_0.tabsize == 0
    assert h_t_t_p_lexer_0.encoding == "guess"
    assert h_t_t_p_lexer_0.filters == []
    assert module_0.DEFAULT_STYLE == "solarized"
    assert module_0.AVAILABLE_STYLES == [
        "solarized",
        "abap",
        "algol",
        "algol_nu",
        "arduino",
        "autumn",
        "bw",
        "borland",
        "coffee",
        "colorful",
        "default",
        "dracula",
        "emacs",
        "friendly_grayscale",
        "friendly",
        "fruity",
        "github-dark",
        "gruvbox-dark",
        "gruvbox-light",
        "igor",
        "inkpot",
        "lightbulb",
        "lilypond",
        "lovelace",
        "manni",
        "material",
        "monokai",
        "murphy",
        "native",
        "nord-darker",
        "nord",
        "one-dark",
        "paraiso-dark",
        "paraiso-light",
        "pastie",
        "perldoc",
        "rainbow_dash",
        "rrt",
        "sas",
        "solarized-dark",
        "solarized-light",
        "staroffice",
        "stata-dark",
        "stata-light",
        "tango",
        "trac",
        "vim",
        "vs",
        "xcode",
        "zenburn",
    ]
    assert module_0.HTTPLexer.name == "HTTP"
    assert module_0.HTTPLexer.aliases == ["http"]
    assert module_0.HTTPLexer.filenames == ["*.http"]
    assert len(module_0.HTTPLexer.tokens) == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.PrettyHttp(none_type_0)
