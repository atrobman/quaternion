from math import cos, sin, exp, log, atan2

class Quaternion:

	def __init__(self, a, b):
		# self.a = a
		# self.b = b

	def mul(self, comp):
		# na = self.a * comp.a - self.b * comp.b
		# nb = self.a * comp.b + self.b * comp.a

		# return Complex(na, nb)

	def add(self, comp):
		# na = self.a + comp.a
		# nb = self.b + comp.b

		# return Complex(na, nb)

	def sub(self, comp):
		# na = self.a - comp.a
		# nb = self.b - comp.b

		# return Complex(na, nb)

	def div(self, comp):
		# if (comp.a ** 2 + comp.b ** 2) != 0:
		# 	na = (self.a * comp.a + self.b * comp.b) / (comp.a ** 2 + comp.b ** 2)
		# 	nb = (self.b * comp.a - self.a * comp.b) / (comp.a ** 2 + comp.b ** 2)

		# 	return Complex(na, nb)
		# else:
		# 	raise ZeroDivisionError("division by zero")

	def pow(self, comp):

		# if self.a == 0 and self.b == 0 and comp.a == 0 and comp.b == 0:
		# 	raise ArithmeticError("indefinite power")

		# elif self.a == 0 and self.b == 0:
		# 	return Complex(0, 0)

		# elif self.a == 1 and self.b == 0:
		# 	return Complex(1, 0)

		# elif comp.a == 0 and comp.b == 0:
		# 	return Complex(1, 0)

		# elif comp.a == 1 and comp.b == 0:
		# 	return Complex(self.a, self.b)

		# else:
		# 	mult1 = (self.a ** 2 + self.b ** 2) ** (comp.a / 2) * exp(-comp.b * atan2(self.b, self.a))
		# 	real_mult = cos(comp.a * atan2(self.b, self.a) + .5 * comp.b * log(self.a**2 + self.b**2))
		# 	imag_mult = sin(comp.a * atan2(self.b, self.a) + .5 * comp.b * log(self.a**2 + self.b**2))

		# 	na = mult1 * real_mult
		# 	nb = mult1 * imag_mult

		# 	return Complex(na, nb)

	def __str__(self):

		# msg = ""
		# if self.a != 0:
		# 	msg += f"{self.a} "

		# if self.b != 0:
		# 	if self.b > 0 and self.a != 0:
		# 		msg += f"+ {self.b}*i"
		# 	elif self.b < 0 and self.a != 0:
		# 		msg += f"- {self.b*-1}*i"
		# 	elif self.b > 0 and self.a == 0:
		# 		msg += f"{self.b}*i"
		# 	elif self.b < 0 and self.a == 0:
		# 		msg += f"{self.b}*i"

		# elif msg == "":
		# 		msg = "0"

		# return msg