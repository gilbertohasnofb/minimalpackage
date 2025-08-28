from minimalpackage.module1 import Class1


def test_class1():
    c1 = Class1()
    assert c1.some_attribute == "some_attribute"
    assert c1.some_method() == "function1 called in some_method()"
