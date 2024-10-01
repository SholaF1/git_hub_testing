from libs.counter import *

def test_number_counter_to():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == f"Counted to 3 so far."