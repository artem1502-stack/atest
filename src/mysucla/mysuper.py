
class MySuperClass:
	sign: int
	data: str

	def __init__(self, data=None, sign=0):
		if data is None:
			data = ""
		self.data = data
		self.sign = sign

	def __add__(self, other):
		c = MySuperClass
		c.data = self.data + other.data
		c.sign = max(self.sign, other.sign)
		return c


def sk_do(a):
	return len(a) >= 5
