def test_get_stats(text_manager):
    res = text_manager.get_stats()
    assert isinstance(res, str)
