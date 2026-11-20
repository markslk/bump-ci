# test_bump.py: pytest runs every function whose name starts with test_
# The next line loads bump_patch from bump.py.
from bump import bump_patch


def test_bump_simple():
    assert bump_patch("1.4.2") == "1.4.3"      # assert = this must be true, or the test fails


def test_bump_nine_becomes_ten():
    assert bump_patch("2.0.9") == "2.0.10"     # the last part can grow past 9
