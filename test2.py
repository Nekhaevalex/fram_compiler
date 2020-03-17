class new_class():
	"""docstring for new_class"""
	def __init__(self, arg):
		self.arg = arg
		self.arg = "arg"+arg
		print(self.arg)

b = "12345"
a = new_class(b)
c = a.arg
print(b)
print(c)
