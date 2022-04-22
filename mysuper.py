
class MySuperClass:
	data: list
	sign: int

	def __int__(self, data=[], sign=0):
		self.data = data
		self.sign = sign

	def __add__(self, other):
		self.data += other.data
		self.sign = max(self.sign, other.sign)


if __name__ == '__main__':
	print("MySUSUCLASSSSS, HELL YEAH!!!")
