from libs.report_length import *

def test_string_length_correct():
    result = report_length("Hello")
    assert result == f"This string was 5 characters long."

def test_string_length_incorrect():
    result = report_length("Hello")
    assert result != f"This string was 270 characters long."
    
    def test_string_length_correct():
        result = report_length("Tomorrow")
        assert result == f"This string was 8 characters long."
    
    def test_string_length_incorrect():
        result = report_length("Hello")
        assert result != f"This string was 5 characters long."