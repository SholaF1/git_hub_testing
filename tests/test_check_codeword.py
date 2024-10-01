from libs.check_codeword import *

def test_check_codeword_result_correct():
    result = check_codeword("horse")
    assert "Correct! Come in."
    
    
def test_check_codeword_result_incorrect():
    result = check_codeword("water")
    assert "WRONG!"

def test_check_codeword_result_close():
    result = check_codeword("house")
    assert "Close, but nope."
    
def test_check_right_first_letter_and_wrong_last_letter():
    result = check_codeword("hat")
    assert "WRONG!"
    
def test_check_wrong_first_letter_and_right_last_letter():
    result = check_codeword("mouse")
    assert "WRONG!"