from my_package import my_module

def test_topn():

    """Test the topn function."""

    assert my_module.topn([1, 2, 3, 4, 5], 3) == [5, 4, 3], "Test failed"
    assert my_module.topn([8, 3, 2, 7, 4], 3) == [8, 7, 4], "Test failed"
    assert my_module.topn([1, 2, 3, 4, 5], 0) == [], "Test failed"