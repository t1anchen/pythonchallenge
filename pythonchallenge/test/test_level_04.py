from pc.level_04 import solution


def test_integration():
    actual = solution()
    expected = "peak"
    assert expected == actual
