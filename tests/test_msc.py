from mysucla.mysuper import MySuperClass, sk_do
import pytest


@pytest.mark.parametrize("test_input,expected", [
	("abcd", False),
	("vjfonjfn", True),
	("12345", True),
])
def test_multi(test_input, expected):
	assert sk_do(test_input) is expected


def test_sum():
	a = MySuperClass("abc", 1)
	b = MySuperClass("def")
	d = MySuperClass("", 0)
	f = MySuperClass()
	c = a + b
	assert a.sign == 1
	assert b.sign == 0
	assert c.sign == 1
	assert c.data == a.data + b.data
	assert (b + d).sign == 0
	assert f.sign == 0
	assert f.data == ""
