from minimalpackage.module3 import function3


def test_function3():
    df = function3()
    assert df.loc[0, "id"] == 0
    assert df.loc[0, "name"] == "Sample Item A"
    assert df.loc[1, "id"] == 1
    assert df.loc[1, "name"] == "Sample Item B"
