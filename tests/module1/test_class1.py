import minimalpackage


def test_class1():
    """test docstring"""
    c1 = minimalpackage.Class1()
    assert c1.some_attribute == 'some_attribute'
    assert c1.some_method() == 'function1 called in some_method()'
