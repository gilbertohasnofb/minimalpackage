import minimalpackage


def test_class2():
    c2 = minimalpackage.Class2()
    assert c2.some_attribute == 'some_attribute'
    assert c2.some_method() == 'function2 called in some_method()'