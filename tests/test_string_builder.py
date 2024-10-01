from libs.string_builder import *

def test_build_a_string():
    string_builder = StringBuilder()
    string_builder.add("Shola")
    assert string_builder.size() == 5
    result = string_builder.output()
    assert result == "Shola"