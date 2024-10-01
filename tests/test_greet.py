from libs.greet import *

def test_greeting_hello_given_name():
    result = greet("Shola")
    assert result == f"Hello Shola, !"