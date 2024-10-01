from libs.gratitudes import *

def test_share_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Family")
    gratitudes.add("Friends")
    gratitudes.add("Work")
    result = gratitudes.format()
    assert result == "Be grateful for: Family, Friends, Work"