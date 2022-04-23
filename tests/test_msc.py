from mysucla.mysuper import MySuperClass


def test_msc():
	a = MySuperClass("abc", 1)
	b = MySuperClass("def")
	c = a + b
	assert a.sign == 1
	assert b.sign == 0
	assert c.sign == 1
	assert c.data == a.data + b.data
